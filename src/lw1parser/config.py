import configparser # https://docs.python.org/3/library/configparser.html
from pathlib import Path

class Config:
	"""
	Holds values reads from the configuration file for reference.
	"""
	game_path: Path = Path()
	save_path: Path = Path()
	use_database: bool = False
	use_gui: bool = True
	keep_json: bool = False
	convert_opens_save_folder: bool = False
	spreadsheet_format: str = "CSV"

	@staticmethod
	def load_config(path = 'config.ini'):
		config_parser = configparser.ConfigParser()
		config_parser.read(path)

		Config.game_path = Path(config_parser["FILE PATHS"]["strXcomFolder"])
		Config.save_path = Path(config_parser["FILE PATHS"]["strSaveFolder"])
		Config.use_database = config_parser.getboolean("SETTINGS", "bUseDatabase")
		Config.use_gui = config_parser.getboolean("SETTINGS", "bUseGUI")
		Config.keep_json = config_parser.getboolean("SETTINGS", "bKeepJSON")
		Config.convert_opens_save_folder = config_parser.getboolean("SETTINGS", "bConvertOpensSaveFolder")

		user_spreadsheet_format = config_parser.get("SETTINGS", "strSpreadsheetFormat").upper()
		if user_spreadsheet_format in ("EXCEL", "CSV"):
			Config.spreadsheet_format = user_spreadsheet_format
		
		 