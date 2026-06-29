from lw1parser.config import Config
from lw1parser.export import Export
from lw1parser.savegame import Save
from lw1parser.database import Engine

class Update:
	def __init__(self, save: Save):
		self.save = save

	def do_update(self):
		if Config.use_database:
			return self._save_db()
		else:
			Export.export_csv(self.save)
			return None

	def _save_db(self):
		db = Engine()
		was_inserted = db.insert_save(self.save)
		db.close()
		return was_inserted

	def _read_db(self):
		db = Engine()
		units = db.get_units()
		db.close()
		return units