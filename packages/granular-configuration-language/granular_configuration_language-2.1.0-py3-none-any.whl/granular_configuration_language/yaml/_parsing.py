from __future__ import annotations

import collections.abc as tabc
import sys
import typing as typ
from pathlib import Path

from granular_configuration_language.exceptions import ParsingTriedToCreateALoop
from granular_configuration_language.yaml.classes import LoadOptions

if sys.version_info >= (3, 12):

    def walkup(file: Path, relative_to: Path) -> Path:
        return file.relative_to(relative_to, walk_up=True)

else:
    import os

    def _get_segments(path: os.PathLike) -> tabc.Iterator[str]:
        head, tail = os.path.split(path)
        if tail:
            yield from _get_segments(head)
            yield tail
        else:
            yield head

    def get_segments(path: os.PathLike) -> list[str]:
        return list(_get_segments(path))

    def walkup(file: Path, relative_to: Path) -> Path:
        # Modified from the 3.12 pathlib.PurePath.relative_to implementation

        for step, path in enumerate([relative_to] + list(relative_to.parents)):
            if file.is_relative_to(path):
                break
            elif path.name == "..":
                raise ValueError(f"'..' segment in {str(relative_to)!r} cannot be walked")
        else:
            raise ValueError(f"{str(file)!r} and {str(relative_to)!r} have different anchors")
        parts = [".."] * step + get_segments(file)[len(get_segments(path)) :]
        return Path(*parts)


FILE_EXTENSION: typ.Final = ".environment_variable-a5b55071-b86e-4f22-90fc-c9db335691f6"


def _get_chain_reversed(options: LoadOptions) -> tabc.Iterator[str]:
    relative_to = Path().resolve()
    seen: set[str] = set()

    if options.previous:
        yield from _get_chain_reversed(options.previous)

    if not options.file_location:
        pass
    elif options.file_location.suffix == FILE_EXTENSION:
        yield "$" + options.file_location.stem
    elif options.file_location.name not in seen:
        seen.add(options.file_location.name)
        yield options.file_location.name
    else:
        try:
            yield str(walkup(options.file_location, relative_to))
        except ValueError:
            yield "?/" + options.file_location.name


def is_in_chain(file: Path, options: LoadOptions) -> bool:
    # Note *.environment_variable don't exist, so .resolve() and .samefile() fail

    if (
        options.file_location
        and (file.name == options.file_location.name)
        and (file == options.file_location or file.samefile(options.file_location))
    ):
        return True
    elif options.previous:
        return is_in_chain(file, options.previous)
    else:
        return False


def make_chain_message(tag: str, value: str, options: LoadOptions) -> ParsingTriedToCreateALoop:
    return ParsingTriedToCreateALoop(
        f"`{tag} {value}` tried to load itself in chain: ({'→'.join(_get_chain_reversed(options))}→...)"
    )


def create_environment_variable_path(env_var: str) -> Path:
    return Path(env_var + FILE_EXTENSION)
