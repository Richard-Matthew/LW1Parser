from lw1parser import maps
from lw1parser import class_progression
from lw1parser.unit import Unit
from .properties import _PropertyUtils

class _UnitParser:
    @staticmethod
    def build_units(checkpoint_table):
        units = []

        # List comprehension
        unit_entries = [
            entry for entry in checkpoint_table
            if entry.get("name", "").startswith("Command1.TheWorld:PersistentLevel.XGStrategySoldier_")
        ]
        
        for entry in unit_entries:          
            # Convert nested mixed structured into nested dict
            unit_dict = _PropertyUtils.properties_array_to_dict(entry.get("properties", []))
            
            # Extract m_kSoldier dict for convinience
            soldier_dict = unit_dict.get("m_kSoldier", {})

            # Get stats array from m_kChar properties.aStats int_values
			# A unit without stats means an issue with reading the save or save corruption
            stats = unit_dict.get("m_kChar", {}).get("aStats")
            if not stats:
                continue
            
            ingame_class = _PropertyUtils._parse_class(unit_dict)
            perks = _UnitParser._get_class_perk_list(unit_dict)

            units.append(Unit(
                ingame_id     = soldier_dict.get("iID"),

                first_name    = soldier_dict.get("strFirstName", ""),
                last_name     = soldier_dict.get("strLastName", ""),
                nick_name     = soldier_dict.get("strNickName", ""),

                rank          = soldier_dict.get("iRank", 0),
                special_rank  = soldier_dict.get("iPsiRank", 0),
                xp            = soldier_dict.get("iXP", 0),
                psi_xp        = soldier_dict.get("iPsiXP", 0),
                kills         = soldier_dict.get("iNumKills", 0),
                kia_date      = unit_dict.get("m_strKIADate", ""),

                class_perks   = perks["class_perks"],
                officer_perks = perks["officer_perks"],
                psi_perks     = perks["psi_perks"],
                gene_perks    = perks["gene_perks"],
                bonus_perks   = perks["bonus_perks"],

                hp            = stats[0],
                aim           = stats[1],
                mobility      = stats[3],
                willpower     = stats[7],
                defense       = stats[2],

                soml_mission_count = stats[6],

                ingame_class  = ingame_class,
                special       = _UnitParser._get_special(unit_dict)
            ))

        return units

    def _get_class_perk_list(unit_dict: dict) -> dict:
        """
        Takes a unit dict and returns a dict of categorized and ordered perk dicts.
        """
        # Get dict of perks
        perk_dict = _PropertyUtils._parse_mapped_array(
            unit_dict.get("m_kChar", {}).get("aUpgrades", []), # Perk flags
            maps.UPGRADE_MAP,
            True
        )

        # Get unit class
        unit_class = _PropertyUtils._parse_class(unit_dict)

        # Get the possible perks for the unit's class
        progression = class_progression.CLASS_PERKS.get(unit_class, {})

        class_perk_ids = {
            perk_id
            for rank_perks in progression.values()
            for perk_id in rank_perks
        }

        bonus_perks   = {}
        officer_perks = {}
        psi_perks     = {}
        gene_perks    = {}
        class_perks   = {}

        for perk_id in perk_dict:
            perk_name = perk_dict[perk_id]

            # MECs get Combined Arms but cannot be Officers
            if perk_id in maps.OFFICER_PERK_MAP and unit_class not in maps.CLASS_TYPES.get("MEC"):
                officer_perks[perk_id] = perk_name

            elif perk_id in maps.PSI_PERK_MAP:
                psi_perks[perk_id] = perk_name

            elif perk_id in maps.GENE_MAP:
                gene_perks[perk_id] = perk_name

            elif perk_id in class_perk_ids:
                class_perks[perk_id] = perk_name

            elif perk_id in maps.PERK_MAP:
                bonus_perks[perk_id] = perk_name

        officer_progression = class_progression.CLASS_PERKS.get("Officer", {})
        ordered_officer = {
            perk_id: officer_perks[perk_id]
            for rank in sorted(officer_progression.keys())
            for perk_id in officer_progression[rank]
            if perk_id in officer_perks
        }

        psi_progression = class_progression.CLASS_PERKS.get("Psionic", {})
        ordered_psi = {
            perk_id: psi_perks[perk_id]
            for rank in sorted(psi_progression.keys())
            for perk_id in psi_progression[rank]
            if perk_id in psi_perks
        }

        # Gene mods don't have an ordered tree
        ordered_gene = {
            perk_id: gene_perks[perk_id]
            for perk_id in sorted(gene_perks, key=lambda pid: gene_perks[pid])
        }


        ordered_class = {
            perk_id: class_perks[perk_id]
            for rank in sorted(progression.keys())
            for perk_id in progression[rank]
            if perk_id in class_perks
        }

        return {
            "bonus_perks":   bonus_perks,
            "officer_perks": ordered_officer,
            "psi_perks":     ordered_psi,
            "gene_perks":    ordered_gene,
            "class_perks":   ordered_class,
        }
    
    def _get_special(unit_dict: dict) -> str:
        """
        Returns Officer rank, Psion rank, MEC, or an empty string.
        """

        # Officer
        medals = unit_dict.get("m_arrMedals", [])
        medal_dict = _PropertyUtils._parse_mapped_array(
            medals,
            maps.MEDAL_MAP,
            False
        )

        if medal_dict:
            # Highest medal_id determines officer rank
            highest_medal_id = max(medal_dict.keys())
            officer_rank_name = maps.MEDAL_MAP.get(highest_medal_id, None)

            if officer_rank_name:
                return officer_rank_name

        # Psion
        psi_rank = unit_dict.get("m_kSoldier", {}).get("iPsiRank", 0)

        if psi_rank > 0:
            psi_rank_name = maps.PSI_RANK_MAP.get(psi_rank, None)
            if psi_rank_name:
                return psi_rank_name
            else:
                return "Psion"

        # MEC
        unit_class = _PropertyUtils._parse_class(unit_dict)

        MEC_CLASSES = {
            "Goliath", "Archer", "Shogun", "Valkyrie",
            "Marauder", "Pathfinder", "Jaeger"
        }

        if unit_class in MEC_CLASSES:
            return "MEC"

        #None
        return 

    def _get_special_rank(unit_dict: dict) -> int | None:
        """
        Return Officer rank, Psion rank, or None.
        """
        # Psion check is easy
        psi_rank = unit_dict.get("m_kSoldier", {}).get("spec_rank", 0)
        if psi_rank > 0:
            return psi_rank

        # Officer rank is highest index in medal array
        medals = unit_dict.get("m_arrMedals", [])
        medal_dict = _PropertyUtils._parse_mapped_array(
            medals,
            maps.MEDAL_MAP,
            False
        )

        officer_rank = max(medal_dict.keys()) if medal_dict else 0
        if officer_rank > 0:
            return officer_rank

        return None
