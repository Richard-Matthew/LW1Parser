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
		campaign_id           = self._get_or_create_campaign(cur, save)
		snapshot_id, inserted = self._get_or_create_snapshot(cur, save)

		# If save has already been processed, abort update
		if not inserted:
			return False

		self._insert_foundry_snapshot(cur, snapshot_id, save.foundry)
		self._insert_research_snapshot(cur, snapshot_id, save.research)

		# Insert missing units and populate Unit db_id field
		self._insert_units(cur, campaign_id, snapshot_id, save.units)

		# Insert snapshot of current unit states
		self._insert_unit_snapshots(cur, snapshot_id, save.units)

		self._insert_unit_perks(cur, snapshot_id, save.units)

		return True

	def _get_or_create_campaign(self, cur, save: Save):
		# Check if campaign with matching id exists
		cur.execute("""
			SELECT id FROM campaign
			WHERE campaign_number = ?
		""", (save.game_number,))
		row = cur.fetchone()
		if row:
			return row["id"]

		# Otherwise, insert a new row
		cur.execute("""
			INSERT INTO campaign (
				campaign_number, time_start
			)
			VALUES (?, ?)
		""", (save.game_number, save.current_time))
		return cur.lastrowid

	def _get_or_create_snapshot(self, cur, save: Save):
		"""
		Checks if save has already been inserted into datase. Returns id and a bool for if a row was inserted
		"""
		# Check if snapshot for current most recent save has already been created
		cur.execute("""
			SELECT id FROM snapshot
			WHERE save_number = ? AND time_save = ?
		""", (save.save_number, save.save_time))
		row = cur.fetchone()
		if row:
			return row["id"], False

		# Otherwise create new snapshot with auto increment id
		cur.execute("""
			INSERT INTO snapshot (
				time_game, time_real, time_save,
			  	save_number, ironman, tactical_save
			)
			VALUES (?, ?, ?, ?, ?, ?)
		""", (
			save.game_time, save.current_time, save.save_time,
			save.save_number, int(save.ironman), int(save.tactical_save)
		))
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
			if row:  # noqa: SIM102
				# Check if already KIA
				if row["kia_date"] != "" and unit.kia_date != "":
					# Unit has been KIA since last snapshot, skip
					continue

			# Otherwise continue
			# Full storage of Unit dataclass
			cur.execute("""
			INSERT INTO unit_snapshot (
				unit_id, snapshot_id,
				ingame_id,
				first_name, last_name, nick_name, ingame_class,
				rank, special_rank, xp, psi_xp, kills, kia_date,
				hp, aim, mobility, willpower, defense,
				soml_mission_count,
				special
			)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
			""", (
				unit.db_id, snapshot_id, unit.ingame_id,
				unit.first_name, unit.last_name, unit.nick_name,
				unit.ingame_class, unit.rank, unit.special_rank,
				unit.xp, unit.psi_xp, unit.kills, unit.kia_date,
				unit.hp, unit.aim, unit.mobility, unit.willpower, unit.defense,
				unit.soml_mission_count, unit.special
			))

	def _insert_unit_perks(self, cur, snapshot_id, units) -> None:
		# Cache perk_source lookup to avoid repeated SELECTs
		source_ids = {
			row[0]: row[1]
			for row in cur.execute("SELECT name, id FROM perk_source")
		}

		for unit in units:
			perks = {
				"class":   unit.class_perks,
				"officer": unit.officer_perks,
				"psi":     unit.psi_perks,
				"gene":    unit.gene_perks,
				"bonus":   unit.bonus_perks,
			}

			# Insert each perk with its source_id
			for source_name, perk_dict in perks.items():
				# Skip empty perk dicts
				if not perk_dict:
					continue

				source_id = source_ids[source_name]

				for perk_id in perk_dict:
					cur.execute("""
						INSERT INTO unit_perk (
							unit_id, snapshot_id, perk_id, source_id
						)
						VALUES (?, ?, ?, ?)
					""", (
						unit.db_id,
						snapshot_id,
						perk_id,
						source_id
					))

	def _insert_foundry_snapshot(self, cur, snapshot_id, unlocks: dict[int,str]) -> None:
		"""
		Inserts foundry unlocks into foundry_snapshot bridge table.
		"""
		for foundry_id in unlocks:
			cur.execute("""
				INSERT INTO foundry_snapshot (
					foundry_id, snapshot_id
				)
				VALUES (?, ?)
			""", (
				foundry_id, snapshot_id
			))

	def _insert_research_snapshot(self, cur, snapshot_id, unlocks: dict[int,str]) -> None:
		"""
		Inserts research unlocks into research_snapshot bridge table.
		"""
		for research_id in unlocks:
			cur.execute("""
				INSERT INTO research_snapshot (
					research_id, snapshot_id
				)
				VALUES (?, ?)
			""", (
				research_id, snapshot_id
			))
