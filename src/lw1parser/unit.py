from dataclasses import dataclass, field


@dataclass  # https://docs.python.org/3/library/dataclasses.html
class Unit:
	"""
	Data class that holds unit information.
	"""
	# Identification
	ingame_id: int
	first_name: str
	last_name: str
	nick_name: str

	# Status
	ingame_class: str
	rank: int
	special_rank: int
	xp: int
	psi_xp: int
	kills: int
	kia_date: str

	# Stats
	hp: int
	aim: int
	mobility: int
	willpower: int
	defense: int

	soml_mission_count: int  # eStat_CouncilMedalAccrued Stat[6]

	# Ordered perk dicts
	class_perks: dict[int, str] = field(default_factory=dict)
	officer_perks: dict[int, str] = field(default_factory=dict)
	psi_perks: dict[int, str] = field(default_factory=dict)
	gene_perks: dict[int, str] = field(default_factory=dict)
	bonus_perks: dict[int, str] = field(default_factory=dict)

	# MEC, Officer, or Psion
	special: str = ""

	# ID inside database for use with SQL, not initialized with the rest of Unit
	db_id: int | None = field(default=None, init=False)


	def to_dict_spreadsheet(self) -> dict:
		"""
		Returns a dict formatted for human usage via spreadsheet.
		"""
		class_perks_list   = _csv_list(list(self.class_perks.values()))
		officer_perks_list = _csv_list(list(self.officer_perks.values()))
		psi_perks_list     = _csv_list(list(self.psi_perks.values()))
		gene_mods_list     = _csv_list(list(self.gene_perks.values()))
		bonus_perks_list   = _csv_list(list(self.bonus_perks.values()))

		if self.nick_name == "":
			name = self.first_name + " " + self.last_name
		else:
			name = self.first_name + " '" + self.nick_name + "' " + self.last_name

		return {
			#"ID": self.ingame_id,

			#"first_name": self.first_name,
			#"last_name": self.last_name,
			#"nick_name": self.nick_name,
			"Name": name,

			"Class": self.ingame_class,

			"Special": self.special,

			"Rank": self.rank,
			"Spec": self.special_rank,

			#"xp": self.xp,
			#"psi_xp": self.psi_xp,

			#"kills": self.kills,

			"HP": self.hp,
			"Aim": self.aim,
			"Mob": self.mobility,
			"Will": self.willpower,
			"Def": self.defense,

			"SOML": self.soml_mission_count,

			"Class Perks": class_perks_list,
			"Psi Perks": psi_perks_list,
			"Officer Perks": officer_perks_list,
			"Gene Mods": gene_mods_list,
			"Bonus Perks": bonus_perks_list,
			
			"KIA Date": self.kia_date,
		}
	
	def to_dict(self) -> dict:
		"""
		Returns a serialized form of the object.
		"""
		return {
			# Identification
			"ingame_id": self.ingame_id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"nick_name": self.nick_name,

			# Status
			"ingame_class": self.ingame_class,
			"rank": self.rank,
			"special_rank": self.special_rank,
			"xp": self.xp,
			"psi_xp": self.psi_xp,
			"kills": self.kills,
			"kia_date": self.kia_date,

			#Stats
			"hp": self.hp,
			"aim": self.aim,
			"mobility": self.mobility,
			"willpower": self.willpower,
			"defense": self.defense,

			"soml_mission_count": self.soml_mission_count,

			#Ordered perk dicts
			"class_perks": self.class_perks,
			"officer_perks": self.office_medals,
			"psi_perks": self.psi_perks,
			"gene_perks": self.gene_perks,
			"bonus_perks": self.bonus_perks,
			
			# MEC, Officer, or Psion
			"special": self.special,
		}
		
def _csv_list(values):
	return ", ".join(values) if values else ""
