import sys
import tomllib
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
	include_deltas: bool = True

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

	numeric_columns: list[str]
	min_fill: str = "F8696B"
	mid_fill: str = "FFEB84"
	max_fill: str = "63BE7B"

	do_delta_formatting: bool = True

	# Stat progression stuff
	lw_version: str = "LW1"
	stat_progression: dict

	@staticmethod
	def load_config(path='config.toml'):
		if getattr(sys, "frozen", False):
			# Running inside PyInstaller EXE
			base_dir = Path(sys.executable).parent
		else:
			# Running from source: config.ini lives next to launcher.py
			base_dir = Path(__file__).resolve().parents[2]

		config_path = base_dir / path

		with open(config_path, "rb") as file:
			data = tomllib.load(file)

		# TOML sections
		file_paths = data["FILE_PATHS"]
		settings = data["SETTINGS"]
		conditional_formatting = data["CONDITIONAL_FORMATTING"]
		stat_progression = data["STAT_PROGRESSION"]

		# FILE PATHS / SETTINGS
		Config.game_path 					= Path(file_paths["strXcomFolder"])
		Config.save_path 					= Path(file_paths["strSaveFolder"])
		Config.use_database 				= settings["bUseDatabase"]
		Config.use_gui 						= settings["bUseGUI"]
		Config.keep_json 					= settings["bKeepJSON"]
		Config.convert_opens_save_folder 	= settings["bConvertOpensSaveFolder"]

		format = settings["strSpreadsheetFormat"].upper()
		if format in ("EXCEL", "CSV"):
			Config.spreadsheet_format = format

		Config.include_deltas = settings["bIncludeStatDeltas"]
		
		# CONDITIONAL FORMATTING
		Config.do_conditional_formatting = conditional_formatting["bUseConditionalFormatting"]
		Config.do_class_formatting = conditional_formatting["bUseClassFormatting"]
		Config.bold_mec_classes = conditional_formatting["bBoldMECClasses"]

        # Bio
		Config.rookie_fill = conditional_formatting["strRookieFill"].upper()
		Config.rookie_text = conditional_formatting["strRookieText"].upper()
		Config.scout_sniper_fill = conditional_formatting["strScout-SniperFill"].upper()
		Config.scout_sniper_text = conditional_formatting["strScout-SniperText"].upper()
		Config.scout_fill = conditional_formatting["strScoutFill"].upper()
		Config.scout_text = conditional_formatting["strScoutText"].upper()
		Config.sniper_fill = conditional_formatting["strSniperFill"].upper()
		Config.sniper_text = conditional_formatting["strSniperText"].upper()
		Config.tactical_fill = conditional_formatting["strTacticalFill"].upper()
		Config.tactical_text = conditional_formatting["strTacticalText"].upper()
		Config.infantry_fill = conditional_formatting["strInfantryFill"].upper()
		Config.infantry_text = conditional_formatting["strInfantryText"].upper()
		Config.assault_fill = conditional_formatting["strAssaultFill"].upper()
		Config.assault_text = conditional_formatting["strAssaultText"].upper()
		Config.weapons_fill = conditional_formatting["strWeaponsFill"].upper()
		Config.weapons_text = conditional_formatting["strWeaponsText"].upper()
		Config.gunner_fill = conditional_formatting["strGunnerFill"].upper()
		Config.gunner_text = conditional_formatting["strGunnerText"].upper()
		Config.rocketeer_fill = conditional_formatting["strRocketeerFill"].upper()
		Config.rocketeer_text = conditional_formatting["strRocketeerText"].upper()
		Config.support_fill = conditional_formatting["strSupportFill"].upper()
		Config.support_text = conditional_formatting["strSupportText"].upper()
		Config.medic_fill = conditional_formatting["strMedicFill"].upper()
		Config.medic_text = conditional_formatting["strMedicText"].upper()
		Config.engineer_fill = conditional_formatting["strEngineerFill"].upper()
		Config.engineer_text = conditional_formatting["strEngineerText"].upper()

		# MEC classes
		Config.pathfinder_fill = conditional_formatting["strPathfinderFill"].upper()
		Config.pathfinder_text = conditional_formatting["strPathfinderText"].upper()
		Config.jaeger_fill = conditional_formatting["strJaegerFill"].upper()
		Config.jaeger_text = conditional_formatting["strJaegerText"].upper()
		Config.valkyrie_fill = conditional_formatting["strValkyrieFill"].upper()
		Config.valkyrie_text = conditional_formatting["strValkyrieText"].upper()
		Config.marauder_fill = conditional_formatting["strMarauderFill"].upper()
		Config.marauder_text = conditional_formatting["strMarauderText"].upper()
		Config.goliath_fill = conditional_formatting["strGoliathFill"].upper()
		Config.goliath_text = conditional_formatting["strGoliathText"].upper()
		Config.archer_fill = conditional_formatting["strArcherFill"].upper()
		Config.archer_text = conditional_formatting["strArcherText"].upper()
		Config.guardian_fill = conditional_formatting["strGuardianFill"].upper()
		Config.guardian_text = conditional_formatting["strGuardianText"].upper()
		Config.shogun_fill = conditional_formatting["strShogunFill"].upper()
		Config.shogun_text = conditional_formatting["strShogunText"].upper()

        # Special formatting
		Config.do_special_formatting = conditional_formatting["bUseSpecialFormatting"]
		Config.psi_fill = conditional_formatting["strPsiFill"].upper()
		Config.psi_text = conditional_formatting["strPsiText"].upper()
		Config.officer_fill = conditional_formatting["strOfficerFill"].upper()
		Config.officer_text = conditional_formatting["strOfficerText"].upper()
		Config.mec_fill = conditional_formatting["strMECFill"].upper()
		Config.mec_text = conditional_formatting["strMECText"].upper()

		# Numeric formatting
		Config.do_numeric_formatting = conditional_formatting["bUseNumericFormatting"]
		Config.numeric_columns = conditional_formatting["strNumericColumns"]
		Config.min_fill = conditional_formatting["strMinFill"].upper()
		Config.mid_fill = conditional_formatting["strMidFill"].upper()
		Config.max_fill = conditional_formatting["strMaxFill"].upper()

		# Delta formatting
		Config.do_delta_formatting = conditional_formatting["bFormatDeltaColumns"]

		# Stat progression stuff
		valid_versions = ["LW1"]
		Config.lw_version = stat_progression["strLongWarVersion"]
		if Config.lw_version not in valid_versions:
			Config.lw_version = "LW1"

		Config.stat_progression = {
			key:value
			for key, value in stat_progression[Config.lw_version].items()
		}
		
		 