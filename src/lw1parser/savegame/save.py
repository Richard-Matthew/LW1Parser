from lw1parser.config import Config
from .locator import _Locator
from .converter import _Converter
from .parser import _Parser

from pathlib import Path
import os

class Save:
	"""
	Container class for loading and parsing data from a save file.
	"""
	def __init__(self, path: Path = None):
		self.locator = _Locator()
		self.converter = _Converter()

		if path:
			data = self.converter.convert(path)
		else:
			path = self.locator.find_latest(Config.save_path)
			data = self.converter.convert(path)

		parser = _Parser(data)

		# Check save type
		if parser.get_tactical_save():
			raise TypeError("Tactical saves are not supported")

		# Information from save
		self.units = parser.get_units()
		self.game_time,	self.save_time, self.current_time = parser.get_times()
		self.game_number = parser.get_game_number()
		self.save_number = parser.get_save_number()
		self.ironman = parser.get_ironman()
		self.tactical_save = parser.get_tactical_save()

		# Clean up JSON per Config setting
		self.cleanup()
			
	def cleanup(self):
		"""
		Deletes the JSON file created by the converter, if it exists.
		"""
		if not Config.keep_json:
			try:
				self.converter.cleanup()
			except OSError:
				pass