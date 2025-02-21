from pathlib import Path
from types import ModuleType
from typing import Literal

Environment = Literal["local", "development", "test", "production"]

LOCAL: Environment = "local"
DEVELOPMENT: Environment = "development"
TEST: Environment = "test"
PRODUCTION: Environment = "production"

_ROOT: Path | None = None

def root(path: Path = Path(__file__)) -> Path:
    """
    Get the path of the directory where ".venv" is present.
    It discovers the root only once for the runtime, using a Singleton approach on module level.

    :param path: [Optional] an initial path to begin the search for the root.

    >>> issubclass(type(root()), Path)
    True
    >>> (root() / ".venv").exists()
    True
    """
    global _ROOT

    if not _ROOT:
        import glob

        if glob.glob(f"{path}/.venv") or glob.glob(f"{path}/main.py"):
            return path
        else:
            return root(path.parent.resolve())

    return _ROOT

def _load_module_from_path(path: Path) -> ModuleType:
    """
    Import a Python module into runtime.

    :param path: a path or string that represents a Python module.

    >>> _load_module_from_path(Path(""))
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: Module 'None' not found.
    """
    import importlib.util

    if not path or not path.exists():
        raise ModuleNotFoundError(f"There is no module at '{path.resolve()}'.")

    name = path.name.replace(".py", "")  # get the module name (filename without extension)
    module_spec = importlib.util.spec_from_file_location(name, path)  # get the module specification

    if module_spec:
        module_instance = importlib.util.module_from_spec(module_spec)

        if module_instance:
            module_spec.loader.exec_module(module_instance)
        else:
            raise ModuleNotFoundError(f"Module spec '{module_spec}' not found.")
    else:
        raise ModuleNotFoundError(f"Module '{module_spec}' not found.")

    return module_instance


def _load_package_from_path(path: Path) -> list[ModuleType]:
    """
    Manually load all Python modules inside a package.
    """
    return [_load_module_from_path(Path(module_path)) for module_path in path.glob("*.py")]


def load_module(module: str) -> ModuleType:
    return _load_module_from_path(Path(f"{root() / module.replace(".", "/")}.py"))

def load_modules(modules: list[str]) -> list[ModuleType]:
    return [load_module(module) for module in modules]
