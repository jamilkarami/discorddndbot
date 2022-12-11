from typing import Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc

MAGICSCHOOLS = {
    "Abjurration": "abjurration",
    "Conjuration": "conjuration",
    "Divination": "divination",
    "Enchantment": "enchantment",
    "Evocation": "evocation",
    "Illusion": "illusion",
    "Necromancy": "necromancy",
    "Transmutation": "transmutation"
}

@dataclass_json
@dataclass
class MagicSchool(DndObjectNameDesc):
    pass