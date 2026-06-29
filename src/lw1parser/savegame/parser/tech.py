from .properties import _PropertyUtils
from lw1parser import maps

class _Tech:
    @staticmethod
    def get_foundry(checkpoint_table: list) -> dict:
        # Stored in checkpoints.checkpoint_table.Command1.TheWorld:PersistentLevel.XGFacility_Engineering_1.propertiers.m_arrFoundryHistory
        engineering = next((
            item for item in checkpoint_table 
            if item["name"] == "Command1.TheWorld:PersistentLevel.XGFacility_Engineering_1"), 
            None
        )

        foundry = next((
            item for item in engineering.get("properties", []) 
            if item["name"] == "m_arrFoundryHistory"), 
            None)
        
        if foundry is None:
            return {}

        # Return dict of foundry unlocks
        return _PropertyUtils._parse_mapped_array(
            flags=foundry.get("elements", []),
            mapping=maps.FOUNDRY_UNLOCK_MAP,
            skip_first=True,
        )
    
    @staticmethod
    def get_research(checkpoint_table: list) -> dict:
        # Stored in checkpoints.checkpoint_table.Command1.TheWorld:PersistentLevel.XGFacility_Labs_1.propertiers.m_arrResearched
        labs = next((
            item for item in checkpoint_table 
            if item["name"] == "Command1.TheWorld:PersistentLevel.XGFacility_Labs_1"), 
            None
        )

        research = next((
            item for item in labs.get("properties", []) 
            if item["name"] == "m_arrResearched"), 
            None)
        
        if research is None:
            return {}

        # Return dict of foundry unlocks
        return _PropertyUtils._parse_mapped_array(
            flags=research.get("elements", []),
            mapping=maps.RESEARCH_UNLOCK_MAP,
            skip_first=True,
        )