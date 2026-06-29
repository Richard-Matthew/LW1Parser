from lw1parser.unit import Unit

class _Read:
	def __init__(self, conn):
		self.conn = conn

	# Get the most recent snapshot for every unit in a campaign
	def get_current_units(self, campaign_id: int | None = None) -> list[Unit]:
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
		units: list[Unit] = []

		# Build Unit dataclasses
		for row in snapshot_rows:
			unit_id = row["unit_id"]
			snapshot_id = row["snapshot_id"]

			# ingame_id
			cur.execute("SELECT ingame_id FROM unit WHERE id = ?", (unit_id,))
			ingame_id = cur.fetchone()["ingame_id"]

			# Assign the rest
			unit = Unit(
				ingame_id=ingame_id,
				first_name=row["first_name"],
				last_name=row["last_name"],
				nick_name=row["nick_name"],
				ingame_class=row["ingame_class"],
				rank=row["rank"],
				#psi_rank=row["psi_rank"],
				xp=row["xp"],
				psi_xp=row["psi_xp"],
				kills=row["kills"],
				kia_date=row["kia_date"],
				hp=row["hitpoints"],
				aim=row["aim"],
				mobility=row["mobility"],
				willpower=row["will"],
				defense=row["defense"],
				class_perks={},
				office_medals=[],
				special=row["special"]
			)

			unit.db_id = unit_id

			# Perks
			cur.execute("""
				SELECT up.perk_id, p.name
				FROM unit_perk up
				JOIN perk p ON p.id = up.perk_id
				WHERE up.unit_id = ? AND up.snapshot_id = ?
			""", (unit_id, snapshot_id))

			for p in cur.fetchall():
				unit.class_perks[p["perk_id"]] = p["name"]


			# Officer medals
			cur.execute("""
				SELECT um.medal_id, m.name
				FROM unit_medal um
				JOIN medal m ON m.id = um.medal_id
				WHERE um.unit_id = ? AND um.snapshot_id = ?
			""", (unit_id, snapshot_id))

			unit.office_medals = {
				m["medal_id"]: m["name"]
				for m in cur.fetchall()
			}

			units.append(unit)

		return units
