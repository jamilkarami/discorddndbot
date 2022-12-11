from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

CLASSES = {
    "Barbarian": "barbarian",
    "Bard": "bard",
    "Cleric": "cleric",
    "Druid": "druid",
    "Fighter": "fighter",
    "Monk": "monk",
    "Paladin": "Rogue",
    "Ranger": "ranger",
    "Rogue": "rogue",
    "Sorcerer": "sorcerer",
    "Warlock": "warlock",
    "Wizard": "wizard"
}

@dataclass_json
@dataclass
class DndClass(DndObject):
    name: str
    hit_die: int
    proficiency_choices: List[Dict] = field(default_factory=list)
    proficiencies: List[Dict] = field(default_factory=list)
    saving_throws: List[Dict] = field(default_factory=list)
    starting_equipment: List[Dict] = field(default_factory=list)
    starting_equipment_options: List[Dict] = field(default_factory=list)

    def get_vals(self):
        self.embedtitle = self.name
        vals = {
            "Hit Die": self.hit_die,
            "Proficiencies": '\n'.join([p['desc'] for p in self.proficiencies]),
            "Saving Throws": ', '.join([st['name'] for st in self.saving_throws]),
            "Starting Equipment": '\n'.join([eq['equipment']['name'] for eq in self.starting_equipment]),
            "Starting Equipment Options": '\n'.join([eq['desc'] for eq in self.starting_equipment_options]),
        }
        return vals