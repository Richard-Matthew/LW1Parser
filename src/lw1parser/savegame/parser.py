from lw1parser.unit import Unit
from lw1parser.maps import *
from datetime import datetime

class _Parser:
	def __init__(self, data: dict):
		self.data = data

	def get_game_number(self):
		return self.data["header"].get("game_number", -1)

	def get_save_number(self):
		return self.data["header"].get("save_number", -1)

	def get_ironman(self):
		return self.data["header"].get("ironman", False)

	def get_tactical_save(self):
		return self.data["header"].get("tactical_save", True)

	def get_times(self):
		"""
		Returns ISO-formatted times as time_in_game, time_of_save, time_of_process.
		"""
		# Format of save_description:
		# 6/6/2026 - 14:11 - Game 19 - Geoscape - 6:38 am   March 10 2016
		# ^-time of save-^            ^-type--^   ^------ingame time----^
		raw = self.data["header"]["save_description"]["str"]
		parts = raw.split(" - ")

		# Save timestamp
		save_date = parts[0] # "6/6/2026"
		save_time = parts[1] # "14:11"

		save_raw = datetime.strptime(
			f"{save_date} {save_time}",
			"%m/%d/%Y %H:%M"
		)
		save_iso = save_raw.isoformat()

		# Game timestamp
		game_raw = parts[-1].strip()  # "6:38 am   March 10 2016"

		game_dt = datetime.strptime(
			game_raw,
			"%I:%M %p %B %d %Y"
		)
		game_iso = game_dt.isoformat()

		return game_iso, save_iso, datetime.now().isoformat()

	def get_units(self) -> list[Unit]:
		"""
		Returns a list of Unit dataclass from the loaded save.
		"""
		checkpoint_table = self.data["checkpoints"][0]["checkpoint_table"]
		units = []

		for entry in checkpoint_table:
			# Check name for match with soldier format, otherwise go to next item
			name = entry.get("name", "")
			if not name.startswith("Command1.TheWorld:PersistentLevel.XGStrategySoldier_"):
				continue

			# Convert nested mixed structured into nested dict
			unit_dict = self._properties_array_to_dict(entry.get("properties", []))

			# Extract m_kSoldier dict for convinience
			soldier_dict = unit_dict.get("m_kSoldier", {})

			# Get stats array from m_kChar properties.aStats int_values
			# A unit without stats means an issue with reading the save or save corruption
			stats = unit_dict.get("m_kChar", {}).get("aStats")
			if not stats:
				continue

			# Medal and perk arrays
			medals = unit_dict.get("m_arrMedals", [])
			perks = unit_dict.get("m_kChar", {}).get("aUpgrades", [])

			units.append(Unit(
				ingame_id     = soldier_dict.get("iID"),
				first_name    = soldier_dict.get("strFirstName", ""),
				last_name     = soldier_dict.get("strLastName", ""),
				nick_name     = soldier_dict.get("strNickName", ""),
				rank          = soldier_dict.get("iRank", 0),
				psi_rank      = soldier_dict.get("iPsiRank", 0),
				xp            = soldier_dict.get("iXP", 0),
				psi_xp        = soldier_dict.get("iPsiXP", 0),
				kills         = soldier_dict.get("iNumKills", 0),
				kia_date      = unit_dict.get("m_strKIADate", ""),

				officer_perks = self._parse_mapped_array(medals, MEDAL_MAP, False),
				perks         = self._parse_mapped_array(perks, UPGRADE_MAP, True),

				hp            = stats[0],
				aim           = stats[1],
				mobility      = stats[3],
				willpower     = stats[7],
				defense       = stats[2],
				ingame_class  = self._parse_class(unit_dict),
			))

		return units

	def _get_property(self, props, name, default_return = None):
		"""
		Like json.get() except it looks through a list of dictionaries.
		"""
		for prop in props:
			if prop.get("name") == name:
				return prop
		return default_return

	def _properties_array_to_dict(self, props):
		"""
		Converts nested array-of-dict into nested dicts.
		"""
		out = {}

		for prop in props:
			name = prop.get("name")
			if not name:
				continue

			# If this property contains its own nested properties array do a recusion
			if "properties" in prop and isinstance(prop["properties"], list):
				out[name] = self._properties_array_to_dict(prop["properties"])
				continue

			kind = prop.get("kind")

			# Simple types
			if kind == "StrProperty":
				out[name] = prop["value"]["str"]

			elif kind in ("IntProperty", "FloatProperty", "BoolProperty", "ByteProperty"):
				out[name] = prop["value"]

			# Arrays
			elif kind in ("StaticArrayProperty", "ArrayProperty"):
				out[name] = prop.get("int_values", prop.get("data"))

			# Otherwise store raw dict
			else:
				out[name] = prop

		return out

	def _parse_mapped_array(self, flags, mapping, skip_first: bool):
		"""
		Takes an array of dicts then returns a dict with id:name keys based on positional mapping.
		"""
		if not flags:
			return {}

		output = {}

		# Technically an integer array, and some values can be non-binary
		# Unpack index and value (usually a binary flag) just in case
		for index, flag in enumerate(flags):
			if index == 0 and skip_first:
				continue # First value is a placeholder "None" string
			if not flag:
				continue # Binary-ish array, 0 means abilities is not active

			output[index] = mapping.get(index, f"Unknown({index})")

		return output

	def _parse_class(self, unit_dict):
		"""
		Takes a normalized nested unit dict and returns a class string.
		"""
		kClass = unit_dict.get("m_kSoldier", {}).get("kClass", {})
		
		supra_class = kClass.get("eType", "")
		infra_class = kClass.get("strName", "")

		if infra_class == "":
			return CLASS_MAP.get(supra_class, supra_class)
		else:
			return infra_class
