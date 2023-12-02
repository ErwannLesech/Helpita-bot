import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def zeus(bot):
    @bot.tree.command(name="zeus", description="Prints the schedule")
    async def print_zeus(interaction: discord.Interaction):
        await interaction.response.send_message(f"Print ZEUS !")

def get_course():
    url = f"https://api.emploi-du-temps.utt.fr/api/weeks/2021-2022/1"