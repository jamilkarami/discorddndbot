from typing import List
from discord import Embed
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject
from .skill import Skill

ABILITIES = {"Charisma":"cha", "Constitution":"con", "Dexterity":"dex", "Intelligence":"int", "Strength":"str", "Wisdom":"wis"}

@dataclass_json
@dataclass
class AbilityScore(DndObject):
    name: str = None
    full_name: str = None
    desc: str = None
    skills: List[Skill] = field(default_factory=list)


    def get_vals(self):
        self.embedtitle = self.full_name
        sks = ', '.join([skill.name for skill in self.skills])
        vals = {
            "Description": ' '.join(self.desc),
            "Related Skills": sks
        }
        return vals
