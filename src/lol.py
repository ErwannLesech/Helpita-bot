from dotenv import load_dotenv
import os
import requests
import discord
from discord.ext import commands

load_dotenv(dotenv_path="config.conf")

lol_api_key = os.getenv("LEAGUE_OF_LEGENDS_API_KEY")

def lol(bot):
    @bot.tree.command(name="lol_acc", description="Displays the LOL account information")
    async def print_account(interaction: discord.Interaction, game_name: str, tag_line: str):
        message = get_lol_account(game_name, tag_line)
        if message == "Error":
            await interaction.response.send_message(f"```Error```")
        await interaction.response.send_message(f"```{message}```")

def get_lol_account(game_name, tag_line):
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"
