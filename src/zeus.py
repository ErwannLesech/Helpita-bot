import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def zeus(bot):
    @bot.tree.command(name="zeus", description="Prints the schedule")
    async def print_zeus(interaction: discord.Interaction):
        await interaction.response.send_message(f"Print ZEUS !")