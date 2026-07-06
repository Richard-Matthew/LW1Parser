# https://www.ufopaedia.org/Dev_Console_(Long_War)#Perks
# And formatted with Copilot
UPGRADE_MAP = {
	0: "0th Upgrade item",
	1: "So Shall You Fight",
	2: "Precision Shot",
	3: "Squadsight",
	4: "Secondary Heart",
	5: "Low Profile",
	6: "Run & Gun",
	7: "Autopsy Required",
	8: "Battle Scanner",
	9: "Disabling Shot",
	10: "Opportunist",
	11: "Executioner",
	12: "Officer",  # Command?
	13: "Double Tap",
	14: "In the Zone",
	15: "Damn Good Ground",
	16: "Snapshot",
	17: "Will to Survive",
	18: "Fire Rocket",
	19: "Holo-Targeting",
	20: "Adrenal Neurosympathy",
	21: "Suppression",
	22: "Shredder Ammo",
	23: "Rapid Reaction",
	24: "Grenadier",
	25: "Danger Zone",
	26: "Ready for Anything",
	27: "Extra Conditioning",
	28: "Neural Damping",
	29: "Neural Feedback",
	30: "Hyper-Reactive Pupils",
	31: "Sprinter",
	32: "Aggression",
	33: "Tactical Sense",
	34: "Close Encounters",
	35: "Lightning Reflexes",
	36: "Rapid Fire",
	37: "Flush",
	38: "Depth Perception",
	39: "Bring 'Em On",
	40: "Close Combat Specialist",
	41: "Killer Instinct",
	42: "Bioelectric Skin",
	43: "Resilience",
	44: "Smoke Grenade",
	45: "Adaptive Bone Marrow",
	46: "Random Subclass",
	47: "Covering Fire",
	48: "Field Medic",
	49: "Pyrokinesis",
	50: "Muscle Fiber Density",
	51: "Combat Drugs",
	52: "Dense Smoke",
	53: "Packmaster",
	54: "Sentinel",
	55: "Savior",
	56: "Revive",
	57: "Elevated Ground",
	58: "Lock N' Load",
	59: "Sapper",
	60: "Suppressed",
	61: "Critically Wounded",
	62: "Airborne",
	63: "Stealth",
	64: "HEAT Warheads",
	65: "Combat Stimmed",
	66: "Javelin Rockets",
	67: "Panicked",
	68: "Mindfray",
	69: "Psi Panic",
	70: "Psi Inspiration",
	71: "Mind Control",
	72: "Telekinetic Field",
	73: "Rift",
	74: "Mind Merge (active)",
	75: "Mind Merge (passive)",
	76: "Hardened",
	77: "Greater Mind Merge (active)",
	78: "Greater Mind Merge (passive)",
	79: "Evasion",
	80: "Launch",
	81: "Bombard",
	82: "Leap",
	83: "Acid Spit",
	84: "Venomous Claws",
	85: "Blood Call",
	86: "Intimidate",
	87: "Fallen Comrades",
	88: "Bloodlust",
	89: "Bullrush",
	90: "HEAT Ammo",
	91: "Smoke & Mirrors",
	92: "Shock & Awe",
	93: "Mayhem",
	94: "Ranger",
	95: "Concealment",
	96: "Cluster Bomb",
	97: "Psi Lance",
	98: "Death Blossom",
	99: "Overload",
	100: "Psi Control",
	101: "Psi Drain",
	102: "Repair",
	103: "Cannon Fire",
	104: "Implant",
	105: "Chryssalid Spawn",
	106: "Battle Fatigue",
	107: "Range Bonus",
	108: "Range Penalty",
	109: "Scope (Foundry)",
	110: "Pistol I (Foundry)",
	111: "Pistol II (Foundry)",
	112: "Tandem Warheads",
	113: "Ammo Conservation",
	114: "Fire In the Hole",
	115: "Arc Thrower (Foundry)",
	116: "Deadeye",
	117: "Drone Capture",
	118: "Field Repairs",
	119: "Psychokinetic Strike",
	120: "Jellied Elerium",  # eFoundry_EleriumFuel
	121: "MEC Close Combat",
	122: "Stay Frosty",
	123: "Shaped Armor",
	124: "Sentinel Module",
	125: "Alien Grenades",
	126: "Light 'Em Up",
	127: "Stealth (Seeker)",
	128: "Ghost Mode",
	129: "Reaper Rounds",
	130: "Disoriented",
	131: "Collateral Damage",
	132: "Automated Threat Assessment",
	133: "Advanced Fire Control",
	134: "Damage Control",
	135: "Vital Point Targeting",
	136: "One For All",
	137: "Jetboot Module",
	138: "Combined Arms",
	139: "Repair Servos",
	140: "Fortiores Una",
	141: "Platform Stability",
	142: "Absorption Fields",
	143: "Shock-Absorbent Armor",
	144: "Reactive Targeting Sensors",
	145: "Body Shield",
	146: "Distortion Field",
	147: "Adrenaline Surge",
	148: "Iron Skin",
	149: "Regen Biofield",
	150: "Field Surgeon",
	151: "EXALT Comm Hack",
	152: "Semper Vigilans",
	153: "Sharpshooter",
	154: "Steadfast",
	155: "Smart Macrophages",
	156: "Legio Patria Nostra",
	157: "Band of Warriors",
	158: "So Others May Live",
	159: "Lone Wolf",
	160: "Esprit de Corps",
	161: "Into the Breach",
	162: "Paramedic",
	163: "Aiming Angles (bonus)",
	164: "Catching Breath",
	165: "Tactical Rigging",
	166: "Strangle",
	167: "Hit and Run",
	168: "Psi Shield",
	169: "Electropulsed",
	170: "Nearby Officer",
	171: "Lead By Example",
	172: "None",
}

