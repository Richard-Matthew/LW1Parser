from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("lw1parser")
except PackageNotFoundError:
    # When running from source without installation
    __version__ = "0.0.0"

__author__ = "Richard Matthew"


from .config import Config
from .gui import GUI, run_gui
from .savegame import Save
from .update import Update
from .utils import path_to_csv

__all__ = [
    "Config",
    "GUI",
    "run_gui",
    "Save",
    "Update",
    "path_to_csv",
    "__version__",
    "__author__",
]