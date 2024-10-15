import json
import random

import discord
from discord import app_commands
from discord.ext import commands

class Redeem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="redeem", description="Want to redeem your Google Play Store gift card?")
    @app_commands.describe(code="Enter the Google Play Store code you wish to redeem.")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def redeem(self, interaction: discord.Interaction, code: str):
        responses = json.load(open("./bot/assets/redeem.json", "r"))
        if random.randint(1, 10) == 1:
            embed = discord.Embed(description=self.client.config["emojis"]["crossOrange"] + " " + random.choice(responses["invalid"]), color=int(self.client.config["colors"]["orange"], 16))
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(content=random.choice(responses["responses"]))

async def setup(client):
    await client.add_cog(Redeem(client))