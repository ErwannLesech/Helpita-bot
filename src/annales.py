import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

annales_links = {
    "cpxa": "https://drive.google.com/drive/folders/1692Lwx3E8DPEiGe3jqePYXjYf-h4oYXx",
    "thl": "https://drive.google.com/drive/folders/19-WdWleMF6rg4n6-QR4mmmmFSC-orgoh",
    "asm": "https://drive.google.com/drive/folders/1FOV6TU82ch51I41TJ7kBRjF6u4_kA65T",
    "net": "https://drive.google.com/drive/folders/1Rjoj0OMrR6aWneVe5Ac-Q7qw3QVRSRjU",
    "sys": "https://drive.google.com/drive/folders/1V_e2gmdScD9ubnZrF2iLB0ktb8L3Kd9p",
    "masi": "https://drive.google.com/drive/folders/1Wyrj8a-GrpyCNZS3buVveBpNqL8Wrvet",
    "sta": "https://drive.google.com/drive/folders/1O5drhnZ2kgjfm2KQX9YO0gVM9svRcbVr",
    "sh": "https://drive.google.com/drive/folders/10EaIZNpw4r-5APDcfIS0MdsKllrpUkpn"
}


def annales(bot):
    @bot.tree.command(name="annales", description="Delivers the annales of the module")
    async def annales_command(interaction: discord.Interaction, module: str):
        module = module.lower()
        if module in annales_links:
            formatted_module = f"**{module.upper()}**"
            await interaction.response.send_message(f"{formatted_module} : {annales_links[module]}")
        else:
            available_modules = ', '.join(f"**{mod.upper()}**" for mod in annales_links.keys())
            await interaction.response.send_message(f"Module {module} not found!\nAvailable modules: {available_modules}")