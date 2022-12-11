import os
import discord
import asyncio
import logging
from discord.ext import commands
from dotenv import load_dotenv

async def main():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    logging.basicConfig(filename='bot.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')

    intents = discord.Intents.all()
    activity = discord.Activity(type=discord.ActivityType.watching, detail="", name="")
    intents.members = True
    client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents, activity=activity)

    @client.event
    async def on_ready():
        print(f'DnD bot is ready to serve.')

    @client.event
    async def on_connect():
        print(f"{client.user.name} has connected to Discord!")
        await client.tree.sync()

    async def load_extensions():
        for filename in os.listdir("./cogs"):
            if not filename.endswith('py'):
                continue
            extension_name = f"cogs.{filename[:-3]}"
            logging.info(f"Loading extension: {extension_name}")
            await client.load_extension(extension_name)

    async with client:
        await load_extensions()
        await client.start(TOKEN)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Powering down...")
