from dataclasses import dataclass


@dataclass  # https://docs.python.org/3/library/dataclasses.html
class Save:
	"""
	Data class that holds save information.
	"""

	units: list["Unit"]  # type: ignore # noqa: F821
	game_time: str
	save_time: str
	current_time: str
	game_number: int
	save_number: int
	ironman: bool
	tactical_save: bool

	foundry: dict[int, str]
	research: dict[int, str]
