from dotenv import load_dotenv
import openai
import os
import discord

from logger import create_log

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

message_history = []

message_history.append({"role": "system", "content": "Tu es un bot discord"})

def gpt(bot):
    @bot.tree.command(name="gpt", description="Prints the GPT-4 response to the prompt")
    async def print_gpt(interaction: discord.Interaction, prompt: str):
        try:
            # wait for the response
            await interaction.response.defer()
            # await asyncio.sleep(10)
            response = get_openai_response(prompt)
            embed = discord.Embed(title="GPT-4", color=discord.Color.blue())
            embed.add_field(name="Prompt", value=f"```{prompt}```", inline=False)
            embed.add_field(name="Response", value=f"```{response}```", inline=False)
            await interaction.followup.send(embed=embed)
        except Exception as e:
            print(f"Error during interaction processing: {e}")
        user = interaction.user
        create_log(prompt, user)

    @bot.tree.command(name="gpt_c", description="Clears the GPT-4 history")
    async def clear_gpt(interaction: discord.Interaction):
        try:
            message_history.clear()
            message_history.append({"role": "system", "content": "Tu es un bot discord"})
            await interaction.response.send_message(f"```GPT-4 history cleared```")
        except Exception as e:
            print(f"Error during interaction processing: {e}")
        
    

def get_openai_response(prompt):
    message_history.append({"role": "user", "content": prompt})
    # print(message_history)
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=message_history,
        temperature=0.9,
        max_tokens=2048
    )
    # print(response)
    message_history.pop()
    
    return response["choices"][0]["message"]["content"]