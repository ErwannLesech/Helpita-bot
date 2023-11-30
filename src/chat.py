from dotenv import load_dotenv
import openai
import os
import discord

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt(bot):
    @bot.tree.command(name="gpt", description="Prints the GPT-3.5 response to the prompt")
    async def print_gpt(interaction: discord.Interaction, prompt: str):
        try:
            response = get_openai_response(prompt)
            await interaction.response.send_message(f"```{response}```")
        except Exception as e:
            print(f"Error during interaction processing: {e}")

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un bot discord"},
            {"role": "user", "content": prompt}
            ],
        temperature=0.9,
        max_tokens=150,
    )
    
    return response["choices"][0]["message"]["content"]