from datetime import datetime

from .tech import _Tech
from .units import _UnitParser


class Parser:
	def __init__(self, data: dict):
		self.data = data

	def get_game_number(self) -> int:
		return self.data["header"].get("game_number", -1)

	def get_save_number(self) -> int:
		return self.data["header"].get("save_number", -1)

	def get_ironman(self) -> bool:
		return self.data["header"].get("ironman", False)

	def get_tactical_save(self) -> bool:
		return self.data["header"].get("tactical_save", True)

	def get_times(self) -> tuple[str, str, str]:
		"""
		Returns ISO-formatted times as time_in_game, time_of_save, time_of_process.
		"""
		# Format of save_description:
		# 6/6/2026 - 14:11 - Game 19 - Geoscape - 6:38 am   March 10 2016
		# ^-time of save-^            ^-type--^   ^------ingame time----^
		raw = self.data["header"]["save_description"]["str"]
		parts = raw.split(" - ")

		# Save timestamp
		save_date = parts[0]
		save_time = parts[1]

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

		current_iso = datetime.now().isoformat()

		return game_iso, save_iso, current_iso

	def get_units(self) -> list["Unit"]:  # type: ignore # noqa: F821
		"""
		Returns a list of Unit dataclass from the loaded save.
		"""
		checkpoint_table = self.data["checkpoints"][0]["checkpoint_table"]
		return _UnitParser.build_units(checkpoint_table)

	def get_foundry(self) -> dict:
		return _Tech.get_foundry(self.data["checkpoints"][0]["checkpoint_table"])
	
	def get_research(self) -> dict:
		return _Tech.get_research(self.data["checkpoints"][0]["checkpoint_table"])