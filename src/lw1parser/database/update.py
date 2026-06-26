from lw1parser.savegame import Save

class _Update:
	"""
	Manages write operations for database.
	"""
	def __init__(self, conn):
		self.conn = conn

	def insert_save(self, save: Save):
		"""
		Inserts save data into database with check for duplicates.
		Returns True if save info was inserted, False if save already exists in database.
		"""
		cur = self.conn.cursor()

		# Check for save collision
		campaign_id           = self._get_or_create_campaign(cur, save.game_number, save.current_time)
		snapshot_id, inserted = self._get_or_create_snapshot(cur, save.game_time, save.current_time, save.save_time, save.save_number)

		# If save has already been processed, abort update
		if not inserted:
			return False

		# Insert missing units and populate Unit db_id field
		self._insert_units(cur, campaign_id, snapshot_id, save.units)

		# Insert snapshot of current unit states
		self._insert_unit_snapshots(cur, snapshot_id, save.units)

		self._insert_unit_perks(cur, snapshot_id, save.units)

		return True

	def _get_or_create_campaign(self, cur, campaign_number, time_start):
		# Check if campaign with matching id exists
		cur.execute("""
			SELECT id FROM campaign
			WHERE campaign_number = ?
		""", (campaign_number,))
		row = cur.fetchone()
		if row:
			return row["id"]

		# Otherwise, insert a new row
		cur.execute("""
			INSERT INTO campaign (
				campaign_number, time_start
			)
			VALUES (?, ?)
		""", (campaign_number, time_start))
		return cur.lastrowid

	def _get_or_create_snapshot(self, cur, time_game, time_real, time_save, save_number):
		"""
		Checks if save has already been inserted into datase. Returns id and a bool for if a row was inserted
		"""
		# Check if snapshot for current most recent save has already been created
		cur.execute("""
			SELECT id FROM snapshot
			WHERE save_number = ? AND time_save = ?
		""", (save_number, time_save))
		row = cur.fetchone()
		if row:
			return row["id"], False

		# Otherwise create new snapshot with auto increment id
		cur.execute("""
			INSERT INTO snapshot (
				time_game, time_real, time_save, save_number
			)
			VALUES (?, ?, ?, ?)
		""", (time_game, time_real, time_save, save_number))
		return cur.lastrowid, True

	def _insert_units(self, cur, campaign_id, snapshot_id, units):
		for unit in units:
			# Check if unit already exists
			cur.execute("""
				SELECT id FROM unit
				WHERE campaign_id = ? AND ingame_id = ?
			""", (campaign_id, unit.ingame_id))
			row = cur.fetchone()

			# Unit already exists, update Unit db_id and go to next unit
			if row:
				unit.db_id = row["id"]
				continue

			# Unit is new, insert row and update Unit db_id
			cur.execute("""
				INSERT INTO unit (
					campaign_id, ingame_id, snapshot_added
				)
				VALUES (?, ?, ?)
			""", (campaign_id, unit.ingame_id, snapshot_id))

			unit.db_id = cur.lastrowid

	def _insert_unit_snapshots(self, cur, snapshot_id, units):
		for unit in units:
			# Check for KIA
			cur.execute("""
				SELECT kia_date
				FROM unit_snapshot
				WHERE unit_id = ?
				ORDER BY snapshot_id DESC
				LIMIT 1
			""", (unit.db_id,))
			row = cur.fetchone()

			# Check if Unit db_id found
			if row:
				# Check if already KIA
				if row["kia_date"] != "" and unit.kia_date != "":
					# Unit has been KIA since last snapshot, skip
					continue

			# Otherwise continue
			# Full storage of Unit dataclass
			cur.execute("""
				INSERT INTO unit_snapshot (
					unit_id, snapshot_id,
					first_name, last_name, nick_name, ingame_class,
					rank, psi_rank, xp, psi_xp, kills, kia_date, special,
					hitpoints, mobility, will, aim, defense
				)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
			""", (
				unit.db_id, snapshot_id,
				unit.first_name, unit.last_name, unit.nick_name, unit.ingame_class,
				unit.rank, unit.psi_rank, unit.xp, unit.psi_xp, unit.kills, unit.kia_date, unit.special,
				unit.hp, unit.mobility, unit.willpower, unit.aim, unit.defense
			))

	def _insert_unit_perks(self, cur, snapshot_id, units):
		for unit in units:
			for perk_id in unit.perks.keys():
				cur.execute("""
					INSERT INTO unit_perk (
						unit_id, snapshot_id, perk_id
					)
					VALUES (?, ?, ?)
				""", (unit.db_id, snapshot_id, perk_id))

	def _insert_unit_medals(self, cur, snapshot_id, units):
		for unit in units:
			for medal_id in unit.officer_perks:
				cur.execute("""
					INSERT INTO unit_medal (
						unit_id, snapshot_id, medal_id)
					VALUES (?, ?, ?)
				""", (unit.db_id, snapshot_id, medal_id))