UPGRADE_MAP_REVERSE = {v: k for k, v in UPGRADE_MAP.items()}

def UPGRADE_TO_ID(name: str) -> int:
    return UPGRADE_MAP_REVERSE[name]

CLASS_MAP = {
	"eSC_Sniper": "Scout-Sniper",
	"eSC_Assault": "Tactical",
	"eSC_HeavyWeapons": "Weapons",
	"eSC_Support": "Support",
	"eSC_None": "Rookie"
}

CLASS_TYPES = {
    "Unranked": CLASS_MAP.values(),
    "Biological": [
        "Scout", "Sniper",
        "Infantry", "Assault",
        "Gunner", "Rocketeer",
        "Medic", "Engineer"
	],
    "MEC": [
        "Pathfinder", "Jaeger",
        "Valkyrie", "Marauder",
        "Goliath", "Archer",
        "Guardian", "Shogun"
	],
}

RANK_MAP = {
    0: "Rookie",
    1: "Specialist",
    2: "Lance Corporal",
    3: "Corporal",
    4: "Sergeant",
    5: "Tech Sergeant",
    6: "Gunnery Sergeant",
    7: "Master Sergeant"
}

MEDAL_MAP = {
	0: "0th officer medal",
	1: "Lieutenant",
	2: "Captain",
	3: "Major",
	4: "Colonel",
	5: "Field Commander",
}

PSI_RANK_MAP = {
    1: "Awakened",
    2: "Sensitive",
    3: "Talent",
    4: "Adept",
    5: "Psion",
    6: "Master",
}

OFFICER_PERK_MAP = {
    1: "So Shall You Fight",
    12: "Officer",
    122: "Stay Frosty",
    138: "Combined Arms",  # Only at Field Commander
    140: "Fortiores Una",
    152: "Semper Vigilans",
    156: "Legio Patria Nostra",
	157: "Band of Warriors",
	158: "So Others May Live",
    160: "Esprit de Corps",
	161: "Into the Breach",
}

