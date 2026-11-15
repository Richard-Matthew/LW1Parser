from lw1parser.config import Config
from lw1parser.database import Database
from lw1parser.export import export_spreadsheet
from lw1parser.savegame import Save


class Update:
	"""
	Handles Update process by inserting into database or exporting a spreadsheet.
	"""
	def __init__(self, save: Save):
		self.save = save

	def do_update(self) -> bool | None:
		"""
		Returns True/False for database operations, None for spreadsheet export.
		"""
		if Config.use_database:
			return self._save_db()
		else:
			export_spreadsheet(Config.spreadsheet_format, self.save)
			return None

	def _save_db(self):
		db = Database()
		was_inserted = db.insert_save(self.save)
		db.close()
		return was_inserted

	def _read_db(self):
		db = Database()
		units = db.get_units()
		db.close()
		return units