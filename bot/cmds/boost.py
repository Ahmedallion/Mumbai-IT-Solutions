import json
import random

import discord
from discord import app_commands
from discord.ext import commands

class Boost(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="boost", description="Boosts your internet speed to... totally unrealistic levels.")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def boost(self, interaction: discord.Interaction):
        responses = json.load(open("./bot/assets/boost.json", "r"))
        if random.randint(1, 10) == 1:
            embed = discord.Embed(description=self.client.config["emojis"]["crossOrange"] + " " + random.choice(responses["invalid"]), color=int(self.client.config["colors"]["orange"], 16))
            await interaction.response.send_message(embed=embed)
        else:
            response = random.choice(responses["responses"])
            formatted_response = response.format(random.randint(150, 10000)) if "{}" in response else response
            await interaction.response.send_message(content=formatted_response)

async def setup(client):
    await client.add_cog(Boost(client))