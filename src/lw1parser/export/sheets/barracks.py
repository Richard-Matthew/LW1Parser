from lw1parser import Config


def write_barracks(sheet, save) -> list[str]:
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
				[None] * len(delta_headers) +
				row[soml_index:]
			)

		sheet.append(row)

	return headers