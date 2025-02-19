"""
Instantiation of configuration objects.
"""

import ast
import builtins
import dataclasses
import os
import pprint
import types
import typing
import uuid
from contextlib import contextmanager
from copy import deepcopy

import iopathlib as file_io
import omegaconf
import yaml
from hydra.core.override_parser.overrides_parser import OverridesParser
from omegaconf import DictConfig, ListConfig

from . import _env as env
from .utils import generate_path, locate_object

__all__ = [
    "apply_overrides",
    "instantiate",
    "dump_config",
    "save_config",
    "load_config_local",
    "load_config_remote",
]

CONFIGS_ROOT = os.getenv("LACO_ROOT", "./")

LAZY_TARGET: typing.Final = "_target_"
LAZY_ARGS: typing.Final = "_args_"
OMEGA_DICT_FLAGS: typing.Final = {"allow_objects": True}

if typing.TYPE_CHECKING:

    class LazyObject[_L]:
        def __getattr__(self, name: str) -> typing.Any: ...

        @typing.override
        def __setattr__(self, __name: str, __value: typing.Any) -> None: ...

else:

    class LazyObject(dict[str, typing.Any]):
        def __class_getitem__(cls, item: typing.Any) -> dict[str, typing.Any]:
            return types.GenericAlias(dict, (str, typing.Any))


KEY_VERSION: typing.Final = "VERSION"
KEY_MODEL: typing.Final = "MODEL"
KEY_ENGINE: typing.Final = "ENGINE"
KEY_NAME: typing.Final = "NAME"
KEY_SESSION_ID: typing.Final = "SESSION_ID"
KEY_WEIGHTS: typing.Final = "WEIGHTS"

type AnyConfig = DictConfig | ListConfig

_PACKAGE_PREFIX: typing.Final = "_config_"


def _apply_recursive[_C: (DictConfig, ListConfig)](
    cfg: _C, func: typing.Callable[[_C], None]
) -> None:
    """
    Apply func recursively to all DictConfig in cfg.
    """
    if isinstance(cfg, DictConfig):
        func(cfg)
        for v in cfg.values():
            _apply_recursive(v, func)
    elif isinstance(cfg, ListConfig):
        for v in cfg:
            _apply_recursive(v, func)


def _validate_syntax(filename):
    """
    Validate the syntax of a Python-based configuration file.
    """
    with file_io.open(filename, "r") as f:
        content = f.read()
    try:
        ast.parse(content)
    except SyntaxError as e:
        raise SyntaxError(f"Config file {filename} has syntax error!") from e


def _as_omegadict(obj: dict | DictConfig) -> omegaconf.DictConfig:
    if isinstance(obj, dict):
        return DictConfig(obj, flags=OMEGA_DICT_FLAGS)
    return obj


def _generate_packagename(path: str):
    # generate a random package name when loading config files
    return _PACKAGE_PREFIX + str(uuid.uuid4())[:4] + "." + os.path.basename(path)


