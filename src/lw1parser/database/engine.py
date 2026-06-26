from lw1parser.savegame import Save
from .create import _Create
from .update import _Update
from .read import _Read
import sqlite3

class Engine:
	DB_NAME = "lw1parser.sqlite"

	def __init__(self):
		self.conn = sqlite3.connect(Engine.DB_NAME)
		self.conn.row_factory = sqlite3.Row

		self.create = _Create(self.conn)
		self.insert = _Update(self.conn)
		self.extract = _Read(self.conn)

		self.create.create_tables()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def insert_save(self, save: Save):
		"""
		Inserts save data into database with check for duplicates. True if save info was inserted, False if save already exists in database.
		"""
		return self.insert.insert_save(save)

	# Potential for full Save class restoration from db
	"""
	 def get_save(self, campaign_id, save_number):
		etc
	"""

	# Until then everything uses this to get unit stats
	def get_units(self, campaign_id = None):
		return self._extract_units(campaign_id)

	def _extract_units(self, campaign_id = None):
		return self.extract.get_current_units(campaign_id)