SUPRA_CLASSES = {
	"eSC_Sniper": "Scout-Sniper",
	"eSC_Assault": "Tactical",
	"eSC_HeavyWeapons": "Weapons",
	"eSC_Support": "Support",
	"eSC_None": "Rookie"
}

CLASS_TYPES = {
    "Unranked": SUPRA_CLASSES.values(),
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
