from lw1parser import Config


def get_numeric_columns(headers) -> list[str]:
	"""
	Returns list of column letters corresponding to numeric columns.
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