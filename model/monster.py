from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

@dataclass_json
@dataclass
class Monster(DndObject):
    name: str = None
    size: str = None
    type: str = None
    alignment: str = None
    armor_class: int = 0
    hit_points: int = 0
    hit_dice: str = None
    hit_points_roll: str = None
    speed: Dict = field(default_factory=dict)
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    proficiencies: List[Dict] = field(default_factory=list)
    damage_vulnerabilities: List[str] = field(default_factory=list)
    damage_resistances: List[str] = field(default_factory=list)
    damage_immunities:  List[str] = field(default_factory=list)
    condition_immunities:  List[str] = field(default_factory=list)
    senses: Dict = field(default_factory=dict)
    languages: str = None
    challenge_rating: int = 0
    xp: int = 0
    special_abilities: List[Dict] = field(default_factory=list)
    actions: List[Dict] = field(default_factory=list)
    legendary_actions: List[Dict] = field(default_factory=list)
    image: str = None

    def get_vals(self):
        self.embedtitle = self.name
        stat_str = f"Strength ({self.strength}), Dexterity ({self.dexterity}), Constitution ({self.constitution})\nIntelligence ({self.intelligence}), Wisdom ({self.wisdom}), Charisma ({self.charisma})"
        return {
            'Size': self.size,
            'Type': self.type,
            'Alignment': self.alignment,
            'Armor Class': self.armor_class,
            'Hit Points': self.hit_points,
            'Hit Dice': self.hit_dice,
            'Hit Points Roll': self.hit_points_roll,
            'Speed': ', '.join([f"{v} ({k})" for k,v in self.speed.items()]),
            'Stats': stat_str,
            'Proficiencies': ', '.join([f"{p['proficiency']['name']} ({p['value']})" for p in self.proficiencies]),
            'Damage Vulnerabilities': ', '.join(self.damage_vulnerabilities),
            'Damage Resistances': ', '.join(self.damage_resistances),
            'Damage Immunities': ', '.join(self.damage_immunities),
            'Condition Immunities': ', '.join(self.condition_immunities),
            'Senses': ', '.join([f"{k} ({v})" for k,v in self.senses.items()]),
            'Languages': self.languages,
            'Challenge Rating': self.challenge_rating,
            'XP': self.xp,
            'Special Abilities': '\n'.join([f"{a['name']} ({a['desc']})" for a in self.special_abilities]),
            'Actions': '\n'.join([f"{a['name']} ({a['desc']})" for a in self.actions]),
            'Legendary Actions': '\n'.join([f"{a['name']} ({a['desc']})" for a in self.legendary_actions]),
            'Image': self.image
        }