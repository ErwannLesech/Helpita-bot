import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.conf")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("READY")

@bot.command(name="helpita")
async def helpita(ctx):
    await ctx.send(f"```Usage:\n\t/zeus: prints the schedule\n\t/news \"[token]\": prints the 5 last news of the token\n\t/todo [date] \"task\": add the task to the todo list```")

@bot.command(name="todo")
async def todo_add(ctx, day, task):
    await ctx.send(f"```{day}: {task}```")

@bot.command(name="zeus")
async def print_zeus(ctx):
    await ctx.send(f"Print ZEUS !")

@bot.command(name="news")
async def new_news(ctx):
    await ctx.send(f"Print News !")

bot.run(os.getenv("TOKEN"))
