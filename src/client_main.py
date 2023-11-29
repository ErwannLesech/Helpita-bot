import discord
from dotenv import load_dotenv
import os

def main():
    # loads the token
    load_dotenv(dotenv_path="config.conf")

    # inits bot
    intents = discord.Intents.default()
    # intents.members = True        # for the on_member_join func
    client = discord.Client(intents=intents)

    # prints ready when the bot is started
    @client.event
    async def on_ready():
        print("READY")

    # reacts when a message is sent on the server
    @client.event
    async def on_message(message):
        print(message.content)                      # prints every messages sent on the server
        if message.content.lower() == "Bonjour":    # BONJOUR, BonJour, bonjour
            await message.content.send("Bonsoir")   # respond on the server
        #TODO ZEUS
        elif message.content.startswith("/zeus"):
            await message.content.send("")
        #TODO NEWS
        elif message.content.startswith("/news"):
            await message.content.send("")
        elif message.content.startswith("/todo"):
            day = message.content.split()[1]
            task = message.content.split()[2]

    # writes a message on the test channel to welcome a new user
    # @client.event
    # async def on_member_join(member):
    # test_chan: discord.TextChannel = client.get_channel(1179455998876987525) # test channel
    # await test_chan.send(content=f"Welcome {member.display_name} !")

    client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()
