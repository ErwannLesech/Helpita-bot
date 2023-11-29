import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def news(bot):
    @bot.command(name="news")
    async def print_news(ctx):
        await ctx.send(f"Print News !")