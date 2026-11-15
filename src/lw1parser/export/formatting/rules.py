from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Font


def add_text_fill_rule(sheet, column_letter, values, fill="FFFFFF", text="000000", bold=False, start_row=2) -> None:
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