PSI_PERK_MAP = {
    29: "Neural Feedback",
    49: "Pyrokinesis",
    68: "Mindfray",
    69: "Psi Panic",
	70: "Psi Inspiration",
	71: "Mind Control",
	72: "Telekinetic Field",
	73: "Rift",
    74: "Mind Merge (active)",
	75: "Mind Merge (passive)",
    77: "Greater Mind Merge (active)",
	78: "Greater Mind Merge (passive)",
    97: "Psi Lance",
    100: "Psi Control",
    101: "Psi Drain",
    119: "Psychokinetic Strike",
    146: "Distortion Field",
    149: "Regen Biofield",
    168: "Psi Shield",
}

GENE_MAP = {
    4: "Secondary Heart",
    20: "Adrenal Neurosympathy",
    28: "Neural Damping",
    30: "Hyper-Reactive Pupils",
    38: "Depth Perception",
    42: "Bioelectric Skin",
    45: "Adaptive Bone Marrow",
    50: "Muscle Fiber Density",
    147: "Adrenaline Surge",  # EXALT only
	148: "Iron Skin",
    155: "Smart Macrophages",  # EXALT only
}

PERK_MAP = {
    2: "Precision Shot",
	3: "Squadsight",
    5: "Low Profile",
	6: "Run & Gun",
    8: "Battle Scanner",
	9: "Disabling Shot",
	10: "Opportunist",
	11: "Executioner",
    13: "Double Tap",
	14: "In the Zone",
	15: "Damn Good Ground",
	16: "Snapshot",
	17: "Will to Survive",
	18: "Fire Rocket",
	19: "Holo-Targeting",
    21: "Suppression",
	22: "Shredder Ammo",
	23: "Rapid Reaction",
	24: "Grenadier",
	25: "Danger Zone",
	26: "Ready for Anything",
	27: "Extra Conditioning",
    31: "Sprinter",
	32: "Aggression",
	33: "Tactical Sense",
	34: "Close Encounters",
	35: "Lightning Reflexes",
	36: "Rapid Fire",
	37: "Flush",
    39: "Bring 'Em On",
	40: "Close Combat Specialist",
	41: "Killer Instinct",
    43: "Resilience",
	44: "Smoke Grenade",
    47: "Covering Fire",
	48: "Field Medic",
    51: "Combat Drugs",
	52: "Dense Smoke",
	53: "Packmaster",
	54: "Sentinel",
	55: "Savior",
	56: "Revive",
    58: "Lock N' Load",
	59: "Sapper",
    61: "Critically Wounded",
    64: "HEAT Warheads",
    66: "Javelin Rockets",
    76: "Hardened",
    80: "Launch",
    81: "Bombard",
    82: "Leap",
    83: "Acid Spit",
	84: "Venomous Claws",
	85: "Blood Call",
	86: "Intimidate",
    88: "Bloodlust",
	89: "Bullrush",
	90: "HEAT Ammo",
	91: "Smoke & Mirrors",
	92: "Shock & Awe",
	93: "Mayhem",
	94: "Ranger",
    95: "Concealment",
	96: "Cluster Bomb",
    98: "Death Blossom",
	99: "Overload",
    102: "Repair",
    103: "Cannon Fire",
	104: "Implant",
    112: "Tandem Warheads",
    114: "Fire In the Hole",
    116: "Deadeye",
    121: "MEC Close Combat",
    126: "Light 'Em Up",
	127: "Stealth (Seeker)",  # Unlimited Cloak ability?
    131: "Collateral Damage",
	132: "Automated Threat Assessment",
	133: "Advanced Fire Control",
	134: "Damage Control",
	135: "Vital Point Targeting",
    136: "One For All",
    139: "Repair Servos",
    141: "Platform Stability",
	142: "Absorption Fields",
	143: "Shock-Absorbent Armor",
	144: "Reactive Targeting Sensors",
    150: "Field Surgeon",
    153: "Sharpshooter",
	154: "Steadfast",
    159: "Lone Wolf",
    162: "Paramedic",
    166: "Strangle",
    167: "Hit and Run",
}

