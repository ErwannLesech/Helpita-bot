import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def zeus(bot):
    @bot.command(name="zeus")
    async def print_zeus(ctx):
        await ctx.send(f"Print ZEUS !")