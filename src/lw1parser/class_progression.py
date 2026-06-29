from lw1parser import maps

CLASS_PERKS = {
    # Biological
    "Scout": {
        1: [
            maps.UPGRADE_TO_ID("Lightning Reflexes")
        ],
        2: [
            maps.UPGRADE_TO_ID("Holo-Targeting"),
            maps.UPGRADE_TO_ID("Damn Good Ground"),
            maps.UPGRADE_TO_ID("Lone Wolf")
        ],
        3: [
            maps.UPGRADE_TO_ID("Low Profile"),
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Deadeye")
        ],
        4: [
            maps.UPGRADE_TO_ID("Flush"),
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Battle Scanner")
        ],
        5: [
            maps.UPGRADE_TO_ID("Concealment"),
            maps.UPGRADE_TO_ID("In the Zone"),
            maps.UPGRADE_TO_ID("Hit and Run")
        ],
        6: [
            maps.UPGRADE_TO_ID("Tactical Sense"),
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Sprinter")
        ],
        7: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Smoke & Mirrors")
        ],
    },

    "Sniper": {
        1: [
            maps.UPGRADE_TO_ID("Squadsight"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Low Profile"),
            maps.UPGRADE_TO_ID("Deadeye"),
            maps.UPGRADE_TO_ID("Lone Wolf"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Disabling Shot"),
            maps.UPGRADE_TO_ID("Precision Shot"),
            maps.UPGRADE_TO_ID("Snapshot"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Damn Good Ground"),
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Sharpshooter"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Executioner"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Platform Stability"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Tactical Sense"),
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Lock N' Load"),
        ],
        7: [
            maps.UPGRADE_TO_ID("In the Zone"),
            maps.UPGRADE_TO_ID("Mayhem"),
            maps.UPGRADE_TO_ID("Double Tap"),
        ],
    },

    "Infantry": {
        1: [
            maps.UPGRADE_TO_ID("Light 'Em Up"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Covering Fire"),
            maps.UPGRADE_TO_ID("Executioner"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Will to Survive"),
            maps.UPGRADE_TO_ID("Opportunist"),
            maps.UPGRADE_TO_ID("Aggression"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Deadeye"),
            maps.UPGRADE_TO_ID("Suppression"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Tactical Sense"),
            maps.UPGRADE_TO_ID("Lock N' Load"),
            maps.UPGRADE_TO_ID("Sharpshooter"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Resilience"),
            maps.UPGRADE_TO_ID("Sentinel"),
            maps.UPGRADE_TO_ID("Bring 'Em On"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
        ],
    },

    "Assault": {
        1: [
            maps.UPGRADE_TO_ID("Run & Gun"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Close Combat Specialist"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Will to Survive"),
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Close Encounters"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Hit and Run"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Resilience"),
            maps.UPGRADE_TO_ID("Killer Instinct"),
            maps.UPGRADE_TO_ID("Executioner"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Tactical Sense"),
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Sprinter"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Lightning Reflexes"),
        ],
    },

    "Gunner": {
        1: [
            maps.UPGRADE_TO_ID("Suppression"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Flush"),
            maps.UPGRADE_TO_ID("Covering Fire"),
            maps.UPGRADE_TO_ID("Holo-Targeting"),
        ],
        3: [
            maps.UPGRADE_TO_ID("HEAT Ammo"),
            maps.UPGRADE_TO_ID("Opportunist"),
            maps.UPGRADE_TO_ID("Shredder Ammo"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Will to Survive"),
            maps.UPGRADE_TO_ID("Executioner"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Ready for Anything"),
            maps.UPGRADE_TO_ID("Double Tap"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Resilience"),
            maps.UPGRADE_TO_ID("Platform Stability"),
            maps.UPGRADE_TO_ID("Danger Zone"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Sentinel"),
            maps.UPGRADE_TO_ID("Mayhem"),
        ],
    },

    "Rocketeer": {
        1: [
            maps.UPGRADE_TO_ID("Fire Rocket"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Will to Survive"),
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("HEAT Warheads"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Rapid Reaction"),
            maps.UPGRADE_TO_ID("Fire In the Hole"),
            maps.UPGRADE_TO_ID("Snapshot"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Suppression"),
            maps.UPGRADE_TO_ID("Platform Stability"),
            maps.UPGRADE_TO_ID("Shredder Ammo"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Tactical Sense"),
            maps.UPGRADE_TO_ID("Opportunist"),
            maps.UPGRADE_TO_ID("Mayhem"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Double Tap"),
            maps.UPGRADE_TO_ID("Shock & Awe"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Tandem Warheads"),
            maps.UPGRADE_TO_ID("Javelin Rockets"),
            maps.UPGRADE_TO_ID("Danger Zone"),
        ],
    },

    "Medic": {
        1: [
            maps.UPGRADE_TO_ID("Field Medic"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Suppression"),
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Field Surgeon"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Rapid Reaction"),
            maps.UPGRADE_TO_ID("Smoke & Mirrors"),
            maps.UPGRADE_TO_ID("Revive"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Ready for Anything"),
            maps.UPGRADE_TO_ID("Smoke Grenade"),
            maps.UPGRADE_TO_ID("Paramedic"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Opportunist"),
            maps.UPGRADE_TO_ID("Dense Smoke"),
            maps.UPGRADE_TO_ID("Combat Drugs"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Lock N' Load"),
            maps.UPGRADE_TO_ID("Bombard"),
            maps.UPGRADE_TO_ID("Sprinter"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("Savior"),
        ],
    },

    "Engineer": {
        1: [
            maps.UPGRADE_TO_ID("Grenadier"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Holo-Targeting"),
            maps.UPGRADE_TO_ID("Smoke Grenade"),
            maps.UPGRADE_TO_ID("Sapper"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Smoke & Mirrors"),
            maps.UPGRADE_TO_ID("HEAT Warheads"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Will to Survive"),
            maps.UPGRADE_TO_ID("Repair"),
            maps.UPGRADE_TO_ID("Suppression"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Battle Scanner"),
            maps.UPGRADE_TO_ID("Dense Smoke"),
            maps.UPGRADE_TO_ID("Mayhem"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("HEAT Ammo"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Tandem Warheads"),
            maps.UPGRADE_TO_ID("Fire Rocket"),
            maps.UPGRADE_TO_ID("Bombard"),
        ],
    },

    # MEC
    "Jaeger": {
        1: [
            maps.UPGRADE_TO_ID("In the Zone"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Damn Good Ground"),
            maps.UPGRADE_TO_ID("Platform Stability"),
            maps.UPGRADE_TO_ID("Sharpshooter"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Executioner"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Lone Wolf"),
            maps.UPGRADE_TO_ID("Advanced Fire Control"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("Squadsight"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Shredder Ammo"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Lock N' Load"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
        ],
    },

    "Pathfinder": {
        1: [
            maps.UPGRADE_TO_ID("Hit and Run"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Deadeye"),
            maps.UPGRADE_TO_ID("Advanced Fire Control"),
            maps.UPGRADE_TO_ID("Lone Wolf"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Damn Good Ground"),
            maps.UPGRADE_TO_ID("Sharpshooter"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Executioner"),
            maps.UPGRADE_TO_ID("Repair Servos"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Squadsight"),
            maps.UPGRADE_TO_ID("Lock N' Load"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Lightning Reflexes"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
    },

    "Valkyrie": {
        1: [
            maps.UPGRADE_TO_ID("Light 'Em Up"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Platform Stability"),
            maps.UPGRADE_TO_ID("Reactive Targeting Sensors"),
            maps.UPGRADE_TO_ID("Rapid Reaction"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Lock N' Load"),
            maps.UPGRADE_TO_ID("HEAT Ammo"),
            maps.UPGRADE_TO_ID("Shredder Ammo"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Sharpshooter"),
            maps.UPGRADE_TO_ID("Opportunist"),
            maps.UPGRADE_TO_ID("Damage Control"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Collateral Damage"),
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Repair Servos"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
    },

    "Marauder": {
        1: [
            maps.UPGRADE_TO_ID("Close Encounters"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Aggression"),
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Shock-Absorbent Armor"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("Close Combat Specialist"),
            maps.UPGRADE_TO_ID("Collateral Damage"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Executioner"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Flush"),
            maps.UPGRADE_TO_ID("Advanced Fire Control"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Bring 'Em On"),
            maps.UPGRADE_TO_ID("Reactive Targeting Sensors"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Run & Gun"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
    },

    "Goliath": {
        1: [
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Reactive Targeting Sensors"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Covering Fire"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Mayhem"),
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Advanced Fire Control"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("Shock-Absorbent Armor"),
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
        ],
        6: [
            maps.UPGRADE_TO_ID("HEAT Ammo"),
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("Collateral Damage"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Close Combat Specialist"),
            maps.UPGRADE_TO_ID("Extra Conditioning"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
        ],
    },

    "Archer": {
        1: [
            maps.UPGRADE_TO_ID("Bombard"),
        ],
        2: [
            maps.UPGRADE_TO_ID("HEAT Warheads"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Platform Stability"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Advanced Fire Control"),
            maps.UPGRADE_TO_ID("Mayhem"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Ranger"),
            maps.UPGRADE_TO_ID("Reactive Targeting Sensors"),
            maps.UPGRADE_TO_ID("Sapper"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("Collateral Damage"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Danger Zone"),
            maps.UPGRADE_TO_ID("Double Tap"),
            maps.UPGRADE_TO_ID("Damage Control"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Grenadier"),
            maps.UPGRADE_TO_ID("Tandem Warheads"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
    },

"Guardian": {
        1: [
            maps.UPGRADE_TO_ID("Opportunist"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Field Medic"),
            maps.UPGRADE_TO_ID("Steadfast"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Platform Stability"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Covering Fire"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Sentinel"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Savior"),
            maps.UPGRADE_TO_ID("Deadeye"),
            maps.UPGRADE_TO_ID("Reactive Targeting Sensors"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Vital Point Targeting"),
            maps.UPGRADE_TO_ID("Lock N' Load"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Ready for Anything"),
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("Double Tap"),
        ],
    },

    "Shogun": {
        1: [
            maps.UPGRADE_TO_ID("Collateral Damage"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Packmaster"),
            maps.UPGRADE_TO_ID("Damage Control"),
            maps.UPGRADE_TO_ID("HEAT Ammo"),
        ],
        3: [
            maps.UPGRADE_TO_ID("HEAT Warheads"),
            maps.UPGRADE_TO_ID("Automated Threat Assessment"),
            maps.UPGRADE_TO_ID("Deadeye"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Mayhem"),
            maps.UPGRADE_TO_ID("Repair Servos"),
            maps.UPGRADE_TO_ID("Flush"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Sapper"),
            maps.UPGRADE_TO_ID("Shock-Absorbent Armor"),
            maps.UPGRADE_TO_ID("Ranger"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Tandem Warheads"),
            maps.UPGRADE_TO_ID("Rapid Fire"),
            maps.UPGRADE_TO_ID("Light 'Em Up"),
        ],
        7: [
            maps.UPGRADE_TO_ID("Grenadier"),
            maps.UPGRADE_TO_ID("Absorption Fields"),
            maps.UPGRADE_TO_ID("Shredder Ammo"),
        ],
    },

    # Special
    "Psionic": {
        1: [
            maps.UPGRADE_TO_ID("Regen Biofield"),
            maps.UPGRADE_TO_ID("Neural Feedback"),
            maps.UPGRADE_TO_ID("Mindfray"),
        ],
        2: [
            maps.UPGRADE_TO_ID("Distortion Field"),
            maps.UPGRADE_TO_ID("Psi Inspiration"),
        ],
        3: [
            maps.UPGRADE_TO_ID("Psi Panic"),
            maps.UPGRADE_TO_ID("Mind Merge (active)"),
        ],
        4: [
            maps.UPGRADE_TO_ID("Psychokinetic Strike"),
            maps.UPGRADE_TO_ID("Pyrokinesis"),
            maps.UPGRADE_TO_ID("Telekinetic Field"),
        ],
        5: [
            maps.UPGRADE_TO_ID("Mind Control"),
        ],
        6: [
            maps.UPGRADE_TO_ID("Rift"),
        ],
    },

    "Officer": {
        0: [  # All Officers get both of these perks, but Command isn't in the Upgrades array
            maps.UPGRADE_TO_ID("Lead By Example"),
            #maps.UPGRADE_TO_ID("Command"),
        ],

        1: [  # Lieutenant
            maps.UPGRADE_TO_ID("Legio Patria Nostra"),
            maps.UPGRADE_TO_ID("Stay Frosty"),
        ],

        2: [  # Captain
            maps.UPGRADE_TO_ID("Semper Vigilans"),
            maps.UPGRADE_TO_ID("Fortiores Una"),
        ],

        3: [  # Major
            maps.UPGRADE_TO_ID("Into the Breach"),
            maps.UPGRADE_TO_ID("So Shall You Fight"),
        ],

        4: [  # Colonel
            maps.UPGRADE_TO_ID("Band of Warriors"),
            maps.UPGRADE_TO_ID("Esprit de Corps"),
        ],

        5: [  # Field Commander
            maps.UPGRADE_TO_ID("So Others May Live"),
            maps.UPGRADE_TO_ID("Combined Arms"),
        ],
    },
}

PERK_STAT_BONUS = {
    # Format:
    # (ClassName, Rank, PerkID): {"StatName": modifier}

    # Scout
    ("Scout", 1, maps.UPGRADE_TO_ID("Lightning Reflexes")): {"mobility": 1},
    ("Scout", 3, maps.UPGRADE_TO_ID("Ranger")): {"aim": 1},
    ("Scout", 3, maps.UPGRADE_TO_ID("Deadeye")): {"aim": 1},
    ("Scout", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

    # Sniper
    ("Sniper", 4, maps.UPGRADE_TO_ID("Damn Good Ground")): {"will": 2},
    ("Sniper", 7, maps.UPGRADE_TO_ID("Mayhem")): {"aim": 2},

    # Infantry
    ("Infantry", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Infantry", 5, maps.UPGRADE_TO_ID("Sharpshooter")): {"aim": 2},
    ("Infantry", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

    # Assault
    ("Assault", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Assault", 3, maps.UPGRADE_TO_ID("Will to Survive")): {"will": 3},
    ("Assault", 4, maps.UPGRADE_TO_ID("Close Encounters")): {"will": 3},
    ("Assault", 5, maps.UPGRADE_TO_ID("Executioner")): {"aim": 2, "will": 5},
    ("Assault", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

    # Gunner
    ("Gunner", 2, maps.UPGRADE_TO_ID("Covering Fire")): {"aim": 2},
    ("Gunner", 4, maps.UPGRADE_TO_ID("Will to Survive")): {"will": 3},
    ("Gunner", 5, maps.UPGRADE_TO_ID("Ready for Anything")): {"aim": 2},
    ("Gunner", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

    # Rocketeer
    ("Rocketeer", 2, maps.UPGRADE_TO_ID("Will to Survive")): {"will": 3},
    ("Rocketeer", 3, maps.UPGRADE_TO_ID("Rapid Reaction")): {"aim": 2},
    ("Rocketeer", 6, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 3, "will": 3, "mobility": 1},

    # Medic
    ("Medic", 1, maps.UPGRADE_TO_ID("Field Medic")): {"mobility": 1},
    ("Medic", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Medic", 3, maps.UPGRADE_TO_ID("Rapid Reaction")): {"aim": 3},
    ("Medic", 3, maps.UPGRADE_TO_ID("Revive")): {"will": 2},
    ("Medic", 4, maps.UPGRADE_TO_ID("Ready for Anything")): {"will": 3},
    ("Medic", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 1},

    # Engineer
    ("Engineer", 2, maps.UPGRADE_TO_ID("Holo-Targeting")): {"aim": 1},
    ("Engineer", 3, maps.UPGRADE_TO_ID("Ranger")): {"aim": 2},
    ("Engineer", 4, maps.UPGRADE_TO_ID("Will to Survive")): {"will": 3},
    ("Engineer", 6, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 3, "will": 3, "mobility": 1},

    # Pathfinder
    ("Pathfinder", 1, maps.UPGRADE_TO_ID("Hit and Run")): {"mobility": 1},
    ("Pathfinder", 2, maps.UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
    ("Pathfinder", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

    # Jaeger
    ("Jaeger", 3, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 3},
    ("Jaeger", 4, maps.UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
    ("Jaeger", 5, maps.UPGRADE_TO_ID("Damage Control")): {"will": 2},
    ("Jaeger", 6, maps.UPGRADE_TO_ID("Repair Servos")): {"will": 2},
    ("Jaeger", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

    # Valkyrie
    ("Valkyrie", 2, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Valkyrie", 3, maps.UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
    ("Valkyrie", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

    # Marauder
    ("Marauder", 1, maps.UPGRADE_TO_ID("Close Encounters")): {"mobility": 1},
    ("Marauder", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Marauder", 4, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Marauder", 4, maps.UPGRADE_TO_ID("Executioner")): {"aim": 2},
    ("Marauder", 5, maps.UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
    ("Marauder", 6, maps.UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
    ("Marauder", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

    # Goliath
    ("Goliath", 1, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
    ("Goliath", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Goliath", 2, maps.UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
    ("Goliath", 3, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Goliath", 4, maps.UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
    ("Goliath", 7, maps.UPGRADE_TO_ID("Extra Conditioning")): {"aim": 4, "will": 4, "mobility": 4},

    # Archer
    ("Archer", 2, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Archer", 3, maps.UPGRADE_TO_ID("Advanced Fire Control")): {"aim": 2},
    ("Archer", 4, maps.UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
    ("Archer", 6, maps.UPGRADE_TO_ID("Damage Control")): {"aim": 3},
    ("Archer", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},

    # Guardian
    ("Guardian", 2, maps.UPGRADE_TO_ID("Steadfast")): {"will": 5},
    ("Guardian", 3, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Guardian", 5, maps.UPGRADE_TO_ID("Reactive Targeting Sensors")): {"aim": 2, "will": 2},
    ("Guardian", 6, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
    ("Guardian", 7, maps.UPGRADE_TO_ID("Ready for Anything")): {"aim": 2, "will": 2},

    # Shogun
    ("Shogun", 3, maps.UPGRADE_TO_ID("Automated Threat Assessment")): {"will": 2},
    ("Shogun", 7, maps.UPGRADE_TO_ID("Absorption Fields")): {"mobility": -1},
}
