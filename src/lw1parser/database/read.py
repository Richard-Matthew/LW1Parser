from lw1parser.unit import Unit
from lw1parser.savegame import Save

class _Read:
	"""
	Handles read operations for the database.
	"""
	def __init__(self, conn):
		self.conn = conn

	# Build a Save dataclass from the most recent snapshot
	def get_save(self, campaign_id:int | None = None) -> "Save":
		"""
		Returns a Save dataclass from the most recent update for the given campaign,
		or the most recent update.
		"""
		cur = self.conn.cursor()

		# Look for campaign with the most recent snapshot
		if campaign_id is None:
			cur.execute("""
				SELECT unit.campaign_id
				FROM unit
				JOIN unit_snapshot us ON us.unit_id = unit.id
				JOIN snapshot s ON s.id = us.snapshot_id
				ORDER BY s.time_real DESC
				LIMIT 1
			""")
			row = cur.fetchone()
			if row is None:
				raise ValueError("No campaigns found in database")
			campaign_id = row["campaign_id"]

		# Get the most recent snapshot for this campaign
		cur.execute("""
			SELECT s.*
			FROM snapshot s
			JOIN unit_snapshot us ON us.snapshot_id = s.id
			JOIN unit u ON u.id = us.unit_id
			WHERE u.campaign_id = ?
			ORDER BY s.time_real DESC
			LIMIT 1
		""", (campaign_id,))
		snap = cur.fetchone()
		
		if snap is None:
			raise ValueError(f"No snapshots found for campaign {campaign_id}")

		snapshot_id = snap["id"]


		return Save(
			units			=self.get_units(campaign_id),
			game_time		=snap["time_game"],
			save_time		=snap["time_save"],
			current_time	=snap["time_real"],
			game_number		=self._get_campaign_number(cur, campaign_id),
			save_number		=snap["save_number"],
			ironman			=bool(snap["ironman"]),
			tactical_save	=bool(snap["tactical_save"]),
			foundry			=self._get_foundry_snapshot(cur, snapshot_id),
			research		=self._get_research_snapshot(cur, snapshot_id),
		)

	# Get the most recent snapshot for every unit in a campaign
	def get_units(self, campaign_id: int | None = None) -> list[Unit]:
		cur = self.conn.cursor()

		# Look for campaign with the most recent snapshot
		if campaign_id is None:
			cur.execute("""
				SELECT unit.campaign_id
				FROM unit
				JOIN unit_snapshot us ON us.unit_id = unit.id
				JOIN snapshot s ON s.id = us.snapshot_id
				ORDER BY s.time_real DESC
				LIMIT 1
			""")
			row = cur.fetchone()
			if row is None:
				return []  # no campaigns exist
			campaign_id = row["campaign_id"]

		# Get latest snapshot for each unit in the selected campaign
		cur.execute("""
			SELECT us.*
			FROM unit_snapshot us
			JOIN (
				SELECT unit.id AS unit_id, MAX(us2.snapshot_id) AS max_snapshot
				FROM unit
				JOIN unit_snapshot us2 ON us2.unit_id = unit.id
				WHERE unit.campaign_id = ?
				GROUP BY unit.id
			) latest
			ON us.unit_id = latest.unit_id
			AND us.snapshot_id = latest.max_snapshot
		""", (campaign_id,))

		snapshot_rows = cur.fetchall()
		
		# Build Unit array
		units = [
			self._build_unit_from_snapshot_row(cur, row)
			for row in snapshot_rows
		]
		return units

	def _build_unit_from_snapshot_row(self, cur, row) -> Unit:
		unit_id = row["unit_id"]
		snapshot_id = row["snapshot_id"]

		# Load ingame_id from unit table
		cur.execute("SELECT ingame_id FROM unit WHERE id = ?", (unit_id,))
		ingame_id = cur.fetchone()["ingame_id"]

		# Build Unit dataclass
		unit = Unit(
			ingame_id=ingame_id,
			first_name=row["first_name"],
			last_name=row["last_name"],
			nick_name=row["nick_name"],
			ingame_class=row["ingame_class"],
			rank=row["rank"],
			special_rank=row["special_rank"],
			xp=row["xp"],
			psi_xp=row["psi_xp"],
			kills=row["kills"],
			kia_date=row["kia_date"],
			hp=row["hp"],
			aim=row["aim"],
			mobility=row["mobility"],
			willpower=row["willpower"],
			defense=row["defense"],
			soml_mission_count=row["soml_mission_count"],
			special=row["special"],

			class_perks={},
			officer_perks={},
			psi_perks={},
			gene_perks={},
			bonus_perks={}
		)

		unit.db_id = unit_id

		# Cache perk_source lookup
		cur.execute("SELECT id, name FROM perk_source")
		source_map = {row2["id"]: row2["name"] for row2 in cur.fetchall()}

		# Load perks grouped by source
		cur.execute("""
			SELECT up.perk_id, up.source_id, p.name
			FROM unit_perk up
			JOIN perk p ON p.id = up.perk_id
			WHERE up.unit_id = ? AND up.snapshot_id = ?
		""", (unit_id, snapshot_id))

		for perk in cur.fetchall():
			perk_id = perk["perk_id"]
			perk_name = perk["name"]
			source_name = source_map[perk["source_id"]]

			if source_name == "class":
				unit.class_perks[perk_id] = perk_name
			elif source_name == "officer":
				unit.officer_perks[perk_id] = perk_name
			elif source_name == "psi":
				unit.psi_perks[perk_id] = perk_name
			elif source_name == "gene":
				unit.gene_perks[perk_id] = perk_name
			elif source_name == "bonus":
				unit.bonus_perks[perk_id] = perk_name

		return unit

	def _get_campaign_number(self, cur, campaign_id):
		"""
		Gets game_number, stored as campaign_number in the database.
		"""
		cur.execute("SELECT campaign_number FROM campaign WHERE id = ?", (campaign_id,))
		return cur.fetchone()["campaign_number"]

	def _get_foundry_snapshot(self, cur, snapshot_id):
		cur.execute("""
			SELECT f.id, f.name
			FROM foundry_snapshot fs
			JOIN foundry f ON f.id = fs.foundry_id
			WHERE fs.snapshot_id = ?
		""", (snapshot_id,))
		return {row["id"]: row["name"] for row in cur.fetchall()}

	def _get_research_snapshot(self, cur, snapshot_id):
		cur.execute("""
			SELECT r.id, r.name
			FROM research_snapshot rs
			JOIN research r ON r.id = rs.research_id
			WHERE rs.snapshot_id = ?
		""", (snapshot_id,))
		return {row["id"]: row["name"] for row in cur.fetchall()}
