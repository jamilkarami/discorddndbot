from dataclasses import dataclass
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc

DAMAGETYPES = {
    "Acid": "acid",
    "Bludgeoning": "bludgeoning",
    "Cold": "cold",
    "Fire": "fire",
    "Force": "force",
    "Lightning": "lightning",
    "Necrotic": "necrotic",
    "Piercing": "piercing",
    "Poison": "poison",
    "Psychic": "psychic",
    "Radiant": "radiant",
    "Slashing": "slashing",
    "Thunder": "thunder",
}

@dataclass_json
@dataclass
class DamageType(DndObjectNameDesc):
    pass