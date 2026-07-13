from lw1parser.maps import UPGRADE_MAP, FOUNDRY_UNLOCK_MAP, RESEARCH_UNLOCK_MAP

class _Create:
	def __init__(self, conn):
		self.conn = conn

	def create_tables(self):
		# SQL statements freehanded then formatted and wrapped in cur.execute via Copilot
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
			id          	INTEGER PRIMARY KEY,
			time_game   	TEXT,
			time_real   	TEXT,
			time_save   	TEXT,
			save_number 	INTEGER,
			ironman			BOOLEAN,
			tactical_save 	BOOLEAN
		);
		""")

		# unit_snapshot
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit_snapshot (
			unit_id      INTEGER NOT NULL,
			snapshot_id  INTEGER NOT NULL,

			-- Identification
			ingame_id    INTEGER NOT NULL,
			first_name   TEXT,
			last_name    TEXT,
			nick_name    TEXT,
			ingame_class TEXT,

			-- Status
			rank         INTEGER,
			special_rank INTEGER,
			xp           INTEGER,
			psi_xp       INTEGER,
			kills        INTEGER,
			kia_date     TEXT   ,

			-- Stats
			hp           INTEGER,
			aim          INTEGER,
			mobility     INTEGER,
			willpower    INTEGER,
			defense      INTEGER,

			-- Other
			soml_mission_count INTEGER,
			special      TEXT,

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

		# perk_source
		cur.execute("""
		CREATE TABLE IF NOT EXISTS perk_source (
			  id	INTEGER  PRIMARY KEY,
			  name	TEXT     UNIQUE	      NOT NULL
		);
		""")
		# Add values
		self._insert_perk_source_definitions(cur)

		# unit_perk
		cur.execute("""
		CREATE TABLE IF NOT EXISTS unit_perk (
			unit_id     INTEGER NOT NULL,
			snapshot_id INTEGER NOT NULL,
			perk_id     INTEGER NOT NULL,
			source_id	INTEGER NOT NULL,
			PRIMARY KEY (unit_id, snapshot_id, perk_id),
			FOREIGN KEY (unit_id) 		REFERENCES unit(id),
			FOREIGN KEY (snapshot_id) 	REFERENCES snapshot(id),
			FOREIGN KEY (perk_id) 		REFERENCES perk(id),
			FOREIGN KEY (source_id) 	REFERENCES perk_source(id)
		);
		""")
		# Add values
		self._insert_perk_definitions(cur)

		# foundry
		cur.execute("""
		CREATE TABLE IF NOT EXISTS foundry (
			id   INTEGER PRIMARY KEY,
			name TEXT    NOT NULL
		);
		""")
		self._insert_foundry_definitions(cur)
		
		# foundry_snapshot
		cur.execute("""
		CREATE TABLE IF NOT EXISTS foundry_snapshot (
			foundry_id  	INTEGER NOT NULL,
			snapshot_id 	INTEGER NOT NULL,
			PRIMARY KEY 	(snapshot_id, foundry_id),
			FOREIGN KEY 	(snapshot_id) 	REFERENCES snapshot(id),
			FOREIGN KEY 	(foundry_id) 	REFERENCES foundry(id)
		);
		""")

		# research
		cur.execute("""
		CREATE TABLE IF NOT EXISTS research (
			id   INTEGER PRIMARY KEY,
			name TEXT    NOT NULL
		);
		""")
		self._insert_research_definitions(cur)

		# research_snapshot
		cur.execute("""
		CREATE TABLE IF NOT EXISTS research_snapshot (
			research_id  	INTEGER NOT NULL,
			snapshot_id 	INTEGER NOT NULL,
			PRIMARY KEY 	(snapshot_id, research_id),
			FOREIGN KEY 	(snapshot_id) 	REFERENCES snapshot(id),
			FOREIGN KEY 	(research_id) 	REFERENCES research(id)
		);
		""")

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

	def _insert_foundry_definitions(self, cur):
		for perk_id, name in FOUNDRY_UNLOCK_MAP.items():
			cur.execute("""
			INSERT OR IGNORE INTO foundry (id, name)
				VALUES (?, ?)
			""", (perk_id, name))

	def _insert_research_definitions(self, cur):
		for perk_id, name in RESEARCH_UNLOCK_MAP.items():
			cur.execute("""
			INSERT OR IGNORE INTO research (id, name)
				VALUES (?, ?)
			""", (perk_id, name))

	def _insert_perk_source_definitions(self, cur):
		cur.execute("""
		INSERT OR IGNORE INTO perk_source (name) VALUES
			('class'),
			('officer'),
			('psi'),
			('gene'),
			('bonus');
		""")