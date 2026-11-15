from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter

from ..utils.columns import get_numeric_columns


def resize_columns(sheet) -> None:
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

def center_columns(sheet, headers) -> None:
	numeric_columns = get_numeric_columns(headers)

	# Apply center alignment
	for col in numeric_columns:
		for row in range(1, sheet.max_row + 1):
			cell = sheet[f"{col}{row}"]
			cell.alignment = Alignment(horizontal="center")