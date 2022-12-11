from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

@dataclass_json
@dataclass
class Subclass(DndObject):
    class_: Dict = field(default_factory=dict)
    name: str = None
    subclass_flavor : str = None
    desc: List[str] = field(default_factory=list)
    spells: List[Dict] = field(default_factory=list)
    
    def get_vals(self):
        self.embedtitle = self.name
        spell_str = []

        for spell in self.spells:
            prereqs = ", ".join([p['name'] for p in spell['prerequisites']])
            spell_str.append(f"{spell['spell']['name']} ({prereqs})")

        return {
            "Class": self.class_,
            "Subclass Flavor": self.subclass_flavor,
            "Description": ' '.join(self.desc),
            "Spells (prerequisite)": '\n'.join(spell_str)
        }