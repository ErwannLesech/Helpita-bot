from dotenv import load_dotenv
import openai
import os

load_dotenv(dotenv_path="config.conf")

openai.api_key = os.getenv("OPENAI_API_KEY")

def openai(bot):
    @bot.command(name="gpt")
    async def print_gpt(ctx, prompt):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n"]
        )

        await ctx.send(response["choices"][0]["text"])