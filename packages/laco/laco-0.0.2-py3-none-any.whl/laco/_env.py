r"""
Working with environment variables.
"""

import enum
import functools
import os
import typing

from distutils.util import strtobool

__all__ = ["get_env", "EnvFilter"]

type EnvVarCompatible = int | str | bool


class EnvFilter(enum.StrEnum):
    STRING = enum.auto()
    TRUTHY = enum.auto()
    FALSY = enum.auto()
    POSITIVE = enum.auto()
    NEGATIVE = enum.auto()
    NONNEGATIVE = enum.auto()
    NONPOSITIVE = enum.auto()

    @staticmethod
    def apply(f: "EnvFilter | str", v: typing.Any, /) -> bool:
        if v is None:
            return False
        match EnvFilter(f):
            case EnvFilter.STRING:
                assert isinstance(v, str)
                v = v.lower()
                return v != ""
            case EnvFilter.TRUTHY:
                return bool(v)
            case EnvFilter.FALSY:
                return not bool(v)
            case EnvFilter.POSITIVE:
                return v > 0
            case EnvFilter.NEGATIVE:
                return v < 0
            case EnvFilter.NONNEGATIVE:
                return v >= 0
            case EnvFilter.NONPOSITIVE:
                return v <= 0
            case _:
                msg = f"Invalid filter: {f!r}"
                raise ValueError(msg)


@typing.overload
def get_env[_T: EnvVarCompatible](
    __type: type[_T],
    /,
    *keys: str,
    default: _T,
    filter: EnvFilter = EnvFilter.TRUTHY,
) -> _T: ...


@typing.overload
def get_env[_T: EnvVarCompatible](
    __type: type[_T],
    /,
    *keys: str,
    default: _T | None = None,
    filter: EnvFilter = EnvFilter.TRUTHY,
) -> _T | None: ...


@functools.cache
def get_env[_T: EnvVarCompatible](
    __type: type[_T],
    /,
    *keys: str,
    default: _T | None = None,
    filter: EnvFilter = EnvFilter.TRUTHY,
) -> _T | None:
    """
    Read an environment variable. If the variable is not set, return the default value.

    If no default is given, an error is raised if the variable is not set.
    """
    keys_read = []
    for k in keys:
        keys_read.append(k)
        v = os.getenv(k)
        if v is None:
            continue
        if __type is bool:
            v = bool(strtobool(v))
        else:
            v = __type(v)
        if not EnvFilter.apply(filter, v):
            continue
        break
    else:
        v = default
    return typing.cast(_T, v)
