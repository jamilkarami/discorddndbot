from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc

ALIGNMENTS = {
    "Chaotic Evil": "chaotic-evil",
    "Chaotic Good": "chaotic-good",
    "Chaotic Neutral": "chaotic-neutral",
    "Lawful Evil": "Lawful-evil",
    "Lawful Good": "Lawful-good",
    "Lawful Neutral": "Lawful-neutral",
    "Neutral": "neutral",
    "Neutral Evil": "Neutral-evil",
    "Neutral Good": "Neutral-good"
}

@dataclass_json
@dataclass
class Alignment(DndObjectNameDesc):
    pass
