import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def todo(bot):
    @bot.tree.command(name="todo", description="Add a task to the todo list")
    async def todo_add(interaction: discord.Interaction, day: str, task: str):
        await interaction.response.send_message(f"```{day}: {task}```")