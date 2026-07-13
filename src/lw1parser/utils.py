from pathlib import Path
import sys

from lw1parser.savegame import Savegame
from lw1parser.export import Export

def path_to_csv(format: str, save_path: Path, export_path: Path) -> Path:
    save = Savegame.load(save_path)

    Export.export_spreadsheet(format, save, export_path)

    return export_path

def resource_path(relative: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "lw1parser" / "resources" / relative
    return Path(__file__).resolve().parent / "resources" / relative