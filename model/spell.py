from typing import List, Dict, Optional
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject
from util.vars import BOOLS

@dataclass_json
@dataclass
class Spell(DndObject):
    name: str = None
    desc: List[str] = field(default_factory=list)
    higher_level: List[str] = field(default_factory=list)
    range: str = None
    components: List[str] = field(default_factory=list)
    material: Optional[str] = None
    ritual: str = None
    duration: str = None
    concentration: bool = False
    casting_time: str = None
    level: int = 0
    damage: Dict = field(default_factory=dict)
    school: Dict = field(default_factory=dict)
    classes: List[Dict] = field(default_factory=list)
    subclasses: List[Dict] = field(default_factory=list)
    
    def get_vals(self):
        self.embedtitle = self.name
        dmg_string = ""
        if 'damage_at_slot_level' in self.damage:
            dmg_string = ', '.join([f"{v} ({k})" for k,v in self.damage['damage_at_slot_level'].items()])
        if 'damage_at_character_level' in self.damage:
            dmg_string = ', '.join([f"{v} ({k})" for k,v in self.damage['damage_at_character_level'].items()])
        return {
            "Description": ' '.join(self.desc),
            "Higher Levels": ' '.join(self.higher_level),
            "Range": self.range,
            "Components": ', '.join(self.components),
            "Material": self.material,
            "Ritual": self.ritual,
            "Duration": self.duration,
            "Concentration": BOOLS[self.concentration],
            "Casting Time": self.casting_time,
            "Level": self.level,
            "Damage Type": self.damage['damage_type']['name'],
            "Damage at Level X":  dmg_string,
            "School": self.school['name'],
            "Classes": ', '.join([c['name'] for c in self.classes]),
            "Subclasses": ', '.join([s['name'] for s in self.subclasses])
        }