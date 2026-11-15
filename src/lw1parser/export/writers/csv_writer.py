import csv
from pathlib import Path


def export_csv(save, save_path=None):
	if save_path is None:
		save_path = Path("unit_export.csv")

	with save_path.open("w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=save.units[0].to_dict_spreadsheet().keys())
		writer.writeheader()

		for unit in save.units:
			writer.writerow(unit.to_dict_spreadsheet())