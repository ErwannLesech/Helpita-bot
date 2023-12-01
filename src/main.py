import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from zeus import zeus
from news import news
from todo import todo
from chat import gpt
from annales import annales

load_dotenv(dotenv_path="config.conf")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Helpita Bot is Up and Ready !")

    sync = await bot.tree.sync()
    print(f"{len(sync)} command(s) sync.")

@bot.tree.command(name="helpita", description="Prints the help message")
async def helpita(interaction: discord.Interaction):
    await interaction.response.send_message(f"```Usage:\n\t/helpita: prints this help message\n\n\t/gpt [Prompt]: prints the GPT-4 response to the prompt\n\n\t/todo: prints the todo list\n\t/todo_a [Date] [Task]: adds the task to the todo list\n\t/todo_r [Date] [Task]: removes the task to the todo list\n\t/todo_c: clears the todo list\n\n\t/lol_acc [Pseudo] [Tag] : Prints info about your lol account```")

todo(bot)
zeus(bot)
news(bot)
gpt(bot)
annales(bot)

bot.run(os.getenv("TOKEN"))
