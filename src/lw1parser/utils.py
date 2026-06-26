from pathlib import Path
import csv
import sys

from lw1parser import *
from lw1parser.savegame.converter import _Converter
from lw1parser.savegame.parser import _Parser

def path_to_csv(save_path: Path, export_path: Path):
	converter = _Converter()

	data = converter.convert(save_path)
	parser = _Parser(data)

	# Check save type
	if parser.get_tactical_save():
		raise TypeError("Tactical saves are not supported")

	# Information from save
	units = parser.get_units()

	with export_path.open("w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=units[0].to_dict().keys())
		writer.writeheader()

		for unit in units:
			writer.writerow(unit.to_dict())

def resource_path(relative: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "lw1parser" / "resources" / relative
    return Path(__file__).resolve().parent / "resources" / relative