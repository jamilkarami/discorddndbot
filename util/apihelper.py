import logging
import requests
import os
from model.abilityscore import AbilityScore
from model.alignment import Alignment
from model.background import Background
from model.dndclass import DndClass
from model.dndobject import DndObject
from model.condition import Condition
from model.damagetype import DamageType
# from model.equipment import Equipment
from model.feature import Feature
from model.language import Language
from model.magicitem import MagicItem
from model.magicschool import MagicSchool
from model.monster import Monster
from model.proficiency import Proficiency
from model.race import Race
from model.skill import *
from model.spell import Spell
from model.subclass import Subclass
from model.subrace import Subrace

API_URL = os.getenv('DND_5E_API_URL')+"/{}/{}"
MAPPING = {
    AbilityScore: "ability-scores",
    Alignment: "alignments",
    Background: "backgrounds",
    DndClass: "classes",
    Condition: "conditions",
    DamageType: "damage-types",
    Feature: "features",
    Language: "languages",
    MagicItem: "magic-items",
    MagicSchool: "magic-schools",
    Monster: "monsters",
    Proficiency: "proficiencies",
    Race: "races",
    Skill: "skills",
    Spell: "spells",
    Subclass: "subclasses",
    Subrace: "subraces",
}

class ApiHelper():

    def get_dndobject(self, cls, query) -> DndObject:
        url = API_URL.format(MAPPING.get(cls), self.get_query(query))
        data = requests.get(url=url)
        if data.status_code == 404:
            return None
        return cls.from_json(data.content)

    def get_query(self, query: str):
        return query.lower().replace(" ", "-")