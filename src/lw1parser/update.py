from lw1parser.config import Config
from lw1parser.export import Export
from lw1parser.savegame import Save
from lw1parser.database import Database

class Update:
	def __init__(self, save: Save):
		self.save = save

	def do_update(self):
		if Config.use_database:
			return self._save_db()
		else:
			Export.export_spreadsheet(Config.spreadsheet_format, self.save)
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