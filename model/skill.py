from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

SKILLS = {
    "Acrobatics": "acrobatics",
    "Animal Handling": "animal-handling",
    "Arcana": "arcana",
    "Athletics": "athletics",
    "Deception": "deception",
    "History": "history",
    "Insight": "insight",
    "Intimidation": "intimidation",
    "Investigation": "investigation",
    "Medicine": "medicine",
    "Nature": "nature",
    "Perception": "perception",
    "Performance": "performance",
    "Persuasion": "persuasion",
    "Religion": "religion",
    "Sleight of Hand": "sleight-of-hand",
    "Stealth": "stealth",
    "Survival": "survival",
}

@dataclass_json
@dataclass
class Skill(DndObject):
    name: str = None
    desc: List[str] = field(default_factory=list)
    ability_score: Dict = field(default_factory=dict)

    def get_vals(self):
        self.embedtitle = self.name
        return {
            'Description': ' '.join(self.desc),
            'Related Ability': self.ability_score['name']
        }