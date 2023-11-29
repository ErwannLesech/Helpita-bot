import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


def main():
    # loads the token
    load_dotenv(dotenv_path="config.conf")

    class HelpitaBot(commands.Bot):
        def __init__(self):
            super().__init__(command_prefix="/", intents=discord.Intents.default())

        # prints ready when the bot is started
        async def on_ready(self):
            print(f"{self.user.display_name} connected")
    
    help_bot = HelpitaBot()
    help_bot.run(os.getenv("TOKEN"))

    # reacts when a message "/todo day task" is sent on the server
    @bot.command(name='todo')
    async def todo_list(context, day: str, task: str):
        print("received")
        await context.content.send("```day: task```")

    

if __name__ == "__main__":
    main()
