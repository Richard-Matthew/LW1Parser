from lw1parser.maps import UPGRADE_MAP, MEDAL_MAP

class _Create:
	def __init__(self, conn):
		self.conn = conn

	def create_tables(self):
		# SQL statements freehanded then properly formatted and wrapped in cur.execute via Copilot
		cur = self.conn.cursor()

		# Enable foreign keys
		cur.execute("PRAGMA foreign_keys = ON;")

		# campaign
		cur.execute("""
		CREATE TABLE IF NOT EXISTS campaign (
			id              INTEGER PRIMARY KEY,
			campaign_number INTEGER NOT NULL,
			time_start      TEXT    NOT NULL
		);
		""")

		# unit
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit (
			id             INTEGER PRIMARY KEY,
			campaign_id    INTEGER NOT NULL,
			ingame_id      INTEGER NOT NULL,
			snapshot_added INTEGER NOT NULL,
			FOREIGN KEY    (campaign_id)     REFERENCES campaign(id),
			FOREIGN KEY    (snapshot_added)  REFERENCES snapshot(id),
			UNIQUE         (campaign_id, ingame_id)
		);
		""")

		# snapshot (née update)
		cur.execute("""
		CREATE TABLE IF NOT EXISTS snapshot (
			id          INTEGER PRIMARY KEY,
			time_game   TEXT    NOT NULL,
			time_real   TEXT    NOT NULL,
			time_save   TEXT    NOT NULL,
			save_number INTEGER NOT NULL
		);
		""")

		# unit_snapshot
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit_snapshot (
			unit_id      INTEGER NOT NULL,
			snapshot_id  INTEGER NOT NULL,

			-- Identification
			first_name   TEXT NOT NULL,
			last_name    TEXT NOT NULL,
			nick_name    TEXT NOT NULL,
			ingame_class TEXT NOT NULL,

			-- Status
			rank         INTEGER NOT NULL,
			psi_rank     INTEGER NOT NULL,
			xp           INTEGER NOT NULL,
			psi_xp       INTEGER NOT NULL,
			kills        INTEGER NOT NULL,
			kia_date     TEXT    NOT NULL,
			special      TEXT    NOT NULL,

			-- Stats
			hitpoints    INTEGER NOT NULL,
			mobility     INTEGER NOT NULL,
			will         INTEGER NOT NULL,
			aim          INTEGER NOT NULL,
			defense      INTEGER NOT NULL,

			PRIMARY KEY  (unit_id, snapshot_id),
			FOREIGN KEY  (unit_id) REFERENCES unit(id),
			FOREIGN KEY  (snapshot_id) REFERENCES snapshot(id)
		);
		""")

		# perk
		cur.execute("""
		CREATE TABLE IF NOT EXISTS perk (
			id   INTEGER PRIMARY KEY,
			name TEXT    NOT NULL
		);
		""")

		# unit_perk
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit_perk (
			unit_id     INTEGER NOT NULL,
			snapshot_id INTEGER NOT NULL,
			perk_id     INTEGER NOT NULL,
			PRIMARY KEY (unit_id, snapshot_id, perk_id),
			FOREIGN KEY (unit_id) REFERENCES unit(id),
			FOREIGN KEY (snapshot_id) REFERENCES snapshot(id),
			FOREIGN KEY (perk_id) REFERENCES perk(id)
		);
		""")
		# Fill with values
		self._insert_perk_definitions(cur)

		# medal
		cur.execute("""
		CREATE TABLE IF NOT EXISTS medal (
			id   INTEGER PRIMARY KEY,
			name TEXT    NOT NULL
		);
		""")

		# unit_medal
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit_medal (
			unit_id     INTEGER NOT NULL,
			snapshot_id INTEGER NOT NULL,
			medal_id    INTEGER NOT NULL,
			PRIMARY KEY (unit_id, snapshot_id, medal_id),
			FOREIGN KEY (unit_id) REFERENCES unit(id),
			FOREIGN KEY (snapshot_id) REFERENCES snapshot(id),
			FOREIGN KEY (medal_id) REFERENCES medal(id)
		);
		""")
		# Fill with values
		self._insert_medal_definitions(cur)

		# Indexes
		cur.execute("CREATE INDEX IF NOT EXISTS idx_unit_campaign ON unit(campaign_id);")
		cur.execute("CREATE INDEX IF NOT EXISTS idx_unitsnapshot ON unit_snapshot(snapshot_id);")
		cur.execute("CREATE INDEX IF NOT EXISTS idx_unitperk_snapshot ON unit_perk(snapshot_id);")

		self.conn.commit()

	def _insert_perk_definitions(self, cur):
		for perk_id, name in UPGRADE_MAP.items():
			cur.execute("""
				INSERT OR IGNORE INTO perk (id, name)
				VALUES (?, ?)
			""", (perk_id, name))

	def _insert_medal_definitions(self, cur):
		for medal_id, name in MEDAL_MAP.items():
			cur.execute("""
				INSERT OR IGNORE INTO medal (id, name)
				VALUES (?, ?)
			""", (medal_id, name))
