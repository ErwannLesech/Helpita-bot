from dotenv import load_dotenv
import openai
import os

from logger import create_log

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt(bot):
    @bot.command(name="gpt")
    async def print_gpt(ctx, *, prompt):
        user = ctx.author
        create_log(prompt, user)
        await ctx.defer()

        response = get_openai_response(prompt)
        await ctx.send(f"```{response}```")

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