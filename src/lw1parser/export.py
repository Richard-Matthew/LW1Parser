import csv
from openpyxl import Workbook
from pathlib import Path

class Export():
	@staticmethod
	def export_spreadsheet(format: str, save: "Save", save_path = None) -> None:  # type: ignore  # noqa: F821
		match format:
			case "CSV":
				Export.export_csv(save, save_path)
			case "EXCEL":
				Export.export_excel(save, save_path)

	@staticmethod
	def export_csv(save: "Save", save_path: Path = Path("unit_export.csv")) -> None:  # type: ignore  # noqa: F821
		"""
		Writes unit stats to a .csv file.
		"""
		with save_path.open("w", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=save.units[0].to_dict_csv().keys())
			writer.writeheader()

			for unit in save.units:
				writer.writerow(unit.to_dict_csv())

	@staticmethod
	def export_excel(save: "Save", save_path: Path = Path("unit_export.xlsx")) -> None:  # type: ignore  # noqa: F821
		"""
		Writes unit stats to a an excel workbook with formatting.
		"""
		wb = Workbook()

		# Barracks sheet
		barracks = wb.active
		barracks.title = "Barracks"

		# Header row
		headers = list(save.units[0].to_dict_csv().keys())
		barracks.append(headers)

		# Insert unit information
		for unit in save.units:
			barracks.append(list(unit.to_dict_csv().values()))

		# Campaign sheet
		campaign = wb.create_sheet("Campaign")

		# Simple key/value layout
		campaign_data = {
			"Game Time": save.game_time,
			"Save Time": save.save_time,
			"Current Time": save.current_time,
			"Game Number": save.game_number,
			"Save Number": save.save_number,
			"Ironman": save.ironman,
			"Tactical Save": save.tactical_save,
			"Foundry": save.foundry,
			"Research": save.research,
		}


		for key, value in campaign_data.items():
			if isinstance(value, dict):
				value = ", ".join(f"{v}" for k, v in value.items())

			elif isinstance(value, list):
				value = ", ".join(str(v) for v in value)

			campaign.append([key, value])


		# Save workbook
		wb.save(save_path)