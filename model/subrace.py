from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

@dataclass_json
@dataclass
class Subrace(DndObject):
    name: str = None
    race: Dict = field(default_factory=dict)
    desc: str = None
    ability_bonuses: List[Dict] = field(default_factory=list)
    starting_proficiencies: List[Dict] = field(default_factory=list)
    languages: List[Dict] = field(default_factory=list)
    language_options: Dict = field(default_factory=dict)
    racial_traits: List[Dict] = field(default_factory=list)

    def get_vals(self):
        self.embedtitle = self.name
        l_options : str = None
        
        if self.language_options:
            opts = ', '.join([o['item']['name'] for o in self.language_options['from']['options']])
            l_options = f"Choose {self.language_options['choose']} from {opts}"

        return {
            "Race": self.race['name'],
            "Description": self.desc,
            "Racial Traits": ', '.join([rt['name'] for rt in self.racial_traits]),
            "Ability Bonuses": ', '.join([f"{a['ability_score']['name']} ({a['bonus']})" for a in self.ability_bonuses]),
            "Starting Proficiencies": ', '.join([sp['name'] for sp in self.starting_proficiencies]),
            "Languages": ', '.join([l['name'] for l in self.languages]),
            "Language Options": l_options,
        }