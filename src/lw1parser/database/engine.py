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
		self.read = _Read(self.conn)

		self.create.create_tables()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def insert_save(self, save: Save):
		"""
		Inserts save data into database with check for duplicates. True if save info was inserted, False if save already exists in database.
		"""
		return self.insert.insert_save(save)


	# New, reconstructs entire Save dataclass
	def get_save(self, campaign_id: int = None, save_number: int = None):
		return self.read.get_save()

	# Old, only gets units, depreciated
	def get_units(self, campaign_id = None):
		return self.read.get_units(campaign_id)