from lw1parser.config import Config
from .save import Save
from .parser import Parser
from .converter import _Converter

from pathlib import Path
import re

class Loader:
	"""
	Handles loading information from a game save into a Save class. Exposed to the main module as Savegame.
	"""
	def load(path: Path | None = None) -> Save:
		"""
		Takes a path and calls various Parser methods to create a Save dataclass for return.
		"""
		converter = _Converter()

		if path:
			data = converter.convert(path)
		else:
			path = Loader._find_latest(Config.save_path)
			data = converter.convert(path)

		parser = Parser(data)

		# Dear future self:
		# If you really, really need to parse a tactical save it mostly works
		# But they aren't supported by xcom2json and random errors sometimes happen

		# Check save type
		if parser.get_tactical_save():
			raise TypeError("Tactical saves are not supported")

		save = Loader._parse_save(parser)

		# Clean up JSON per Config setting
		Loader._cleanup(converter)

		return save

	def _find_latest(save_dir: Path) -> Path:
		if not save_dir.exists():
			raise FileNotFoundError(f"Save directory not found: {save_dir}")

		save_files = [
			f for f in save_dir.iterdir()
			if f.is_file() and re.fullmatch(r"save(\d+)", f.name)
		]

		if not save_files:
			raise FileNotFoundError(f"No XCOM save files found in {save_dir}")

		save_files.sort(key=lambda f: f.stat().st_mtime)
		return save_files[-1]
	
	def _parse_save(parser: Parser) -> Save:
		times = parser.get_times()
		return Save(
			units 			= parser.get_units(),
			game_time 		= times[0],
			save_time 		= times[1],
			current_time 	= times[2],
			game_number 	= parser.get_game_number(),
			save_number 	= parser.get_save_number(),
			ironman 		= parser.get_ironman(),
			tactical_save 	= parser.get_tactical_save(),
			foundry 		= parser.get_foundry(),
			research 		= parser.get_research(),
		)

		

	def _cleanup(converter):
		"""
		Deletes the JSON file created by the converter, if it exists, per Config.
		"""
		if not Config.keep_json:
			try:
				converter.cleanup()
			except OSError:
				pass