from pathlib import Path

from openpyxl import Workbook

from ..formatting.classes import apply_class_formatting
from ..formatting.delta import write_stat_deltas
from ..formatting.layout import center_columns, resize_columns
from ..formatting.numeric import apply_numeric_formatting
from ..formatting.special import apply_special_formatting
from ..sheets.barracks import write_barracks
from ..sheets.campaign import write_campaign


def export_xlsx(save, save_path=None):
	save_path = save_path or Path("unit_export.xlsx")
	wb = Workbook()

	barracks = wb.active
	barracks.title = "Barracks"

	headers = write_barracks(barracks, save)
	write_stat_deltas(barracks, headers)

	apply_numeric_formatting(barracks, headers)
	apply_class_formatting(barracks, headers)
	apply_special_formatting(barracks, headers)

	center_columns(barracks, headers)
	resize_columns(barracks)

	campaign = wb.create_sheet("Campaign")
	write_campaign(campaign, save)

	wb.save(save_path)
