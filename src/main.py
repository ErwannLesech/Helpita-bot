import discord
from dotenv import load_dotenv
import os

def main():
    load_dotenv(dotenv_path="config.conf")

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()
