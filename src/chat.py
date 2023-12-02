from dotenv import load_dotenv
import openai
import os
import discord

from logger import create_log

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

message_history = []

message_history.append({"role": "system", "content": "Tu es un bot discord"})


historic = open("historic.txt", "r")
for line in historic:
    message_history.append(line)
historic.close()


def gpt(bot):
    @bot.tree.command(name="gpt", description="Prints the GPT-3.5 response to the prompt")
    async def print_gpt(interaction: discord.Interaction, prompt: str):
        try:
            response = get_openai_response(prompt)
            await interaction.response.send_message(f"```{response}```")
        except Exception as e:
            print(f"Error during interaction processing: {e}")
        user = interaction.user
        create_log(prompt, user)

def get_openai_response(prompt):
    message_history.append({"role": "user", "content": prompt})
    print(message_history)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
        temperature=0.9,
        max_tokens=2048,
    )

    # write in historic
    historic = open("historic.txt", "w")
    historic.write("\{\"role\": \"user\", \"content\": prompt\}\n")
    historic.write("\{\"role\": \"system\", \"content\": response\}\n")
    historic.close()
    
    return response["choices"][0]["message"]["content"]