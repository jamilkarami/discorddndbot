from typing import List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

@dataclass_json
@dataclass
class Language(DndObject):
    name: str = None
    type: str = None
    typical_speakers: List[str] = field(default_factory=list)
    script: str = None

    def get_vals(self):
        self.embedtitle = self.name
        return {
            "Type": self.type,
            "Typical Speakers": ', '.join(self.typical_speakers),
            "Script": self.script
        }