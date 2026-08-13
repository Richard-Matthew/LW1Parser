import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule, FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from lw1parser import Config
from lw1parser.maps import CLASS_TYPES, MEDAL_MAP, PSI_RANK_MAP, expected_stat


class Export:
	"""
	Handles export of information to a spreadsheet file.
	"""
	@staticmethod
	def export_spreadsheet(format: str, save: "Save", save_path = None) -> None:  # type: ignore  # noqa: F821
		"""
		Writes save information to a file based on Config selected format.
		"""
		match format:
			case "CSV":
				Export.export_csv(save, save_path)
			case "EXCEL":
				Export.export_excel(save, save_path)

	@staticmethod
	def export_csv(save: "Save", save_path: Path = Path("unit_export.csv")) -> None:  # type: ignore  # noqa: F821
		"""
		Writes save information to a .csv file.
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
		Writes save information to an excel workbook with formatting.
		"""

		# Poor structural decisions means an additional safeguard
		if save_path is None:
			save_path = Path("unit_export.xlsx")

		wb = Workbook()

		# Barracks sheet
		barracks = wb.active
		barracks.title = "Barracks"

		headers = Export._write_barracks(barracks, save)
		Export._write_stat_deltas(barracks, headers)

		Export._apply_numeric_formatting(barracks, headers)
		Export._apply_class_formatting(barracks, headers)
		Export._apply_special_formatting(barracks, headers)

		Export._center_columns(barracks, headers)
		Export._resize_columns(barracks)
		
		# Campaign sheet
		campaign = wb.create_sheet("Campaign")
		Export._write_campaign(campaign, save)

		# Save workbook
		wb.save(save_path)

	def _write_barracks(sheet, save: "Save") -> list[str]:  # type: ignore # noqa: F821
		base_headers = list(save.units[0].to_dict_spreadsheet().keys())
		delta_headers = ["ΔHP", "ΔAim", "ΔMob", "ΔWill", "ΔDef", "ΔPts"]

		if Config.include_deltas:
			try:
				# Insert after SOML column
				soml_index = base_headers.index("SOML") + 1
			except ValueError:
				# If SOML column doesn't exist insert to the right
				soml_index = len(base_headers)

			headers = (
				base_headers[:soml_index] +
				delta_headers +
				base_headers[soml_index:]
			)
		else:
			headers = base_headers

		sheet.append(headers)

		# Insert unit information
		for unit in save.units:
			row = list(unit.to_dict_spreadsheet().values())

			if Config.include_deltas:
				row = (
					row[:soml_index] +
					[None] * len(delta_headers)
					+ row[soml_index:]
				)

			sheet.append(row)


		return headers

	def _apply_numeric_formatting(sheet, headers: list[str]) -> None:
		if not Config.do_numeric_formatting:
			return

		# Convert config names to column letters
		numeric_columns = Export._get_numeric_columns(headers)

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

		for class_type, class_list in CLASS_TYPES.items():
			bold = Config.bold_mec_classes and class_type == "MEC"

			for cls in class_list:
				cls_norm = cls.lower().replace("-", "_")

				Export._add_text_fill_rule(
					sheet, column_class,
					cls,
					PatternFill(start_color=getattr(Config, f"{cls_norm}_fill"), end_color=getattr(Config, f"{cls_norm}_fill"), fill_type="solid"),
					getattr(Config, f"{cls_norm}_text", None),
					bold
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
				cell_value = str(cell.value) if cell.value is not None else ""
				
				if cell_value:
					max_length = max(max_length, len(cell_value))

			# Slight padding
			adjusted_width = max_length + 2

			column_letter = get_column_letter(col_idx)
			sheet.column_dimensions[column_letter].width = adjusted_width

	def _center_columns(sheet, headers) -> None:
		numeric_columns = Export._get_numeric_columns(headers)

		# Apply center alignment
		for col in numeric_columns:
			for row in range(1, sheet.max_row + 1):
				cell = sheet[f"{col}{row}"]
				cell.alignment = Alignment(horizontal="center")

	def _write_stat_deltas(sheet, headers) -> None:
		if not Config.include_deltas:
			return

		header_to_column = {
			header: get_column_letter(idx + 1)
			for idx, header in enumerate(headers)
		}

		delta_map = {
			"ΔHP":   "HP",
			"ΔAim":  "Aim",
			"ΔMob":  "Mob",
			"ΔWill": "Will",
			"ΔDef":  "Def",
		}

		for delta_header, stat_header in delta_map.items():
			delta_col = header_to_column[delta_header]
			stat_col = header_to_column[stat_header]

			for row in range(2, sheet.max_row + 1):
				unit_class = sheet[f"{header_to_column['Class']}{row}"].value
				unit_rank = sheet[f"{header_to_column['Rank']}{row}"].value
				unit_stat = sheet[f"{stat_col}{row}"].value

				stat_delta = unit_stat - expected_stat(unit_class, stat_header, unit_rank)
				sheet[f"{delta_col}{row}"] = round(stat_delta, 2)

		for row in range(2, sheet.max_row + 1):
			pts = (
			sheet[f"{header_to_column['ΔHP']}{row}"].value * 3 +
			sheet[f"{header_to_column['ΔAim']}{row}"].value +
			sheet[f"{header_to_column['ΔMob']}{row}"].value * 4 +
			sheet[f"{header_to_column['ΔDef']}{row}"].value +
			sheet[f"{header_to_column['ΔWill']}{row}"].value
			)

			sheet[f"{header_to_column['ΔPts']}{row}"] = round(pts, 2)

	def _get_numeric_columns(headers):
		"""
		Returns an array of column letters for numeric columns.
		"""
		# Build header to column letter map
		header_to_column = {
			header: chr(ord("A") + idx)
			for idx, header in enumerate(headers)
		}

		# Convert config names to column letters
		numeric_columns = [
			header_to_column[name]
			for name in Config.numeric_columns
			if name in header_to_column
		]

		if Config.do_delta_formatting:
			delta_columns = [
				f"Δ{name}"
				for name in Config.numeric_columns
				if f"Δ{name}" in header_to_column
			]

			numeric_columns.extend(
				header_to_column[name]
				for name in delta_columns
			)

			numeric_columns.append(header_to_column["ΔPts"])

		return numeric_columns