# Perks granted by foundry research
FOUNDRY_PERK_MAP = {
    109: "Scope (Foundry)",
	110: "Pistol I (Foundry)",
	111: "Pistol II (Foundry)",
    113: "Ammo Conservation",
    115: "Arc Thrower (Foundry)",
    117: "Drone Capture",
    118: "Field Repairs",
    120: "Jellied Elerium",  # eFoundry_EleriumFuel
    123: "Shaped Armor",
    124: "Sentinel Module",  # ePerk_Foundry_SentinelDrone
    125: "Alien Grenades",  # ePerk_Foundry_AlienGrenades
    165: "Tactical Rigging",
}

# Perks that should only be present in Tactical layer
COMBAT_MAP = {
    57: "Elevated Ground",
    60: "Suppressed",
    62: "Airborne",
	63: "Stealth",
    65: "Combat Stimmed",
    67: "Panicked",
    87: "Fallen Comrades",
    105: "Chryssalid Spawn",
	106: "Battle Fatigue",
    107: "Range Bonus",
	108: "Range Penalty",
    128: "Ghost Mode",
    130: "Disoriented",
    151: "EXALT Comm Hack",
    164: "Catching Breath",  # Seeker choke recovery
    169: "Electropulsed",  # Caused by MEC Electro Pulse equipment
    170: "Nearby Officer",
    171: "Lead By Example",
}

# Perks that don't fit in the above categories
# Or which I don't know what they are in-game
MISC_MAP = {
	0: "Upgrade[0] is None",  # Upgrade array is 1-indexed?
    46: "Random Subclass",
    79: "Evasion", # ???
    129: "Reaper Rounds",  # From Reaper Pack equipment
    137: "Jetboot Module",  # From the MEC suit
    145: "Body Shield",  # From the MEC suit
    163: "Aiming Angles (bonus)",  # Second Wave
    172: "Upgrade[172] is None", # Placeholder?
}

# Foundry items in m_arrFoundryHistory
FOUNDRY_UNLOCK_MAP = {
    0: "0th Foundry item",  			# eFoundry_None
    1: "Enhanced Ballistics",  			# eFoundry_SHIV
    2: "Alien Grenades",  				# eFoundry_AlienGrenades
    3: "Improved Medikit",  			# eFoundry_MedikitII
    4: "Improved Arc Thrower",  		# eFoundry_ArcThrowerII
    5: "Advanced Repair",  				# eFoundry_VehicleRepair
    6: "Enhanced Lasers",  				# eFoundry_AutomatedLasers
    7: "Enhanced Plasma",  				# eFoundry_AutomatedPlasma
    8: "Field Repairs",  				# eFoundry_SHIV_Heal
    9: "Drone Capture",  				# eFoundry_CaptureDrone
    10: "Ammo Conservation",  			# eFoundry_AmmoConservation
    11: "Advanced Flight",  			# eFoundry_AdvancedFlight
    12: "Armored Fighters",  			# eFoundry_AdvancedConstruction
    13: "Mag Pistols",  				# eFoundry_PistolI
    14: "Rail Pistols",  				# eFoundry_PistolII
    15: "Reflex Pistols",  				# eFoundry_PistolIII
    16: "Shiv Suppression",  			# eFoundry_SHIVSuppression
    17: "Stealth Satellites",  			# eFoundry_StealthSatellites
    18: "SCOPE Upgrade",  				# eFoundry_Scope
    19: "Jellied Elerium",  			# eFoundry_EleriumFuel
    20: "MEC Close Combat",  			# eFoundry_MECCloseCombat
    21: "Advanced Servomotors",  		# eFoundry_AdvancedServomotors
    22: "Shaped Armor",  				# eFoundry_ShapedArmor
    23: "Sentinel Drone",  				# eFoundry_SentinelDrone
    24: "Tactical Rigging",  			# eFoundry_TacticalRigging
    25: "Alien Metallurgy",  			# eMPMECSTT_MECSuitTemplate8
    26: "Aircraft Boosters",  			# eMPT_MECTemplate1
    27: "Wingtip Sparrowhawks",  		# eMPT_MECTemplate2
    28: "Penetrator Weapons",  			# eMPT_MECTemplate3
    29: "Mechanized Unit Defense",  	# eMPT_MECTemplate4
    30: "Advanced Surgery",  			# eMPT_MECTemplate5
    31: "Improved Avionics",  			# eMPT_MECTemplate6
    32: "UFO Countermeasures",  		# eMPT_MECTemplate7
    33: "Elerium Afterburners",  		# eMPT_MECTemplate8
    34: "Supercapacitors",  			# eMPMECSTT_MECSuitTemplate1
    35: "UFO Tracking",  				# eMPMECSTT_MECSuitTemplate2
    36: "MEC Warfare Systems",  		# eMPMECSTT_MECSuitTemplate3
    37: "Super Skyranger",  			# eMPMECSTT_MECSuitTemplate4
    38: "Alien Nucleonics",  			# eMPMECSTT_MECSuitTemplate5
    39: "Improved Salvage",  			# eMPMECSTT_MECSuitTemplate6
    40: "New Combat Systems",  			# eMPMECSTT_MECSuitTemplate7
    41: "Psi Warfare Systems",  		# eMPMECSTT_MECSuitTemplate8
    42: "Security Training: Weapons",	# eMPMECSTT_MECSuitTemplate8_1
    43: "Security Training: Armor",  	# eMPMECSTT_MECSuitTemplate8_2
    44: "Phoenix Coilguns",  			# eMPMECSTT_MECSuitTemplate8_3
    45: "UFO Scanners",  				# eMPMECSTT_MECSuitTemplate8_4
    46: "Quenchguns",  					# eFoundry_MAX
}

