from typing import List, Dict, Optional
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject
from .dndclass import DndClass
from .race import Race

@dataclass_json
@dataclass
class Proficiency(DndObject):
    type: str = Optional[None]
    name: str = None
    classes: List[Dict] = field(default_factory=list)
    races: List[Dict] = field(default_factory=list)

    def get_vals(self):
        self.embedtitle = self.name
        return {
            "Type": self.type,
            "Classes": ', '.join([c['name'] for c in self.classes]),
            "Races": ', '.join([r['name'] for r in self.races])
        }
        