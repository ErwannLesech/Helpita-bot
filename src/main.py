import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from zeus import zeus
from news import news
from todo import todo
from openai import openai

load_dotenv(dotenv_path="config.conf")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("READY")

@bot.command(name="helpita")
async def helpita(ctx):
    await ctx.send(f"```Usage:\n\t/zeus: prints the schedule\n\t/news \"[token]\": prints the 5 last news of the token\n\t/todo [date] \"task\": add the task to the todo list\n\t/gpt [prompt]: prints the GPT-3.5 response to the prompt\n\t/helpita: prints this message```")

todo(bot)
zeus(bot)
news(bot)
openai(bot)

bot.run(os.getenv("TOKEN"))
