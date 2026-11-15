from importlib.metadata import PackageNotFoundError, version

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
	"GUI",
	"Config",
	"Save",
	"Update",
	"__author__",
	"__version__",
	"path_to_csv",
	"run_gui",
]