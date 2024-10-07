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
        responses = ["MA'AM, DO NOT REDEEM THAT CODE!", "WHY? DID YOU REDEEM IT?!", "OH NO, YOU REDEEMED IT! WHAT HAVE YOU DONE?!", "WHY ARE YOU NOT LISTENING TO ME?!", "I'M LITERALLY SHOUTING!! I'M LITERALLY SHOUTING RIGHT NOW MA'AM!!!!", "WAIT... PLEASE WAIT!", "NO!! NO! NO!!!", "WOAH WAIT!", "MA'AM NOOOOOOOOOOOOOOOO!", "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!", "YOU DON'T HAVE TO DO THAT!!"]
        invalid = ["Your code could not be redeemed.", "There is a problem with that code, try a different one.", "This code has been redeemed.", "You have already redeemed this code."]
        if random.randint(1, 10) == 1:
            embed = discord.Embed(description=self.client.config["emojis"]["crossOrange"] + " **Error**: " + random.choice(invalid), color=int(self.client.config["colors"]["orange"], 16))
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(content=random.choice(responses))

async def setup(client):
    await client.add_cog(Redeem(client))