# Research items in m_arrResearched
RESEARCH_UNLOCK_MAP = {
    0: "eTech_None",  					# eTech_None
    1: "Xenobiology",  					# eTech_Xenobiology
    2: "Xenoneurology",  				# eTech_ArcThrower
    3: "Alien Operations",  			# eTech_BaseShard
    4: "Xenopsionics",  				# eTech_PsiLabs
    5: "Alien Propulsion",  			# eTech_Firestorm
    6: "Sectoid Commander Autopsy",  	# eTech_AutopsySectoidCommander
    7: "Alien Communications",  		# eTech_Hyperwave
    8: "Alien Command and Control",  	# eTech_PsiLink
    9: "Alien Weaponry",  				# eTech_WeaponFragments
    10: "Alien Materials",  			# eTech_AlienMaterials
    11: "Experimental Warfare",  		# eTech_Exp_Warfare
    12: "Elerium",  					# eTech_Elerium
    13: "Xenogenetics",  				# eTech_Meld
    14: "Mind And Machine",  			# eTech_PsiArmor
    15: "Advanced Body Armor",  		# eTech_Armor_Carapace
    16: "Mobile Power Armor",  			# eTech_Armor_Skeleton
    17: "Advanced Power Armor",  		# eTech_Armor_Titan
    18: "Stealth Systems",  			# eTech_Armor_Ghost
    19: "Antigrav Systems",  			# eTech_Armor_ArchAngel
    20: "Beam Lasers",  				# eTech_LaserWeapons
    21: "Advanced Beam Lasers",  		# eTech_PrecisionLasers
    22: "Pulse Lasers",  				# eTech_HeavyLasers
    23: "Compact Plasma Weapons",  		# eTech_Plasma_Pistol
    24: "Plasma Weapons",  				# eTech_Plasma_Light
    25: "Advanced Plasma Weapons",  	# eTech_Plasma_Rifle
    26: "Heavy Plasma Weapons",  		# eTech_Plasma_Heavy
    27: "Precision Plasma Weapons",  	# eTech_Plasma_Sniper
    28: "Gauss Weapons",  				# eTech_Alloy_Cannon
    29: "Vehicular Plasma Weapons",  	# eTech_Plasma_Cannon
    30: "Fusion Weapons",  				# eTech_Fusion_Launcher
    31: "Advanced Gauss Weapons",  		# eTech_BlasterLauncher
    32: "Alien Computers",  			# eTech_AlienNavigation
    33: "Alien Power Systems",  		# eTech_UFOPowerSource
    34: "Electromagnetic Pulse Weapons",# eTech_EMP
    35: "Interrogate Sectoid",  		# eTech_InterrogateSectoid
    36: "Interrogate Floater",  		# eTech_InterrogateFloater
    37: "Interrogate Muton",  			# eTech_InterrogateMuton
    38: "Interrogate Sectoid Commander",# eTech_InterrogateSectoidCommander
    39: "Interrogate Berserker",  		# eTech_InterrogateBerserker
    40: "Interrogate Thin Man",  		# eTech_InterrogateThinMan
    41: "Interrogate Heavy Floater",  	# eTech_InterrogateHeavyFloater
    42: "Interrogate Muton Elite",  	# eTech_InterrogateMutonElite
    43: "Interrogate Ethereal",  		# eTech_InterrogateEthereal
    44: "Sectoid Autopsy",  			# eTech_AutopsySectoid
    45: "Floater Autopsy",  			# eTech_AutopsyFloater
    46: "Thin Man Autopsy",  			# eTech_AutopsyThinMan
    47: "Muton Autopsy",  				# eTech_AutopsyMuton
    48: "Chryssalid Autopsy",  			# eTech_AutopsyCryssalid
    49: "Advanced Pulse Lasers",  		# eTech_AutopsyZombie
    50: "Cyberdisc Autopsy",  			# eTech_AutopsyCyberdisc
    51: "Berserker Autopsy",  			# eTech_AutopsyBerserker
    52: "Heavy Floater Autopsy",  		# eTech_AutopsyHeavyFloater
    53: "Muton Elite Autopsy",  		# eTech_AutopsyMutonElite
    54: "Drone Autopsy",  				# eTech_AutopsyDrone
    55: "Sectopod Autopsy",  			# eTech_AutopsySectopod
    56: "Ethereal Autopsy",  			# eTech_AutopsyEthereal
    57: "Mechtoid Autopsy",  			# eTech_AutopsyMechtoid
    58: "Seeker Autopsy",  				# eTech_AutopsySeeker
    59: "Advanced Aerospace Concepts",  # eTech_Autopsy_END
    60: "eTech_Placeholder",  			# eTech_Placeholder
    61: "UFO Analysis: Scout",  		# eTech_Placeholder_1
    62: "UFO Analysis: Destroyer",  	# eTech_Placeholder_2
    63: "UFO Analysis: Abductor",  		# eTech_Placeholder_3
    64: "UFO Analysis: Transport",  	# eTech_Placeholder_4
    65: "UFO Analysis: Battleship",  	# eTech_Placeholder_5
    66: "UFO Analysis: Overseer",  		# eTech_Placeholder_6
    67: "UFO Analysis: Fighter",  		# eTech_Placeholder_7
    68: "UFO Analysis: Raider",  		# eTech_Placeholder_8
    69: "UFO Analysis: Harvester",  	# eTech_Placeholder_9
    70: "UFO Analysis: Terror Ship",  	# eTech_Placeholder_10
    71: "UFO Analysis: Assault Carrier",# eTech_Placeholder_11
    72: "Improved Body Armor",  		# eTech_Placeholder_12
    73: "Improved Combat Exoskeletons", # eTech_Placeholder_13
    74: "Mobile Combat Exoskeletons",  	# eTech_Placeholder_14
    75: "Heavy Combat Exoskeletons",  	# eTech_Placeholder_15
    76: "eTech_MAX",  					# eTech_MAX
}

