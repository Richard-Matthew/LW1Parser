from openpyxl.utils import get_column_letter

from lw1parser import Config
from lw1parser.maps import expected_stat


def write_stat_deltas(sheet, headers) -> None:
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