from typing import Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc

@dataclass_json
@dataclass
class Feature(DndObjectNameDesc):
    class_: Dict = field(default_factory=dict)

    def to_dict(self):
        vals: dict = DndObjectNameDesc.to_dict()
        vals['class'] = self.class_['name']