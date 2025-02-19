r"""
Utils
-----

General utilities.
"""

import importlib
import pydoc
import types
import typing


def generate_path(obj: typing.Any) -> str:
    """
    Inverse of ``locate()``. Generates the fully qualified name of an object.
    Handles cases where the object is not directly importable, e.g. due to
    nested classes or private modules.

    The generated path is simplified by removing redundant module parts, e.g.
    ``module.submodule._impl.class`` may become ``module.submodule.class`` if
    the later also resolves to the same object.

    Bound methods are supported by inspecting the ``__self__`` attribute.

    Parameters
    ----------
    obj
        The object to generate the path for.

    Returns
    -------
    str
        The fully qualified name of the object.
    """

    def __check(path: str, obj: typing.Any) -> bool:
        # Check if the path resolves to the same object
        try:
            check_ok = locate_object(path) is obj
        except ImportError:
            check_ok = False
        return check_ok

    try:
        self = obj.__self__
    except AttributeError:
        self = None

    if self is not None:
        self_path = generate_path(self)
        return f"{self_path}.{obj.__name__}"

    module, qualname = obj.__module__, obj.__qualname__

    # Compress the path to this object, e.g. ``module.submodule._impl.class``
    # may become ``module.submodule.class``, if the later also resolves to the same
    # object. This simplifies the string, and also is less affected by moving the
    # class implementation.
    module_parts = module.split(".")
    for k in range(1, len(module_parts)):
        prefix = ".".join(module_parts[:k])
        path = f"{prefix}.{qualname}"
        if __check(path, obj):
            return path

    # Default to the full path plus qualname
    path = f"{module}.{qualname}"
    if not __check(path, obj):
        msg = f"Cannot generate path for object {obj}!"
        raise ImportError(msg)

    return path


def locate_object(path: str) -> typing.Any:
    """
    Dynamically locates and returns an object by its fully qualified name.

    Parameters
    ----------
    name (str):
        The fully qualified name of the object to locate.

    Returns
    -------
    Any:
        The located object.

    Raises
    ------
    ImportError
        If the object cannot be located.
    """

    obj = pydoc.locate(path)

    # Some cases (e.g. torch.optim.sgd.SGD) not handled correctly
    # by pydoc.locate. Try a private function from hydra.
    if obj is None:
        try:
            from hydra.utils import _locate
        except ImportError as e:
            raise ImportError(f"Cannot dynamically locate object {path}!") from e
        else:
            obj = _locate(path)  # it raises if fails
    if path == "":
        raise ImportError("Empty path")
    parts = [part for part in path.split(".")]
    for part in parts:
        if not len(part):
            raise ValueError(
                f"Error loading '{path}': invalid dotstring."
                + "\nRelative imports are not supported."
            )
    assert len(parts) > 0
    part0 = parts[0]
    try:
        obj = importlib.import_module(part0)
    except Exception as exc_import:
        raise ImportError(
            f"Error loading '{path}':\n{repr(exc_import)}"
            + f"\nAre you sure that module '{part0}' is installed?"
        ) from exc_import
    for m in range(1, len(parts)):
        part = parts[m]
        try:
            obj = getattr(obj, part)
        except AttributeError as exc_attr:
            parent_dotpath = ".".join(parts[:m])
            if isinstance(obj, types.ModuleType):
                mod = ".".join(parts[: m + 1])
                try:
                    obj = importlib.import_module(mod)
                    continue
                except ModuleNotFoundError as exc_import:
                    raise ImportError(
                        f"Error loading '{path}':\n{repr(exc_import)}"
                        + f"\nAre you sure that '{part}' is importable from module '{parent_dotpath}'?"
                    ) from exc_import
                except Exception as exc_import:
                    raise ImportError(
                        f"Error loading '{path}':\n{repr(exc_import)}"
                    ) from exc_import
            raise ImportError(
                f"Error loading '{path}':\n{repr(exc_attr)}"
                + f"\nAre you sure that '{part}' is an attribute of '{parent_dotpath}'?"
            ) from exc_attr
    return obj
