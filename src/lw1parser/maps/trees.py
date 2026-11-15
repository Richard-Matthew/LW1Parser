from .perks import UPGRADE_TO_ID

CLASS_PERKS = {
	# Biological
	"Scout": {
		1: [
			UPGRADE_TO_ID("Lightning Reflexes")
		],
		2: [
			UPGRADE_TO_ID("Holo-Targeting"),
			UPGRADE_TO_ID("Damn Good Ground"),
			UPGRADE_TO_ID("Lone Wolf")
		],
		3: [
			UPGRADE_TO_ID("Low Profile"),
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Deadeye")
		],
		4: [
			UPGRADE_TO_ID("Flush"),
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Battle Scanner")
		],
		5: [
			UPGRADE_TO_ID("Concealment"),
			UPGRADE_TO_ID("In the Zone"),
			UPGRADE_TO_ID("Hit and Run")
		],
		6: [
			UPGRADE_TO_ID("Tactical Sense"),
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Sprinter")
		],
		7: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Smoke & Mirrors")
		],
	},

	"Sniper": {
		1: [
			UPGRADE_TO_ID("Squadsight"),
		],
		2: [
			UPGRADE_TO_ID("Low Profile"),
			UPGRADE_TO_ID("Deadeye"),
			UPGRADE_TO_ID("Lone Wolf"),
		],
		3: [
			UPGRADE_TO_ID("Disabling Shot"),
			UPGRADE_TO_ID("Precision Shot"),
			UPGRADE_TO_ID("Snapshot"),
		],
		4: [
			UPGRADE_TO_ID("Damn Good Ground"),
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Sharpshooter"),
		],
		5: [
			UPGRADE_TO_ID("Executioner"),
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Platform Stability"),
		],
		6: [
			UPGRADE_TO_ID("Tactical Sense"),
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Lock N' Load"),
		],
		7: [
			UPGRADE_TO_ID("In the Zone"),
			UPGRADE_TO_ID("Mayhem"),
			UPGRADE_TO_ID("Double Tap"),
		],
	},

	"Infantry": {
		1: [
			UPGRADE_TO_ID("Light 'Em Up"),
		],
		2: [
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Covering Fire"),
			UPGRADE_TO_ID("Executioner"),
		],
		3: [
			UPGRADE_TO_ID("Will to Survive"),
			UPGRADE_TO_ID("Opportunist"),
			UPGRADE_TO_ID("Aggression"),
		],
		4: [
			UPGRADE_TO_ID("Deadeye"),
			UPGRADE_TO_ID("Suppression"),
			UPGRADE_TO_ID("Ranger"),
		],
		5: [
			UPGRADE_TO_ID("Tactical Sense"),
			UPGRADE_TO_ID("Lock N' Load"),
			UPGRADE_TO_ID("Sharpshooter"),
		],
		6: [
			UPGRADE_TO_ID("Resilience"),
			UPGRADE_TO_ID("Sentinel"),
			UPGRADE_TO_ID("Bring 'Em On"),
		],
		7: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Rapid Fire"),
		],
	},

	"Assault": {
		1: [
			UPGRADE_TO_ID("Run & Gun"),
		],
		2: [
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Close Combat Specialist"),
			UPGRADE_TO_ID("Flush"),
		],
		3: [
			UPGRADE_TO_ID("Will to Survive"),
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Ranger"),
		],
		4: [
			UPGRADE_TO_ID("Close Encounters"),
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Hit and Run"),
		],
		5: [
			UPGRADE_TO_ID("Resilience"),
			UPGRADE_TO_ID("Killer Instinct"),
			UPGRADE_TO_ID("Executioner"),
		],
		6: [
			UPGRADE_TO_ID("Tactical Sense"),
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Sprinter"),
		],
		7: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Lightning Reflexes"),
		],
	},

	"Gunner": {
		1: [
			UPGRADE_TO_ID("Suppression"),
		],
		2: [
			UPGRADE_TO_ID("Flush"),
			UPGRADE_TO_ID("Covering Fire"),
			UPGRADE_TO_ID("Holo-Targeting"),
		],
		3: [
			UPGRADE_TO_ID("HEAT Ammo"),
			UPGRADE_TO_ID("Opportunist"),
			UPGRADE_TO_ID("Shredder Ammo"),
		],
		4: [
			UPGRADE_TO_ID("Will to Survive"),
			UPGRADE_TO_ID("Executioner"),
			UPGRADE_TO_ID("Ranger"),
		],
		5: [
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Ready for Anything"),
			UPGRADE_TO_ID("Double Tap"),
		],
		6: [
			UPGRADE_TO_ID("Resilience"),
			UPGRADE_TO_ID("Platform Stability"),
			UPGRADE_TO_ID("Danger Zone"),
		],
		7: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Sentinel"),
			UPGRADE_TO_ID("Mayhem"),
		],
	},

	"Rocketeer": {
		1: [
			UPGRADE_TO_ID("Fire Rocket"),
		],
		2: [
			UPGRADE_TO_ID("Will to Survive"),
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("HEAT Warheads"),
		],
		3: [
			UPGRADE_TO_ID("Rapid Reaction"),
			UPGRADE_TO_ID("Fire In the Hole"),
			UPGRADE_TO_ID("Snapshot"),
		],
		4: [
			UPGRADE_TO_ID("Suppression"),
			UPGRADE_TO_ID("Platform Stability"),
			UPGRADE_TO_ID("Shredder Ammo"),
		],
		5: [
			UPGRADE_TO_ID("Tactical Sense"),
			UPGRADE_TO_ID("Opportunist"),
			UPGRADE_TO_ID("Mayhem"),
		],
		6: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Double Tap"),
			UPGRADE_TO_ID("Shock & Awe"),
		],
		7: [
			UPGRADE_TO_ID("Tandem Warheads"),
			UPGRADE_TO_ID("Javelin Rockets"),
			UPGRADE_TO_ID("Danger Zone"),
		],
	},

	"Medic": {
		1: [
			UPGRADE_TO_ID("Field Medic"),
		],
		2: [
			UPGRADE_TO_ID("Suppression"),
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Field Surgeon"),
		],
		3: [
			UPGRADE_TO_ID("Rapid Reaction"),
			UPGRADE_TO_ID("Smoke & Mirrors"),
			UPGRADE_TO_ID("Revive"),
		],
		4: [
			UPGRADE_TO_ID("Ready for Anything"),
			UPGRADE_TO_ID("Smoke Grenade"),
			UPGRADE_TO_ID("Paramedic"),
		],
		5: [
			UPGRADE_TO_ID("Opportunist"),
			UPGRADE_TO_ID("Dense Smoke"),
			UPGRADE_TO_ID("Combat Drugs"),
		],
		6: [
			UPGRADE_TO_ID("Lock N' Load"),
			UPGRADE_TO_ID("Bombard"),
			UPGRADE_TO_ID("Sprinter"),
		],
		7: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("Savior"),
		],
	},

	"Engineer": {
		1: [
			UPGRADE_TO_ID("Grenadier"),
		],
		2: [
			UPGRADE_TO_ID("Holo-Targeting"),
			UPGRADE_TO_ID("Smoke Grenade"),
			UPGRADE_TO_ID("Sapper"),
		],
		3: [
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Smoke & Mirrors"),
			UPGRADE_TO_ID("HEAT Warheads"),
		],
		4: [
			UPGRADE_TO_ID("Will to Survive"),
			UPGRADE_TO_ID("Repair"),
			UPGRADE_TO_ID("Suppression"),
		],
		5: [
			UPGRADE_TO_ID("Battle Scanner"),
			UPGRADE_TO_ID("Dense Smoke"),
			UPGRADE_TO_ID("Mayhem"),
		],
		6: [
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("HEAT Ammo"),
		],
		7: [
			UPGRADE_TO_ID("Tandem Warheads"),
			UPGRADE_TO_ID("Fire Rocket"),
			UPGRADE_TO_ID("Bombard"),
		],
	},

	# MEC
	"Jaeger": {
		1: [
			UPGRADE_TO_ID("In the Zone"),
		],
		2: [
			UPGRADE_TO_ID("Damn Good Ground"),
			UPGRADE_TO_ID("Platform Stability"),
			UPGRADE_TO_ID("Sharpshooter"),
		],
		3: [
			UPGRADE_TO_ID("Executioner"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Flush"),
		],
		4: [
			UPGRADE_TO_ID("Lone Wolf"),
			UPGRADE_TO_ID("Advanced Fire Control"),
			UPGRADE_TO_ID("Ranger"),
		],
		5: [
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("Squadsight"),
		],
		6: [
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Shredder Ammo"),
		],
		7: [
			UPGRADE_TO_ID("Lock N' Load"),
			UPGRADE_TO_ID("Absorption Fields"),
			UPGRADE_TO_ID("Vital Point Targeting"),
		],
	},

	"Pathfinder": {
		1: [
			UPGRADE_TO_ID("Hit and Run"),
		],
		2: [
			UPGRADE_TO_ID("Deadeye"),
			UPGRADE_TO_ID("Advanced Fire Control"),
			UPGRADE_TO_ID("Lone Wolf"),
		],
		3: [
			UPGRADE_TO_ID("Damn Good Ground"),
			UPGRADE_TO_ID("Sharpshooter"),
			UPGRADE_TO_ID("Flush"),
		],
		4: [
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Executioner"),
			UPGRADE_TO_ID("Repair Servos"),
		],
		5: [
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Vital Point Targeting"),
		],
		6: [
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Squadsight"),
			UPGRADE_TO_ID("Lock N' Load"),
		],
		7: [
			UPGRADE_TO_ID("Lightning Reflexes"),
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Absorption Fields"),
		],
	},

	"Valkyrie": {
		1: [
			UPGRADE_TO_ID("Light 'Em Up"),
		],
		2: [
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Flush"),
		],
		3: [
			UPGRADE_TO_ID("Platform Stability"),
			UPGRADE_TO_ID("Reactive Targeting Sensors"),
			UPGRADE_TO_ID("Rapid Reaction"),
		],
		4: [
			UPGRADE_TO_ID("Lock N' Load"),
			UPGRADE_TO_ID("HEAT Ammo"),
			UPGRADE_TO_ID("Shredder Ammo"),
		],
		5: [
			UPGRADE_TO_ID("Sharpshooter"),
			UPGRADE_TO_ID("Opportunist"),
			UPGRADE_TO_ID("Damage Control"),
		],
		6: [
			UPGRADE_TO_ID("Collateral Damage"),
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Repair Servos"),
		],
		7: [
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Absorption Fields"),
		],
	},

	"Marauder": {
		1: [
			UPGRADE_TO_ID("Close Encounters"),
		],
		2: [
			UPGRADE_TO_ID("Aggression"),
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Shock-Absorbent Armor"),
		],
		3: [
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("Close Combat Specialist"),
			UPGRADE_TO_ID("Collateral Damage"),
		],
		4: [
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Executioner"),
			UPGRADE_TO_ID("Ranger"),
		],
		5: [
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Flush"),
			UPGRADE_TO_ID("Advanced Fire Control"),
		],
		6: [
			UPGRADE_TO_ID("Bring 'Em On"),
			UPGRADE_TO_ID("Reactive Targeting Sensors"),
			UPGRADE_TO_ID("Vital Point Targeting"),
		],
		7: [
			UPGRADE_TO_ID("Run & Gun"),
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Absorption Fields"),
		],
	},

	"Goliath": {
		1: [
			UPGRADE_TO_ID("Absorption Fields"),
		],
		2: [
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Reactive Targeting Sensors"),
			UPGRADE_TO_ID("Flush"),
		],
		3: [
			UPGRADE_TO_ID("Covering Fire"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Ranger"),
		],
		4: [
			UPGRADE_TO_ID("Mayhem"),
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Advanced Fire Control"),
		],
		5: [
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("Shock-Absorbent Armor"),
			UPGRADE_TO_ID("Vital Point Targeting"),
		],
		6: [
			UPGRADE_TO_ID("HEAT Ammo"),
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("Collateral Damage"),
		],
		7: [
			UPGRADE_TO_ID("Close Combat Specialist"),
			UPGRADE_TO_ID("Extra Conditioning"),
			UPGRADE_TO_ID("Rapid Fire"),
		],
	},

	"Archer": {
		1: [
			UPGRADE_TO_ID("Bombard"),
		],
		2: [
			UPGRADE_TO_ID("HEAT Warheads"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Platform Stability"),
		],
		3: [
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Advanced Fire Control"),
			UPGRADE_TO_ID("Mayhem"),
		],
		4: [
			UPGRADE_TO_ID("Ranger"),
			UPGRADE_TO_ID("Reactive Targeting Sensors"),
			UPGRADE_TO_ID("Sapper"),
		],
		5: [
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("Collateral Damage"),
		],
		6: [
			UPGRADE_TO_ID("Danger Zone"),
			UPGRADE_TO_ID("Double Tap"),
			UPGRADE_TO_ID("Damage Control"),
		],
		7: [
			UPGRADE_TO_ID("Grenadier"),
			UPGRADE_TO_ID("Tandem Warheads"),
			UPGRADE_TO_ID("Absorption Fields"),
		],
	},

"Guardian": {
		1: [
			UPGRADE_TO_ID("Opportunist"),
		],
		2: [
			UPGRADE_TO_ID("Field Medic"),
			UPGRADE_TO_ID("Steadfast"),
			UPGRADE_TO_ID("Ranger"),
		],
		3: [
			UPGRADE_TO_ID("Platform Stability"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Covering Fire"),
		],
		4: [
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Sentinel"),
		],
		5: [
			UPGRADE_TO_ID("Savior"),
			UPGRADE_TO_ID("Deadeye"),
			UPGRADE_TO_ID("Reactive Targeting Sensors"),
		],
		6: [
			UPGRADE_TO_ID("Vital Point Targeting"),
			UPGRADE_TO_ID("Lock N' Load"),
			UPGRADE_TO_ID("Absorption Fields"),
		],
		7: [
			UPGRADE_TO_ID("Ready for Anything"),
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("Double Tap"),
		],
	},

	"Shogun": {
		1: [
			UPGRADE_TO_ID("Collateral Damage"),
		],
		2: [
			UPGRADE_TO_ID("Packmaster"),
			UPGRADE_TO_ID("Damage Control"),
			UPGRADE_TO_ID("HEAT Ammo"),
		],
		3: [
			UPGRADE_TO_ID("HEAT Warheads"),
			UPGRADE_TO_ID("Automated Threat Assessment"),
			UPGRADE_TO_ID("Deadeye"),
		],
		4: [
			UPGRADE_TO_ID("Mayhem"),
			UPGRADE_TO_ID("Repair Servos"),
			UPGRADE_TO_ID("Flush"),
		],
		5: [
			UPGRADE_TO_ID("Sapper"),
			UPGRADE_TO_ID("Shock-Absorbent Armor"),
			UPGRADE_TO_ID("Ranger"),
		],
		6: [
			UPGRADE_TO_ID("Tandem Warheads"),
			UPGRADE_TO_ID("Rapid Fire"),
			UPGRADE_TO_ID("Light 'Em Up"),
		],
		7: [
			UPGRADE_TO_ID("Grenadier"),
			UPGRADE_TO_ID("Absorption Fields"),
			UPGRADE_TO_ID("Shredder Ammo"),
		],
	},

	# Special
	"Psionic": {
		1: [
			UPGRADE_TO_ID("Regen Biofield"),
			UPGRADE_TO_ID("Neural Feedback"),
			UPGRADE_TO_ID("Mindfray"),
		],
		2: [
			UPGRADE_TO_ID("Distortion Field"),
			UPGRADE_TO_ID("Psi Inspiration"),
		],
		3: [
			UPGRADE_TO_ID("Psi Panic"),
			UPGRADE_TO_ID("Mind Merge (active)"),
		],
		4: [
			UPGRADE_TO_ID("Psychokinetic Strike"),
			UPGRADE_TO_ID("Pyrokinesis"),
			UPGRADE_TO_ID("Telekinetic Field"),
		],
		5: [
			UPGRADE_TO_ID("Mind Control"),
		],
		6: [
			UPGRADE_TO_ID("Rift"),
		],
	},

	"Officer": {
		0: [  # All Officers get both of these perks, but Command isn't in the Upgrades array
			UPGRADE_TO_ID("Lead By Example"),
			#UPGRADE_TO_ID("Command"),
		],

		1: [  # Lieutenant
			UPGRADE_TO_ID("Legio Patria Nostra"),
			UPGRADE_TO_ID("Stay Frosty"),
		],

		2: [  # Captain
			UPGRADE_TO_ID("Semper Vigilans"),
			UPGRADE_TO_ID("Fortiores Una"),
		],

		3: [  # Major
			UPGRADE_TO_ID("Into the Breach"),
			UPGRADE_TO_ID("So Shall You Fight"),
		],

		4: [  # Colonel
			UPGRADE_TO_ID("Band of Warriors"),
			UPGRADE_TO_ID("Esprit de Corps"),
		],

		5: [  # Field Commander
			UPGRADE_TO_ID("So Others May Live"),
			UPGRADE_TO_ID("Combined Arms"),
		],
	},
}

PERK_STAT_BONUS = {
	# Format:
	# (ClassName, Rank, PerkID): {"StatName": modifier}

	# Scout
	("Scout", 1, UPGRADE_TO_ID("Lightning Reflexes")): {"mobility": 1},
	("Scout", 3, UPGRADE_TO_ID("Ranger")): {"aim": 1},
	("Scout", 3, UPGRADE_TO_ID("Deadeye")): {"aim": 1},
	("Scout", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Sniper
	("Sniper", 4, UPGRADE_TO_ID("Damn Good Ground")): {"will": 2},
	("Sniper", 7, UPGRADE_TO_ID("Mayhem")): {"aim": 2},

	# Infantry
	("Infantry", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Infantry", 5, UPGRADE_TO_ID("Sharpshooter")): {"aim": 2},
	("Infantry", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Assault
	("Assault", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Assault", 3, UPGRADE_TO_ID("Will to Survive")): {"will": 3},
	("Assault", 4, UPGRADE_TO_ID("Close Encounters")): {"will": 3},
	("Assault", 5, UPGRADE_TO_ID("Executioner")): {"aim": 2, "will": 2},
	("Assault", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Gunner
	("Gunner", 2, UPGRADE_TO_ID("Covering Fire")): {"aim": 2},
	("Gunner", 4, UPGRADE_TO_ID("Will to Survive")): {"will": 3},
	("Gunner", 5, UPGRADE_TO_ID("Ready for Anything")): {"aim": 2},
	("Gunner", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Rocketeer
	("Rocketeer", 2, UPGRADE_TO_ID("Will to Survive")): {"will": 3},
	("Rocketeer", 3, UPGRADE_TO_ID("Rapid Reaction")): {"aim": 2},
	("Rocketeer", 6, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 3, "will": 3, "mobility": 1},

	# Medic
	("Medic", 1, UPGRADE_TO_ID("Field Medic")): {"mobility": 1},
	("Medic", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Medic", 3, UPGRADE_TO_ID("Rapid Reaction")): {"aim": 3},
	("Medic", 3, UPGRADE_TO_ID("Revive")): {"will": 2},
	("Medic", 4, UPGRADE_TO_ID("Ready for Anything")): {"will": 3},
	("Medic", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Engineer
	("Engineer", 2, UPGRADE_TO_ID("Holo-Targeting")): {"aim": 1},
	("Engineer", 3, UPGRADE_TO_ID("Ranger")): {"aim": 2},
	("Engineer", 4, UPGRADE_TO_ID("Will to Survive")): {"will": 3},
	("Engineer", 6, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 3, "will": 3, "mobility": 1},

	# Pathfinder
	("Pathfinder", 1, UPGRADE_TO_ID("Hit and Run")): {"mobility": 1},
	("Pathfinder", 2, UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
	("Pathfinder", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

	# Jaeger
	("Jaeger", 3, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Jaeger", 4, UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
	("Jaeger", 5, UPGRADE_TO_ID("Damage Control")): {"will": 2},
	("Jaeger", 6, UPGRADE_TO_ID("Repair Servos")): {"will": 2},
	("Jaeger", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

	# Valkyrie
	("Valkyrie", 2, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Valkyrie", 3, UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
	("Valkyrie", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

	# Marauder
	("Marauder", 1, UPGRADE_TO_ID("Close Encounters")): {"mobility": 1},
	("Marauder", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Marauder", 4, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Marauder", 4, UPGRADE_TO_ID("Executioner")): {"aim": 2},
	("Marauder", 5, UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
	("Marauder", 6, UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
	("Marauder", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

	# Goliath
	("Goliath", 1, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
	("Goliath", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Goliath", 2, UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
	("Goliath", 3, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Goliath", 4, UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
	("Goliath", 7, UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

	# Archer
	("Archer", 2, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Archer", 3, UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
	("Archer", 4, UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
	("Archer", 6, UPGRADE_TO_ID("Damage Control")): {"aim": 3},
	("Archer", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

	# Guardian
	("Guardian", 2, UPGRADE_TO_ID("Steadfast")): {"will": 5},
	("Guardian", 3, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Guardian", 5, UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
	("Guardian", 6, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
	("Guardian", 7, UPGRADE_TO_ID("Ready for Anything")): {"aim": 2, "will": 2},

	# Shogun
	("Shogun", 3, UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
	("Shogun", 7, UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
}
