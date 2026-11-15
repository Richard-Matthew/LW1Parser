from .writers.csv_writer import export_csv
from .writers.xlsx_writer import export_xlsx


def export_spreadsheet(format: str, save: "Save", save_path=None): # type: ignore  # noqa: F821
	"""
	Writes save information to a file of the specified format.
	"""
	match format:
		case "CSV":
			export_csv(save, save_path)
		case "EXCEL":
			export_xlsx(save, save_path)
		case _:
			raise ValueError(f"Invalid file format: {format}")
