import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping", description="Shows the bot's latency.")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"Latency: {round(self.client.latency * 1000)}ms", color=int(self.client.config["defaultColor"], 16))
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(Ping(client))