@contextmanager
def _patch_import():
    """
    Context manager that patches ``builtins.__import__`` to:
    - locate files purely based on relative location, regardless of packages.
            e.g. you can import file without having __init__
    - do not cache modules globally; modifications of module states has no side effect
    - support other storage system through file_io, so config files can be in the cloud
    - imported dict are turned into DictConfig automatically
    """
    import importlib.machinery
    import importlib.util

    # Reference the 'original' import function such that we can revert to normal behavior
    # after exiting the context manager.
    import_default = builtins.__import__

    def find_relative(original_file, relative_import_path, level):
        # NOTE: "from . import x" is not handled. Because then it's unclear
        # if such import should produce `x` as a python module or DictConfig.
        # This can be discussed further if needed.
        relative_import_err = (
            "Relative import of directories is not allowed within config files. "
            "Within a config file, relative import can only import other config files."
        )
        if not len(relative_import_path):
            raise ImportError(relative_import_err)

        cur_file = os.path.dirname(original_file)
        for _ in range(level - 1):
            cur_file = os.path.dirname(cur_file)
        cur_name = relative_import_path.lstrip(".")
        for part in cur_name.split("."):
            cur_file = os.path.join(cur_file, part)
        if not cur_file.endswith(".py"):
            cur_file += ".py"
        if not file_io.isfile(cur_file):
            cur_file_no_suffix = cur_file[: -len(".py")]
            if file_io.isdir(cur_file_no_suffix):
                raise ImportError(
                    f"Cannot import from {cur_file_no_suffix}." + relative_import_err
                )
            raise ImportError(
                f"Cannot import name {relative_import_path} from "
                f"{original_file}: {cur_file} does not exist."
            )
        return cur_file

    def import_patched(name, globals=None, locals=None, fromlist=(), level=0):
        if (
            # Only deal with relative imports inside config files
            level != 0
            and globals is not None
            and (globals.get("__package__", "") or "").startswith(_PACKAGE_PREFIX)
        ):
            cur_file = find_relative(globals["__file__"], name, level)
            _validate_syntax(cur_file)
            spec = importlib.machinery.ModuleSpec(
                _generate_packagename(cur_file), None, origin=cur_file
            )
            module = importlib.util.module_from_spec(spec)
            module.__file__ = cur_file
            with file_io.open(cur_file) as f:
                content = f.read()
            exec(compile(content, cur_file, "exec"), module.__dict__)
            for name in fromlist:  # turn imported dict into DictConfig automatically
                val = _as_omegadict(module.__dict__[name])
                module.__dict__[name] = val
            return module
        return import_default(name, globals, locals, fromlist=fromlist, level=level)

    builtins.__import__ = import_patched
    yield import_patched
    builtins.__import__ = import_default


def _filepath_to_name(path: str | file_io.Path) -> str | None:
    """
    Convert a file path to a module name.
    """

    configs_root = file_io.Path(CONFIGS_ROOT).resolve()
    path = file_io.Path(path).resolve()
    try:
        # If the file is under "./configs", then we can use the relative path to generate a name
        name = path.relative_to(configs_root).parent.as_posix() + "/" + path.stem
    except Exception:
        # Otherwise, we use the absolute path and find the name using the filename without suffix
        name = "/".join([path.parent.stem, path.stem])

    name = name.replace("./", "")
    name = name.replace("//", "/")

    if name in {"__init__", "defaults", "unknown", "config", "configs"}:
        return None
    return name.removesuffix(".py")


def load_config_remote(path: str):
    """
    Load a configuration from a remote source. Currently accepted external configuration
    sources are:

    - `Weights & Biases <https://wandb.ai/>`_ runs: ``wandb-run://<run_id>``

    Users should prefer to load configurations via the unified API with
    :func:`unipercept.read_config` instead of calling this method directly.
    """
    from unipercept.engine.integrations.wandb_integration import WANDB_RUN_PREFIX
    from unipercept.engine.integrations.wandb_integration import (
        read_run as wandb_read_run,
    )

    if path.startswith(WANDB_RUN_PREFIX):
        run = wandb_read_run(path)
        cfg = DictConfig(run.config)
    else:
        raise FileNotFoundError(path)

    return cfg


def load_config_local(path: str):
    """
    Loads a configuration from a local source.

    Users should prefer to load configurations via the unified API with
    :func:`unipercept.read_config` instead of calling this method directly.
    """
    from laco import __version__ as version

    ext = os.path.splitext(path)[1]
    match ext.lower():
        case ".py":
            _validate_syntax(path)

            with _patch_import():
                # Record the filename
                nsp = {
                    "__file__": path,
                    "__package__": _generate_packagename(path),
                }
                with file_io.open(path) as f:
                    content = f.read()
                # Compile first with filename to:
                # 1. make filename appears in stacktrace
                # 2. make load_rel able to find its parent's (possibly remote) location
                exec(compile(content, file_io.get_local_path(path), "exec"), nsp)

            export = nsp.get(
                "__all__",
                (
                    k
                    for k, v in nsp.items()
                    if not k.startswith("_")
                    and (
                        isinstance(
                            v,
                            (
                                dict,
                                list,
                                DictConfig,
                                ListConfig,
                                int,
                                float,
                                str,
                                bool,
                            ),
                        )
                        or v is None
                    )
                ),
            )
            obj: dict[str, typing.Any] = {k: v for k, v in nsp.items() if k in export}
            obj.setdefault(KEY_NAME, _filepath_to_name(path))
            obj.setdefault(KEY_VERSION, version)

        case ".yaml":
            with file_io.open(path) as f:
                obj = yaml.unsafe_load(f)
            obj.setdefault(KEY_NAME, "unknown")
            obj.setdefault(KEY_VERSION, "unknown")
        case _:
            msg = "Unsupported file extension %s!"
            raise ValueError(msg, ext)

    cfg = _as_omegadict(obj)
    return cfg


