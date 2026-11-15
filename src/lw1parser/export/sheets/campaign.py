def write_campaign(sheet, save) -> None:
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