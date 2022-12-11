from typing import List, Dict
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .dndobjectnamedesc import DndObjectNameDesc
from util.vars import BOOLS

@dataclass_json
@dataclass
class MagicItem(DndObjectNameDesc):
    equipment_category: Dict = field(default_factory=dict)
    rarity: Dict = field(default_factory=dict)
    variants: List[Dict] = field(default_factory=dict)
    variant: bool = False

    def get_vals(self):
        self.embedtitle = self.name
        vals = DndObjectNameDesc.get_vals(self)
        vals['Category'] = self.equipment_category['name']
        vals['Rarity'] = self.rarity['name']
        vals['Is Variant'] = BOOLS[self.variant]
        vals['Variants'] = '\n'.join([mi['name'] for mi in self.variants])
        return vals