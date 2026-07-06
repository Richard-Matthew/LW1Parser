import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.formatting.rule import FormulaRule, ColorScaleRule
from openpyxl.utils import get_column_letter

from lw1parser.maps import MEDAL_MAP, PSI_RANK_MAP
from lw1parser import Config

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
		if save_path is None:
			save_path = Path("unit_export.csv")

		with save_path.open("w", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=save.units[0].to_dict_spreadsheet().keys())
			writer.writeheader()

			for unit in save.units:
				writer.writerow(unit.to_dict_spreadsheet())

	@staticmethod
	def export_excel(save: "Save", save_path: Path = Path("unit_export.xlsx")) -> None:  # type: ignore  # noqa: F821
		"""
		Writes unit stats to a an excel workbook with formatting.
		"""

		# Poor structural decisions means an additional safeguard
		if save_path is None:
			save_path = Path("unit_export.xlsx")

		wb = Workbook()

		# Barracks sheet
		barracks = wb.active
		barracks.title = "Barracks"

		headers = Export._write_barracks(barracks, save)
		Export._apply_numeric_formatting(barracks, headers)
		Export._apply_class_formatting(barracks, headers)
		Export._apply_special_formatting(barracks, headers)
		Export._resize_columns(barracks)
		Export._center_columns(barracks, headers)

		# Campaign sheet
		campaign = wb.create_sheet("Campaign")
		Export._write_campaign(campaign, save)

		# Save workbook
		wb.save(save_path)

	def _write_barracks(sheet, save: "Save") -> list[str]:  # type: ignore # noqa: F821
		# Header row
		headers = list(save.units[0].to_dict_spreadsheet().keys())
		sheet.append(headers)

		# Insert unit information
		for unit in save.units:
			sheet.append(list(unit.to_dict_spreadsheet().values()))

		return headers

	def _apply_numeric_formatting(sheet, headers: list[str]) -> None:
		if not Config.do_numeric_formatting:
			return
		
		# Build header → column letter map
		header_to_column = {
			header: chr(ord("A") + idx)
			for idx, header in enumerate(headers)
		}

		# Convert config names → column letters
		numeric_columns = [
			header_to_column[name]
			for name in Config.numeric_columns
			if name in header_to_column
		]

		# Conditional formatting rule
		color_rule = ColorScaleRule(
			start_type="min", start_color=Config.min_fill,
			mid_type="percentile", mid_value=50, mid_color=Config.mid_fill,
			end_type="max", end_color=Config.max_fill,
		)

		# Apply formatting
		for col in numeric_columns:
			cell_range = f"{col}2:{col}{sheet.max_row}"
			sheet.conditional_formatting.add(cell_range, color_rule)

	def _apply_class_formatting(sheet, headers) -> None:
		if not Config.do_class_formatting:
			return
		
		# Find the column index
		try:
			special_idx = headers.index("Class")
		except ValueError:
			return
		
		column_class = chr(ord("A") + special_idx)

		# Generated with Copilot based on a template
		# Bio
		Export._add_text_fill_rule(
			sheet, column_class,
			"Rookie",
			PatternFill(start_color=Config.rookie_fill, end_color=Config.rookie_fill, fill_type="solid"),
			Config.rookie_text
		)

		# Scout/Sniper supraclass
		Export._add_text_fill_rule(
			sheet, column_class,
			"Scout-Sniper",
			PatternFill(start_color=Config.scout_sniper_fill, end_color=Config.scout_sniper_fill, fill_type="solid"),
			Config.scout_sniper_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Scout",
			PatternFill(start_color=Config.scout_fill, end_color=Config.scout_fill, fill_type="solid"),
			Config.scout_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Sniper",
			PatternFill(start_color=Config.sniper_fill, end_color=Config.sniper_fill, fill_type="solid"),
			Config.sniper_text
		)

		# Infantry/Assault supraclass
		Export._add_text_fill_rule(
			sheet, column_class,
			"Tactical",
			PatternFill(start_color=Config.tactical_fill, end_color=Config.tactical_fill, fill_type="solid"),
			Config.tactical_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Infantry",
			PatternFill(start_color=Config.infantry_fill, end_color=Config.infantry_fill, fill_type="solid"),
			Config.infantry_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Assault",
			PatternFill(start_color=Config.assault_fill, end_color=Config.assault_fill, fill_type="solid"),
			Config.assault_text
		)

		# Gunner/Rocketeer supraclass
		Export._add_text_fill_rule(
			sheet, column_class,
			"Weapons",
			PatternFill(start_color=Config.weapons_fill, end_color=Config.weapons_fill, fill_type="solid"),
			Config.weapons_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Gunner",
			PatternFill(start_color=Config.gunner_fill, end_color=Config.gunner_fill, fill_type="solid"),
			Config.gunner_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Rocketeer",
			PatternFill(start_color=Config.rocketeer_fill, end_color=Config.rocketeer_fill, fill_type="solid"),
			Config.rocketeer_text
		)

		# Support supraclass
		Export._add_text_fill_rule(
			sheet, column_class,
			"Support",
			PatternFill(start_color=Config.support_fill, end_color=Config.support_fill, fill_type="solid"),
			Config.support_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Medic",
			PatternFill(start_color=Config.medic_fill, end_color=Config.medic_fill, fill_type="solid"),
			Config.medic_text
		)

		Export._add_text_fill_rule(
			sheet, column_class,
			"Engineer",
			PatternFill(start_color=Config.engineer_fill, end_color=Config.engineer_fill, fill_type="solid"),
			Config.engineer_text
		)

		# Pathfinder
		Export._add_text_fill_rule(
			sheet, column_class,
			"Pathfinder",
			PatternFill(start_color=Config.pathfinder_fill, end_color=Config.pathfinder_fill, fill_type="solid"),
			Config.pathfinder_text,
			Config.bold_mec_classes
		)

		# Jaeger
		Export._add_text_fill_rule(
			sheet, column_class,
			"Jaeger",
			PatternFill(start_color=Config.jaeger_fill, end_color=Config.jaeger_fill, fill_type="solid"),
			Config.jaeger_text,
			Config.bold_mec_classes
		)

		# Valkyrie
		Export._add_text_fill_rule(
			sheet, column_class,
			"Valkyrie",
			PatternFill(start_color=Config.valkyrie_fill, end_color=Config.valkyrie_fill, fill_type="solid"),
			Config.valkyrie_text,
			Config.bold_mec_classes
		)

		# Marauder
		Export._add_text_fill_rule(
			sheet, column_class,
			"Marauder",
			PatternFill(start_color=Config.marauder_fill, end_color=Config.marauder_fill, fill_type="solid"),
			Config.marauder_text,
			Config.bold_mec_classes
		)

		# Goliath
		Export._add_text_fill_rule(
			sheet, column_class,
			"Goliath",
			PatternFill(start_color=Config.goliath_fill, end_color=Config.goliath_fill, fill_type="solid"),
			Config.goliath_text,
			Config.bold_mec_classes
		)

		# Archer
		Export._add_text_fill_rule(
			sheet, column_class,
			"Archer",
			PatternFill(start_color=Config.archer_fill, end_color=Config.archer_fill, fill_type="solid"),
			Config.archer_text,
			Config.bold_mec_classes
		)

		# Guardian
		Export._add_text_fill_rule(
			sheet, column_class,
			"Guardian",
			PatternFill(start_color=Config.guardian_fill, end_color=Config.guardian_fill, fill_type="solid"),
			Config.guardian_text,
			Config.bold_mec_classes
		)

		# Shogun
		Export._add_text_fill_rule(
			sheet, column_class,
			"Shogun",
			PatternFill(start_color=Config.shogun_fill, end_color=Config.shogun_fill, fill_type="solid"),
			Config.shogun_text,
			Config.bold_mec_classes
		)


	def _apply_special_formatting(sheet, headers) -> None:
		if not Config.do_special_formatting:
			return
		
		# Find the column index
		try:
			special_idx = headers.index("Special")
		except ValueError:
			return
		
		column_special = chr(ord("A") + special_idx)

		# Officer formatting
		officer_fill = PatternFill(start_color=Config.officer_fill, end_color=Config.officer_fill, fill_type="solid")
		Export._add_text_fill_rule(sheet, column_special, MEDAL_MAP.values(), officer_fill, Config.officer_text)

		# Psi formatting
		psi_fill = PatternFill(start_color=Config.psi_fill, end_color=Config.psi_fill, fill_type="solid")
		Export._add_text_fill_rule(sheet, column_special, PSI_RANK_MAP.values(), psi_fill, Config.psi_text)

		# MEC formatting
		mec_fill = PatternFill(start_color=Config.mec_fill, end_color=Config.mec_fill, fill_type="solid")
		Export._add_text_fill_rule(sheet, column_special, "MEC", mec_fill, Config.mec_text)

	def _write_campaign(sheet, save: "Save") -> None:  # type: ignore # noqa: F821
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

			elif value is None:
				value = "" # openpyxel doesn't like None values

			sheet.append([key, value])
	

	def _add_text_fill_rule(sheet, column_letter, values, fill="FFFFFF", text="000000", bold=False, start_row=2) -> None:
		"""
		Apply conditional formatting to a column so that any cell whose text matches one of values gets the specified PatternFill.
		"""
		if isinstance(values, str):
			values = [values]

		end_row = sheet.max_row
		cell_range = f"{column_letter}{start_row}:{column_letter}{end_row}"

		for v in values:
			formula = f'{column_letter}{start_row}="{v}"'
			rule = FormulaRule(
				formula=[formula],
				fill=fill,
				font=Font(color=text, bold=bold)
			)
			sheet.conditional_formatting.add(cell_range, rule)

	def _resize_columns(sheet) -> None:
		for col_idx, column_cells in enumerate(sheet.columns, start=1):
			max_length = 0

			for cell in column_cells:
				try:
					cell_value = str(cell.value)
				except Exception:
					cell_value = ""

				if cell_value:
					max_length = max(max_length, len(cell_value))

			# Slight padding
			adjusted_width = max_length + 2

			column_letter = get_column_letter(col_idx)
			sheet.column_dimensions[column_letter].width = adjusted_width

	def _center_columns(sheet, headers) -> None:
		# Build header → column letter map
		header_to_column = {
			header: get_column_letter(idx + 1)
			for idx, header in enumerate(headers)
		}

		# Convert config names → column letters
		numeric_columns = [
			header_to_column[name]
			for name in Config.numeric_columns
			if name in header_to_column
		]

		# Apply center alignment starting at row 2
		for col in numeric_columns:
			for row in range(2, sheet.max_row + 1):
				cell = sheet[f"{col}{row}"]
				cell.alignment = Alignment(horizontal="center")