from typing import List, Union
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobject import DndObject

@dataclass_json
@dataclass
class DndObjectNameDesc(DndObject):
    name: str
    desc: Union[str, List[str]] = None

    def get_vals(self):
        self.embedtitle = self.name
        return {
            "Description": '\n'.join(self.desc) if type(self.desc)==list else self.desc
        }