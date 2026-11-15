from openpyxl.formatting.rule import ColorScaleRule

from lw1parser import Config

from ..utils.columns import get_numeric_columns


def apply_numeric_formatting(sheet, headers: list[str]) -> None:
	if not Config.do_numeric_formatting:
		return

	# Convert config names to column letters
	numeric_columns = get_numeric_columns(headers)

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