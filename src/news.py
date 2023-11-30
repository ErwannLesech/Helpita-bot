import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def news(bot):
    @bot.tree.command(name="news", description="Prints the last news")
    async def print_news(interaction: discord.Interaction):
        await interaction.response.send_message(f"Print News !")