import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.conf")

intent = discord.Intents.all()
intent.members = True

class HelpitaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intent)

    async def on_ready(self):
        print("READY")
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        await self.process_commands(message)
    
        print(message.content)
        if message.content.lower() == "bonjour":
            await message.channel.send("Bonsoir")
        elif message.content.startswith("/zeus"):
            await message.channel.send("zeus mode")
        elif message.content.startswith("/news"):
            await message.channel.send("news mode")
        elif message.content.startswith("/todo"):
            await message.channel.send("todo mode")
        
    async def todo(ctx):
        await ctx.send("todo mode")


bot = HelpitaBot()
bot.run(os.getenv("TOKEN"))