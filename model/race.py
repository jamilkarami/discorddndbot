from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

RACES = {
    'Dragonborn': 'dragonborn',
    'Dwarf': 'Dwarf',
    'Elf': 'elf',
    'Gnome': 'gnome',
    'Half-elf': 'half-elf',
    'Half-Orc': 'half-orc',
    'Halfling': 'halfling',
    'Human': 'human',
    'Tiefling': 'tiefling',
}

@dataclass_json
@dataclass
class Race(DndObject):
    name: str = None
    speed: int = 0
    ability_bonuses: List[Dict] = field(default_factory=list)
    alignment: str = None
    age: str = None
    size: str = None
    size_description: str = None
    starting_proficiencies: List[Dict] = field(default_factory=list)
    languages: List[Dict] = field(default_factory=list)
    language_desc: str = None
    traits: List[Dict] = field(default_factory=list)
    subraces: List[Dict] = field(default_factory=list)

    def get_vals(self):
        self.embedtitle = self.name
        return {
            'inline': None,
            'Speed': self.speed,
            'Ability Bonuses': ', '.join([f"{a['ability_score']['name']} ({a['bonus']})" for a in self.ability_bonuses]),
            'Age': self.age,
            'Alignment': self.alignment,
            'Size': f"{self.size}. {self.size_description}",
            'Starting Proficiencies': ', '.join([p['name'] for p in self.starting_proficiencies]),
            'Language': self.language_desc,
            'Traits': ', '.join([t['name'] for t in self.traits]),
            'Subraces': ', '.join([s['name'] for s in self.subraces]),
        }