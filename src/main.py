import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from zeus import zeus
from news import news
from todo import todo
from chat import gpt

load_dotenv(dotenv_path="config.conf")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Helpita Bot is Up and Ready !")

    sync = await bot.tree.sync()
    print(f"{len(sync)} command(s) sync.")

@bot.tree.command(name="helpita", description="Prints the help message")
async def helpita(interaction: discord.Interaction):
    await interaction.response.send_message(f"```Usage:\n\t/zeus: prints the schedule\n\t/news \"[token]\": prints the 5 last news of the token\n\t/todo [date] \"task\": add the task to the todo list\n\t/gpt [prompt]: prints the GPT-3.5 response to the prompt\n\t/helpita: prints this message```")

todo(bot)
zeus(bot)
news(bot)
gpt(bot)

bot.run(os.getenv("TOKEN"))
