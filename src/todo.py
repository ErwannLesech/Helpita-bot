import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

def todo(bot):
    @bot.command(name="todo")
    async def todo_add(ctx, day, task):
        user = ctx.author
        await ctx.send(f"```{day}: {task}```")