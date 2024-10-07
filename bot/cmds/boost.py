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
        responses = ["Speed boosted to 9000 Mbps!", "Virus detected! To remove, please provide your credit card info... totally safe, promise! 😏"]
        await interaction.response.send_message(content=random.choice(responses))

async def setup(client):
    await client.add_cog(Boost(client))