def dump_config(cfg) -> str:
    if not isinstance(cfg, DictConfig):
        cfg = _as_omegadict(
            dataclasses.asdict(cfg) if dataclasses.is_dataclass(cfg) else cfg
        )
    try:
        cfg = deepcopy(cfg)
    except Exception:
        pass
    else:
        # if it's deep-copyable, then...
        def _replace_type_by_name(x):
            if LAZY_TARGET in x and callable(x._target_):
                try:
                    x._target_ = generate_path(x._target_)
                except AttributeError:
                    pass

        # not necessary, but makes yaml looks nicer
        _apply_recursive(cfg, _replace_type_by_name)

    try:
        cfg_as_dict = omegaconf.OmegaConf.to_container(
            cfg,
            # Do not resolve interpolation when saving, i.e. do not turn ${a} into
            # actual values when saving.
            resolve=False,
            # Save structures (dataclasses) in a format that can be instantiated later.
            # Without this option, the type information of the dataclass will be erased.
            structured_config_mode=omegaconf.SCMode.INSTANTIATE,
        )
    except Exception as err:
        cfg_pretty = pprint.pformat(omegaconf.OmegaConf.to_container(cfg)).replace(
            "\n", "\n\t"
        )
        msg = f"Config cannot be converted to a dict!\n\nConfig node:\n{cfg_pretty}"
        raise ValueError(msg) from err

    dump_kwargs = {"default_flow_style": None, "allow_unicode": True}

    def _find_undumpable(cfg_as_dict, *, _key=()) -> tuple[str, ...] | None:
        for key, value in cfg_as_dict.items():
            if not isinstance(value, dict):
                continue
            try:
                _ = yaml.dump(value, **dump_kwargs)
                continue
            except Exception:
                pass
            key_with_error = _find_undumpable(value, _key=_key + (key,))
            if key_with_error:
                return key_with_error
            return _key + (key,)
        return None

    try:
        dumped = yaml.dump(cfg_as_dict, **dump_kwargs)
    except Exception as err:
        cfg_pretty = pprint.pformat(cfg_as_dict).replace("\n", "\n\t")
        problem_key = _find_undumpable(cfg_as_dict)
        if problem_key:
            problem_key = ".".join(problem_key)
            msg = f"Config cannot be saved due to key {problem_key!r}"
        else:
            msg = "Config cannot be saved due to an unknown entry"
        msg += f"\n\nConfig node:\n\t{cfg_pretty}"
        raise SyntaxError(msg) from err

    return dumped


def save_config(cfg, path: str):
    """
    Save a config object to a yaml file.

    Parameters
    ----------
    cfg
        An omegaconf config object.
    filename
        The file name to save the config file.

    Notes
    -----
    When the config dictionary contains complex objects (e.g. lambda), it cannot be saved to yaml.
    In that case, an error will be printed and the config will be saved to a pkl file instead.
    """
    local_path = file_io.get_local_path(path)
    if not local_path.endswith(".yaml"):
        msg = f"Config file should be saved as a yaml file! Got: {path}"
        raise ValueError(msg)

    dumped = dump_config(cfg)
    try:
        with open(local_path, "w") as fh:
            fh.write(dumped)
        _ = yaml.unsafe_load(dumped)
    except Exception as err:
        msg = f"Config file cannot be saved at {local_path!r}"
        raise SyntaxError(msg) from err


