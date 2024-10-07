import asyncio
import json
import logging
import logging.handlers
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

with open("./bot/config.json", "r") as config_file:
    config = json.load(config_file)

load_dotenv()
token = os.getenv("BOT_TOKEN")

if token is None:
    print("Error: The BOT_TOKEN environment variable is required. Please set it and try again.")
    sys.exit(1)

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logging.getLogger("discord.http").setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename = "discord.log",
    encoding = "utf-8",
    maxBytes = 32 * 1024 * 1024,
    backupCount = 5
)
dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter("[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{")
handler.setFormatter(formatter)
logger.addHandler(handler)

class MyClient(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config
        self.status_task = None

    async def setup_hook(self) -> None:
        await self.load_extensions()
        self.status_task = asyncio.create_task(self.change_status())

    async def load_extensions(self):
        for filename in os.listdir("./bot/cmds"):
            if filename.endswith(".py"):
                await self.load_extension(f"cmds.{filename[:-3]}")

    async def on_ready(self):
        logging.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logging.info("------")
        try:
            synced = await self.tree.sync()
            logging.info(f"Synced {len(synced)} command(s)")
        except Exception as e:
            logging.error(e)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(description=f"{config["emojis"]["crossOrange"]} **Not Found**: Sorry, prefixes are no longer available. Please use slash commands instead.", color=int(config["colors"]["orange"], 16))
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.CheckFailure):
            embed = discord.Embed(description=f"{config["emojis"]["crossOrange"]} **Missing Permission**: You do not have the required permission to use this command.", color=int(config["colors"]["orange"], 16))
            await ctx.reply(embed=embed)
        else:
            logging.error(f"Error in command '{ctx.command}': {error}")
            embed = discord.Embed(description=f"{config["emojis"]["cross"]} **Error**: {error}", color=int(config["colors"]["red"], 16))
            await ctx.reply(embed=embed)

    async def change_status(self):
        await self.wait_until_ready()
        while not self.is_closed():
            activities = [
                discord.Game(name="Tech Support Simulator 2024"),
                discord.Activity(type=discord.ActivityType.watching, name="Tutorials on how not to fix things"),
                discord.CustomActivity(name="Fixing tech... or making it worse 🤷‍♂️"),
                discord.CustomActivity(name="Have you tried turning it off and on?"),
            ]
            
            for activity in activities:
                await self.change_presence(activity=activity)
                await asyncio.sleep(600)

intents = discord.Intents.all()
client = MyClient(command_prefix=config["commandPrefix"], intents=intents)
client.remove_command("help")

logging.info("Starting bot...")
client.run(token)