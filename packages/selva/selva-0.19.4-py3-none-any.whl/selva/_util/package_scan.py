import importlib
import inspect
import pkgutil
from collections.abc import Callable, Iterable
from types import ModuleType
from typing import Any


def _is_class_or_function(arg) -> bool:
    return inspect.isclass(arg) or inspect.isfunction(arg)


def _scan_members(module, predicate):
    for _name, member in inspect.getmembers(module, predicate):
        if member.__module__ == module.__name__:
            yield member


def scan_packages(
    *args: str | ModuleType,
    predicate: Callable[[Any], bool] = None,
) -> Iterable[type | Callable]:
    if predicate and not inspect.isfunction(predicate):
        raise TypeError("invalid predicate")

    for module in args:
        if isinstance(module, str):
            module = importlib.import_module(module)

        def scan_predicate(arg):
            predicate_result = predicate(arg) if predicate else True
            return _is_class_or_function(arg) and predicate_result

        yield from _scan_members(module, scan_predicate)

        spec = getattr(module, "__spec__", None)
        if not spec or not spec.submodule_search_locations:
            # module is not a package
            continue

        search_paths = spec.submodule_search_locations

        prefix = spec.name
        if prefix:
            prefix += "."

        for _module_finder, name, _ispkg in pkgutil.walk_packages(search_paths, prefix):
            submodule = importlib.import_module(name)
            yield from _scan_members(submodule, scan_predicate)
