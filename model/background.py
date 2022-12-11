from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject
from .proficiency import Proficiency

BACKGROUNDS = {
    "Acolyte": "acolyte"
}

@dataclass_json
@dataclass
class Background(DndObject):
    name: str
    starting_proficiencies: List[Proficiency] = field(default_factory=list)
    language_options: Dict = field(default_factory=dict)
    starting_equipment: List[Dict] = field(default_factory=list)
    starting_equipment_options: List[Dict] = field(default_factory=list)
    feature: Dict = field(default_factory=dict)
    personality_traits: Dict = field(default_factory=dict)
    ideals: Dict = field(default_factory=dict)
    bonds: Dict = field(default_factory=dict)
    flaws: Dict = field(default_factory=dict)

    def get_vals(self):
        self.embedtitle = self.name
        st_eq_opts = '\n'.join([f"{eq['from']['equipment_category']['name']} ({eq['choose']})" for eq in self.starting_equipment_options])
        vals = {
            "Starting Proficiencies": ', '.join([p.name for p in self.starting_proficiencies]),
            "Starting Equipment": '\n'.join([eq['equipment']['name'] for eq in self.starting_equipment]),
            "Language Options": self.language_options['choose'],
            "Starting Equipment Options": st_eq_opts
        }
        return vals