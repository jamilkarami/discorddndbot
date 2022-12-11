from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc

CONDITIONS = {
    "Blinded": "blinded",
    "Charmed": "charmed",
    "Deafened": "deafened",
    "Exhaustion": "exhaustion",
    "Frightened": "frightened",
    "Grappled": "grappled",
    "Incapacitated": "incapacitated",
    "Invisible": "invisible",
    "Paralyezed": "paralyezed",
    "Petrified": "petrified",
    "Poisoned": "poisoned",
    "Prone": "prone",
    "Restrained": "restrained",
    "Stunned": "stunned",
    "Unconscious": "unconscious",
}

@dataclass_json
@dataclass
class Condition(DndObjectNameDesc):
    pass