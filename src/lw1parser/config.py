import configparser # https://docs.python.org/3/library/configparser.html
from pathlib import Path

class Config:
	"""
	Holds values reads from the configuration file for reference
	"""
	game_path: Path = Path()
	save_path: Path = Path()
	use_database: bool = False
	use_gui: bool = True
	keep_json: bool = False
	convert_opens_save_folder: bool = False

	@staticmethod
	def load_config(path = 'config.ini'):
		parser = configparser.ConfigParser()
		parser.read(path)

		Config.game_path = Path(parser["FILE PATHS"]["strXcomFolder"])
		Config.save_path = Path(parser["FILE PATHS"]["strSaveFolder"])
		Config.use_database = parser.getboolean("SETTINGS", "bUseDatabase")
		Config.use_gui = parser.getboolean("SETTINGS", "bUseGUI")
		Config.keep_json = parser.getboolean("SETTINGS", "bKeepJSON")
		Config.convert_opens_save_folder = parser.getboolean("SETTINGS", "bConvertOpensSaveFolder")