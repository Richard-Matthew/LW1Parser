from dataclasses import dataclass, field

# https://docs.python.org/3/library/dataclasses.html
@dataclass
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

	soml_mission_count: int #eStat_CouncilMedalAccrued Stat[6] ?
	#unit_type: str # Bio, Psi, Officer, Mec, Shiv etc merge with unit.special?

	# Ordered perk dicts
	class_perks: dict[int, str] = field(default_factory=dict)
	officer_perks: dict[int, str] = field(default_factory=dict)
	psi_perks: dict[int, str] = field(default_factory=dict)
	gene_perks: dict[int, str] = field(default_factory=dict)
	bonus_perks: dict[int, str] = field(default_factory=dict)

	# Officer medals, linked to rank
	office_medals : list[int] = field(default_factory=list)

	# Misc spot
	special: str = ""

	# ID inside database for use with SQL, not initialized with the rest of Unit
	db_id: int | None = field(default=None, init=False)


	def to_dict_csv(self):
		class_perks_list   = _csv_list(list(self.class_perks.values()))
		officer_perks_list = _csv_list(list(self.officer_perks.values()))
		psi_perks_list     = _csv_list(list(self.psi_perks.values()))
		gene_mods_list     = _csv_list(list(self.gene_perks.values()))
		bonus_perks_list   = _csv_list(list(self.bonus_perks.values()))

		return {
			"ingame_id": self.ingame_id,

			"first_name": self.first_name,
			"last_name": self.last_name,
			"nick_name": self.nick_name,

			"ingame_class": self.ingame_class,

			"special": self.special,

			"rank": self.rank,
			"spec_rank": self.special_rank,

			#"xp": self.xp,
			#"psi_xp": self.psi_xp,

			#"kills": self.kills,

			"hp": self.hp,
			"aim": self.aim,
			"mobility": self.mobility,
			"willpower": self.willpower,
			"defense": self.defense,

			"SOML": self.soml_mission_count,

			"perks": class_perks_list,
			"psi_perks": psi_perks_list,
			"officer_perks": officer_perks_list,
			"gene_mods": gene_mods_list,
			"bonus_perks": bonus_perks_list,
			
			"kia_date": self.kia_date,
		}
	
	def to_dict(self):
		return {
			"ingame_id": self.ingame_id,
			"first_name": self.first_name,
			"nick_name": self.nick_name,
			"last_name": self.last_name,
			"ingame_class": self.ingame_class,
			"rank": self.rank,
			#"psi_rank": self.psi_rank,
			"xp": self.xp,
			"psi_xp": self.psi_xp,
			"kills": self.kills,
			"hp": self.hp,
			"aim": self.aim,
			"mobility": self.mobility,
			"willpower": self.willpower,
			"defense": self.defense,
			"class_perks": self.class_perks,
			"officer_perks": self.office_medals,
			"psi_perks": self.psi_perks,
			#"SOML": self.soml_mission_count,
			"kia_date": self.kia_date,
			"special": self.special,
		}


	def console_print(self):
		print(f"Name:        {self.first_name} '{self.nick_name}' {self.last_name}")
		print(f"ID:          {self.ingame_id}")
		print(f"Class:       {self.ingame_class}")
		print(f"Rank:        {self.rank}")
		#print(f"Psi Rank:    {self.psi_rank}")
		print(f"XP:          {self.xp}")
		print(f"Psi XP:      {self.psi_xp}")
		print(f"Kills:       {self.kills}")
		print(f"KIA Date:    {self.kia_date if self.kia_date else 'Alive'}")

		print("\nStats:")
		print(f"  HP:        {self.hp}")
		print(f"  Aim:       {self.aim}")
		print(f"  Mobility:  {self.mobility}")
		print(f"  Will:      {self.willpower}")
		print(f"  Defense:   {self.defense}")

		print("\nOfficer Perks (Medals):")
		if self.office_medals:
			print(f"  {self.office_medals}")
		else:
			print("  None")

		print("\nPerks:")
		if self.class_perks:
			for p in self.class_perks:
				print(f"  - {p}")
		else:
			print("  None")

		print(f"\nSpecial:     {self.special if self.special else 'None'}")
		print("-" * 40)

def _csv_list(values):
	return ", ".join(values) if values else ""
