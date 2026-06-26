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
	psi_rank: int
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

	# Perks, called upgrades before parsing
	perks: dict[int, str] = field(default_factory=dict)

	# Officer perks stored as medals
	officer_perks : list[int] = field(default_factory=list)

	# Misc spot
	special: str = ""

	# ID inside database for use with SQL, not initialized with the rest of Unit
	db_id: int | None = field(default=None, init=False)


	def to_dict(self):
		return {
			"ingame_id": self.ingame_id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"nick_name": self.nick_name,
			"ingame_class": self.ingame_class,
			"rank": self.rank,
			"psi_rank": self.psi_rank,
			"xp": self.xp,
			"psi_xp": self.psi_xp,
			"kills": self.kills,
			"hp": self.hp,
			"aim": self.aim,
			"mobility": self.mobility,
			"willpower": self.willpower,
			"defense": self.defense,
			"perks": self.perks,
			"officer_perks": self.officer_perks,
			"kia_date": self.kia_date,
			"special": self.special,
		}


	def console_print(self):
		print(f"Name:        {self.first_name} '{self.nick_name}' {self.last_name}")
		print(f"ID:          {self.ingame_id}")
		print(f"Class:       {self.ingame_class}")
		print(f"Rank:        {self.rank}")
		print(f"Psi Rank:    {self.psi_rank}")
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
		if self.officer_perks:
			print(f"  {self.officer_perks}")
		else:
			print("  None")

		print("\nPerks:")
		if self.perks:
			for p in self.perks:
				print(f"  - {p}")
		else:
			print("  None")

		print(f"\nSpecial:     {self.special if self.special else 'None'}")
		print("-" * 40)
