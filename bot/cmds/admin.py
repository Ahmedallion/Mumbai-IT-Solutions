import os
import sys

import discord
import psutil
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.admins = client.config["adminIDs"]

    @staticmethod
    def is_bot_admin():
        def predicate(ctx):
            return ctx.author.id in ctx.cog.admins
        return commands.check(predicate)

    @commands.command(name="about")
    @is_bot_admin()
    async def about(self, ctx):
        embed = discord.Embed(color=int(self.client.config["defaultColor"], 16))
        embed.set_author(name=f"{self.client.user.name}", icon_url=self.client.user.avatar.url)
        embed.set_thumbnail(url=self.client.user.avatar.url)
        embed.add_field(name="CPU Usage", value=f"`{psutil.cpu_percent()}%`")
        embed.add_field(name="Memory Usage", value=f"`{"{:.2f} GB".format(psutil.virtual_memory().used / (1024 * 1024 * 1024))}`")
        embed.add_field(name="Shard", value=f"`{ctx.guild.shard_id} / {self.client.shard_count}`")
        embed.add_field(name="Boomers / Servers", value=f"`{sum(guild.member_count for guild in self.client.guilds):,} / {len(self.client.guilds):,}`")
        embed.add_field(name="Discord.py", value=f"`{discord.__version__}`")
        embed.add_field(name="Python", value=f"`{sys.version.split()[0]}`")
        embed.set_footer(text=f"Latency: {round(self.client.latency * 1000)}ms", icon_url=self.client.user.avatar.url)
        await ctx.reply(embed=embed)

    @commands.command(name="logs")
    @is_bot_admin()
    async def logs(self, ctx):
        log_file_path = "discord.log"

        if os.path.exists(log_file_path):
            try:
                await ctx.reply(file=discord.File(log_file_path))
            except discord.DiscordException as e:
                await ctx.reply(f"An error occurred while sending the log file: {e}")
        else:
            await ctx.reply("The log file was not found")


async def setup(client):
    await client.add_cog(Admin(client))