def apply_overrides(cfg, overrides: list[str]):
    """
    In-place override contents of cfg.

    Parameters
    ----------
    cfg
        An omegaconf config object
    overrides
        List of strings in the format of "a=b" to override configs.
        See: https://hydra.cc/docs/next/advanced/override_grammar/basic/

    Returns
    -------
    DictConfig
        Lazy configuration object
    """

    def safe_update(cfg, key, value):
        parts = key.split(".")
        for idx in range(1, len(parts)):
            prefix = ".".join(parts[:idx])
            v = omegaconf.OmegaConf.select(cfg, prefix, default=None)
            if v is None:
                break
            if not omegaconf.OmegaConf.is_config(v):
                raise KeyError(
                    f"Trying to update key {key}, but {prefix} "
                    f"is not a config, but has type {type(v)}."
                )
        omegaconf.OmegaConf.update(cfg, key, value, merge=True)

    for o in OverridesParser.create().parse_overrides(overrides):
        key = o.key_or_group
        value = o.value()
        if o.is_delete():
            raise NotImplementedError("deletion is not yet a supported override")
        safe_update(cfg, key, value)

    return cfg


def migrate_target(target: typing.Any) -> typing.Any:
    return target


_INST_SEQ_TYPEMAP: dict[type, type] = {
    ListConfig: list,
    list: list,
    tuple: tuple,
    set: set,
    frozenset: frozenset,
}


def instantiate(cfg: typing.Any, /) -> object:
    """
    Recursively instantiate objects defined in dictionaries with keys:

    - Special key ``LAZY_TARGET``: defines the callable/objec to be instantiated.
    - Special key ``"_args_"``: defines the positional arguments to be passed to the callable.
    - Other keys define the keyword arguments to be passed to the callable.
    """
    if cfg is None or isinstance(
        cfg,
        (
            int,
            float,
            bool,
            str,
            set,
            frozenset,
            bytes,
            type,
            types.NoneType,
            types.FunctionType,
        ),
    ):
        return cfg  # type: ignore

    if env.get_env(bool, "UP_CONFIG_TRACE", default=False):
        logger.info(
            "Instantiating %s", pprint.pprint(omegaconf.OmegaConf.to_container(cfg))
        )

    if isinstance(cfg, typing.Sequence) and not isinstance(
        cfg, (typing.Mapping, str, bytes)
    ):
        cls = type(cfg)
        cls = _INST_SEQ_TYPEMAP.get(cls, cls)
        return cls(instantiate(x) for x in cfg)

    # If input is a DictConfig backed by dataclasses (i.e. omegaconf's structured config),
    # instantiate it to the actual dataclass.
    if isinstance(cfg, DictConfig) and dataclasses.is_dataclass(
        cfg._metadata.object_type
    ):
        return omegaconf.OmegaConf.to_object(cfg)

    if isinstance(cfg, typing.Mapping) and LAZY_TARGET in cfg:
        # conceptually equivalent to hydra.utils.instantiate(cfg) with _convert_=all,
        # but faster: https://github.com/facebookresearch/hydra/issues/1200
        cfg = {k: instantiate(v) for k, v in cfg.items()}
        cls = cfg.pop(LAZY_TARGET)
        cls = migrate_target(cls)
        cls = instantiate(cls)

        if isinstance(cls, str):
            cls_name = cls
            cls = locate_object(cls_name)
            assert cls is not None, cls_name
        else:
            try:
                cls_name = cls.__module__ + "." + cls.__qualname__
            except Exception:  # noqa: B902, PIE786
                # target could be anything, so the above could fail
                cls_name = str(cls)
        if not callable(cls):
            msg = f"Non-callable object found: {LAZY_TARGET}={cls!r}!"
            raise TypeError(msg)

        cfg_args = cfg.pop(LAZY_ARGS, ())
        if not isinstance(cfg_args, typing.Sequence):
            msg = f"Expected sequence for {LAZY_ARGS}, but got {type(cfg_args)}!"
            raise TypeError(msg)

        try:
            return cls(*cfg_args, **cfg)
        except Exception as err:
            msg = (
                f"Error instantiating lazy object {cls_name}.\n\nConfig node:\n\t{cfg}!"
            )
            raise RuntimeError(msg) from err

    if isinstance(cfg, (dict, DictConfig)):
        return {k: instantiate(v) for k, v in cfg.items()}  # type: ignore

    if callable(cfg):
        return cfg

    err = f"Cannot instantiate {cfg}, type {type(cfg)}!"
    raise ValueError(err)
