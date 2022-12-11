import discord
import logging
from discord.ext import commands
from discord import app_commands
from util.apihelper import ApiHelper
from util.commandhelper import get_options
from model.abilityscore import *
from model.alignment import *
from model.background import *
from model.dndclass import *
from model.condition import *
from model.damagetype import *
# from model.equipment import *
from model.feature import Feature
from model.language import Language
from model.magicitem import MagicItem
from model.magicschool import *
from model.monster import Monster
from model.proficiency import Proficiency
from model.race import *
from model.skill import *
from model.spell import Spell
from model.subclass import Subclass
from model.subrace import Subrace

class Dnd(commands.Cog, name="dnd"):

    def __init__(self, bot):
        self.bot = bot
        self.apihelper = ApiHelper()

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"[{__name__}] Cog is ready")

    @commands.command()
    async def ping(self, ctx):
        return

    @app_commands.command(name="marco")
    async def marco(self, interaction: discord.Interaction):
        await interaction.response.send_message("Polo")
        return
    
    @app_commands.command(name="ability", description="Get details for an ability in DnD.")
    @app_commands.choices(abilityname=get_options(ABILITIES))
    async def ability(self, interaction: discord.Interaction, abilityname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(AbilityScore, abilityname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="alignment", description="Get details for an alignment in DnD.")
    @app_commands.choices(alignmentname=get_options(ALIGNMENTS))
    async def alignment(self, interaction: discord.Interaction, alignmentname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(Alignment, alignmentname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="background", description="Get details for a background in DnD.")
    @app_commands.choices(backgroundname=get_options(BACKGROUNDS))
    async def background(self, interaction: discord.Interaction, backgroundname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(Background, backgroundname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="class", description="Get details for a class in DnD.")
    @app_commands.choices(dndclassname=get_options(CLASSES))
    async def dndclass(self, interaction: discord.Interaction, dndclassname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(DndClass, dndclassname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="condition", description="Get details for a condition in DnD.")
    @app_commands.choices(conditionname=get_options(CONDITIONS))
    async def condition(self, interaction: discord.Interaction, conditionname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(Condition, conditionname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="damagetype", description="Get details for a damage type in DnD.")
    @app_commands.choices(damagetypename=get_options(DAMAGETYPES))
    async def damagetype(self, interaction: discord.Interaction, damagetypename: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(DamageType, damagetypename.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    # @app_commands.command(name="equipment", description="Get details for equipment in DnD.")
    # @app_commands.choices(damagetypename=get_options(DAMAGETYPES))
    # async def damagetype(self, interaction: discord.Interaction, damagetypename: app_commands.Choice[str]):
    #     c = self.apihelper.get_dndobject(DamageType, damagetypename.value)
    #     await interaction.response.send_message(embed=c.get_embed())
    #     return

    @app_commands.command(name="feature", description="Get details for a feature in DnD.")
    async def damagetype(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Feature, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="language", description="Get details for a language in DnD.")
    async def language(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Language, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="magicitem", description="Get details for a magic item in DnD.")
    async def magicitem(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(MagicItem, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="magicschool", description="Get details for a magic school in DnD.")
    @app_commands.choices(magicschoolname=get_options(MAGICSCHOOLS))
    async def magicschool(self, interaction: discord.Interaction, magicschoolname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(MagicSchool, magicschoolname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="monster", description="Get details for a monster in DnD.")
    async def monster(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Monster, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="proficiency", description="Get details for a proficiency in DnD.")
    async def proficiency(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Proficiency, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="race", description="Get details for a race in DnD.")
    @app_commands.choices(racename=get_options(RACES))
    async def race(self, interaction: discord.Interaction, racename: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(Race, racename.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="skill", description="Get details for a skill in DnD.")
    @app_commands.choices(skillname=get_options(SKILLS))
    async def skill(self, interaction: discord.Interaction, skillname: app_commands.Choice[str]):
        obj = self.apihelper.get_dndobject(Skill, skillname.value)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="spell", description="Get details for a spell in DnD.")
    async def spell(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Spell, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="subclass", description="Get details for a subclass in DnD.")
    async def subclass(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Subclass, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return

    @app_commands.command(name="subrace", description="Get details for a subrace in DnD.")
    async def subrace(self, interaction: discord.Interaction, query: str):
        obj = self.apihelper.get_dndobject(Subrace, query)
        if not obj:
            await interaction.response.send_message("Could not find anything matching your query.", ephemeral=True)
            return
        await interaction.response.send_message(embed=obj.get_embed())
        return


async def setup(bot: commands.Bot):
    await bot.add_cog(Dnd(bot))
