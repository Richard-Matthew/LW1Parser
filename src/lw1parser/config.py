import configparser # https://docs.python.org/3/library/configparser.html
from pathlib import Path

class Config:
	"""
	Holds values reads from the configuration file for reference.
	"""
	# FILE PATHS
	game_path: Path = Path()
	save_path: Path = Path()

	# SETTINGS
	use_database: bool = False
	use_gui: bool = True
	keep_json: bool = False
	convert_opens_save_folder: bool = False
	spreadsheet_format: str = "CSV"

	# CONDITIONAL FORMATTING
	do_conditional_formatting: bool = True
	do_class_formatting: bool = True
	bold_mec_classes: bool = True


	# Bio classes
	rookie_fill: str = "00339A"
	rookie_text: str = "000000"

	# Scout/Sniper supraclass
	scout_sniper_fill: str = "FBD500"
	scout_sniper_text: str = "000000"

	scout_fill: str = "F9622D"
	scout_text: str = "000000"

	sniper_fill: str = "FBD500"
	sniper_text: str = "000000"

	# Infantry/Assault supraclass
	tactical_fill: str = "FA2D2D"
	tactical_text: str = "FFFFFF"

	infantry_fill: str = "5780F6"
	infantry_text: str = "000000"

	assault_fill: str = "FA2D2D"
	assault_text: str = "000000"

	# Gunner/Rocketeer supraclass
	weapons_fill: str = "5E8E1F"
	weapons_text: str = "000000"

	gunner_fill: str = "5E8E1F"
	gunner_text: str = "000000"

	rocketeer_fill: str = "BD107E"
	rocketeer_text: str = "000000"

	# Support supraclass
	support_fill: str = "1FAD9D"
	support_text: str = "000000"

	medic_fill: str = "F6F6F6"
	medic_text: str = "000000"

	engineer_fill: str = "1FAD9D"
	engineer_text: str = "000000"

	# MEC classes
	pathfinder_fill: str = "F9622D"
	pathfinder_text: str = "000000"

	jaeger_fill: str = "FBD500"
	jaeger_text: str = "000000"

	valkyrie_fill: str = "5780F6"
	valkyrie_text: str = "000000"

	marauder_fill: str = "FA2D2D"
	marauder_text: str = "000000"

	goliath_fill: str = "5E8E1F"
	goliath_text: str = "000000"

	archer_fill: str = "BD107E"
	archer_text: str = "000000"

	guardian_fill: str = "F6F6F6"
	guardian_text: str = "000000"

	shogun_fill: str = "1FAD9D"
	shogun_text: str = "000000"

	# Special column formatting
	do_special_formatting: bool = True

	psi_fill: str = "A09CD6"
	psi_text: str = "000000"

	officer_fill: str = "67E8ED"
	officer_text: str = "000000"

	mec_fill: str = "69747C"
	mec_text: str = "000000"

	# Numeric column color scales
	do_numeric_formatting: bool = True

	numeric_columns: list[str] = []
	min_fill: str = "F8696B"
	mid_fill: str = "FFEB84"
	max_fill: str = "63BE7B"

	@staticmethod
	def load_config(path='config.ini'):
		config_parser = configparser.ConfigParser()
		config_parser.read(path)

		# FILE PATHS / SETTINGS
		Config.game_path = Path(config_parser["FILE PATHS"]["strXcomFolder"])
		Config.save_path = Path(config_parser["FILE PATHS"]["strSaveFolder"])
		Config.use_database = config_parser.getboolean("SETTINGS", "bUseDatabase")
		Config.use_gui = config_parser.getboolean("SETTINGS", "bUseGUI")
		Config.keep_json = config_parser.getboolean("SETTINGS", "bKeepJSON")
		Config.convert_opens_save_folder = config_parser.getboolean("SETTINGS", "bConvertOpensSaveFolder")

		user_spreadsheet_format = config_parser.get("SETTINGS", "strSpreadsheetFormat").upper()
		if user_spreadsheet_format in ("EXCEL", "CSV"):
			Config.spreadsheet_format = user_spreadsheet_format

		# CONDITIONAL FORMATTING
		cf = config_parser["CONDITIONAL FORMATTING"]

		Config.do_conditional_formatting = cf.getboolean("bUseConditionalFormatting")
		Config.do_class_formatting = cf.getboolean("bUseClassFormatting")
		Config.bold_mec_classes = cf.getboolean("bBoldMECClasses")

		# Bio
		Config.rookie_fill = cf["strRookieFill"].upper()
		Config.rookie_text = cf["strRookieText"].upper()
		Config.scout_sniper_fill = cf["strScout-SniperFill"].upper()
		Config.scout_sniper_text = cf["strScout-SniperText"].upper()
		Config.scout_fill = cf["strScoutFill"].upper()
		Config.scout_text = cf["strScoutText"].upper()
		Config.sniper_fill = cf["strSniperFill"].upper()
		Config.sniper_text = cf["strSniperText"].upper()
		Config.tactical_fill = cf["strTacticalFill"].upper()
		Config.tactical_text = cf["strTacticalText"].upper()
		Config.infantry_fill = cf["strInfantryFill"].upper()
		Config.infantry_text = cf["strInfantryText"].upper()
		Config.assault_fill = cf["strAssaultFill"].upper()
		Config.assault_text = cf["strAssaultText"].upper()
		Config.weapons_fill = cf["strWeaponsFill"].upper()
		Config.weapons_text = cf["strWeaponsText"].upper()
		Config.gunner_fill = cf["strGunnerFill"].upper()
		Config.gunner_text = cf["strGunnerText"].upper()
		Config.rocketeer_fill = cf["strRocketeerFill"].upper()
		Config.rocketeer_text = cf["strRocketeerText"].upper()
		Config.support_fill = cf["strSupportFill"].upper()
		Config.support_text = cf["strSupportText"].upper()
		Config.medic_fill = cf["strMedicFill"].upper()
		Config.medic_text = cf["strMedicText"].upper()
		Config.engineer_fill = cf["strEngineerFill"].upper()
		Config.engineer_text = cf["strEngineerText"].upper()

		# MEC classes
		Config.pathfinder_fill = cf["strPathfinderFill"].upper()
		Config.pathfinder_text = cf["strPathfinderText"].upper()
		Config.jaeger_fill = cf["strJaegerFill"].upper()
		Config.jaeger_text = cf["strJaegerText"].upper()
		Config.valkyrie_fill = cf["strValkyrieFill"].upper()
		Config.valkyrie_text = cf["strValkyrieText"].upper()
		Config.marauder_fill = cf["strMarauderFill"].upper()
		Config.marauder_text = cf["strMarauderText"].upper()
		Config.goliath_fill = cf["strGoliathFill"].upper()
		Config.goliath_text = cf["strGoliathText"].upper()
		Config.archer_fill = cf["strArcherFill"].upper()
		Config.archer_text = cf["strArcherText"].upper()
		Config.guardian_fill = cf["strGuardianFill"].upper()
		Config.guardian_text = cf["strGuardianText"].upper()
		Config.shogun_fill = cf["strShogunFill"].upper()
		Config.shogun_text = cf["strShogunText"].upper()

		# Special formatting
		Config.do_special_formatting = cf.getboolean("bUseSpecialFormatting")
		Config.psi_fill = cf["strPsiFill"].upper()
		Config.psi_text = cf["strPsiText"].upper()
		Config.officer_fill = cf["strOfficerFill"].upper()
		Config.officer_text = cf["strOfficerText"].upper()
		Config.mec_fill = cf["strMECFill"].upper()
		Config.mec_text = cf["strMECText"].upper()

		# Numeric formatting
		Config.do_numeric_formatting = cf.getboolean("bUseNumericFormatting")

		# Split on ", "
		Config.numeric_columns = [s.strip() for s in cf["strNumericColums"].split(", ")]

		Config.min_fill = cf["strMinFill"].upper()
		Config.mid_fill = cf["strMidFill"].upper()
		Config.max_fill = cf["strMaxFill"].upper()
		
		 