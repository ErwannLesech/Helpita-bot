"""
Inspired by Sanetro"s videos
"""

from dotenv import load_dotenv
import os
import requests
import discord
from discord.ext import commands

load_dotenv(dotenv_path="config.conf")

lol_api_key = os.getenv("LEAGUE_OF_LEGENDS_API_KEY")

def lol(bot):
    @bot.tree.command(name="lol_acc", description="Displays the LOL account information")
    async def print_account(interaction: discord.Interaction, game_name: str, tag_line: str):
        account = get_lol_account(game_name, tag_line)
        ranks = get_lol_ranks(account[4])
        masteries = get_lol_masteries(account[1])
        if account == "Error":
            await interaction.response.send_message(f"```Error```")
        ember = discord.Embed(title=account[0], description=f"Level {account[2]}", color=discord.Color.blue())
        ember.set_thumbnail(url=account[3])
        # ember.add_field(name="Account ID", value=message[1], inline=False)
        for i in range(0, len(ranks), 6):
            if (ranks[i] == "RANKED_SOLO_5x5"):
                ember.add_field(name=f"Ranked_solo - Winrate", value=ranks[i + 1] + " " + ranks[i + 2] + " " + str(ranks[i + 3]) + " LP - " + str(round(ranks[i + 4] / (ranks[i + 4] + ranks[i + 5]) * 100, 2)) + "%", inline=False)
            elif (ranks[i] == "RANKED_FLEX_SR"):
                ember.add_field(name=f"Ranked_flex - Winrate", value=ranks[i + 1] + " " + ranks[i + 2] + " " + str(ranks[i + 3]) + " LP - " + str(round(ranks[i + 4] / (ranks[i + 4] + ranks[i + 5]) * 100, 2)) + "%", inline=False)
            else:
                ember.add_field(name=f"Ranked_tft - Winrate", value=ranks[i + 1] + " " + ranks[i + 2] + " " + str(ranks[i + 3]) + " LP - " + str(round(ranks[i + 4] / (ranks[i + 4] + ranks[i + 5]) * 100, 2)) + "%", inline=False)
        for i in range(1):
            ember.set_image(url=masteries[3][0])
            ember.add_field(name=masteries[0][i], value=str(masteries[1][i]) + " pts, lvl " + str(masteries[2][i]), inline=False)
        await interaction.response.send_message(embed=ember)

    @bot.tree.command(name="lol_rotation", description="Displays the LOL free rotation")
    async def print_rotation(interaction: discord.Interaction):
        rotation = get_lol_rotation()
        if rotation == "Error":
            await interaction.response.send_message(f"```Error```")
        ember = discord.Embed(title="Free rotation", color=discord.Color.blue())
        for i in range(len(rotation[0])):
            """ember = discord.Embed(title=rotation[0][i], color=discord.Color.blue())
            ember.set_thumbnail(url=rotation[1][i])
            if interaction.response.is_done():
                await interaction.followup.send(embed=ember)
            else:
                await interaction.response.send_message(embed=ember)"""
            ember.add_field(name=rotation[0][i], value="")  
        ember.set_thumbnail(url=rotation[1][0])        
        await interaction.response.send_message(embed=ember)  

    @bot.tree.command(name="lol_match", description="Displays the last LOL match")
    async def print_match(interaction: discord.Interaction, game_name: str, tag_line: str):
        account = get_lol_account(game_name, tag_line)
        if account == "Error":
            await interaction.response.send_message(f"```Error```")
        match = get_lol_match(account[1])
        if match == "Error":
            await interaction.response.send_message(f"```Error```")
        ember = discord.Embed(title=match[0], description=match[1], color=discord.Color.blue())
        ember.set_thumbnail(url=account[3])
        ember.set_image(url=match[1])
        ember.add_field(name="Game duration", value=match[3], inline=False)
        ember.add_field(name="Game mode", value=match[4], inline=False)
        ember.add_field(name="Champion", value=match[5], inline=False)
        ember.add_field(name="KDA", value=match[6], inline=False)
        await interaction.response.send_message(embed=ember)

def get_champ_image(champ):
    champions_db = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()    
    
    champions = []

    # listing all champions
    [champions.append(champion) for champion in champions_db['data']]        

    # get ordered list champion names and include avatars
    for name in champions:
        wantedChampion = champions_db['data'][name]['key']             
        if int(wantedChampion) == int(champ):            
            return "http://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/" + name + ".png"

    

def get_lol_match(id):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{id}/ids?start=0&count=1"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        match_id = response.json()[0]
    else:
        return "Error"

    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        game_mode = response.json()["info"]["gameMode"]
        game_duration = response.json()["info"]["gameDuration"]
        game_duration = str(game_duration // 60) + "m " + str(game_duration % 60) + "s"
        for i in range(len(response.json()["info"]["participants"])):
            if response.json()["info"]["participants"][i]["puuid"] == id:
                game_name = response.json()["info"]["participants"][i]["summonerName"]
                game_icon = "http://ddragon.leagueoflegends.com/cdn/11.16.1/img/profileicon/" + str(response.json()["info"]["participants"][0]["profileIcon"])
                game_champ = response.json()["info"]["participants"][i]["championName"]
                champ_id = response.json()["info"]["participants"][i]["championId"]
                game_kills = response.json()["info"]["participants"][i]["kills"]
                game_deaths = response.json()["info"]["participants"][i]["deaths"]
                game_assists = response.json()["info"]["participants"][i]["assists"]
                game_ratio = str(game_kills) + "/" + str(game_deaths) + "/" + str(game_assists)
                champ_image = get_champ_image(champ_id)
        return (game_name, champ_image, game_icon, game_duration, game_mode, game_champ, game_ratio)
    else:
        return "Error"


def get_lol_rotation():
    url = f"https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rotation = []
        for i in range(len(response.json()["freeChampionIds"])):
            rotation.append(response.json()["freeChampionIds"][i])

        champions_db = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()    
    
        champions = []

        # listing all champions
        [champions.append(champion) for champion in champions_db['data']]        

        champNames = []
        champIcons = []

        # get ordered list champion names and include avatars
        for championId in rotation:
            for name in champions:
                wantedChampion = champions_db['data'][name]['key']             
                if int(wantedChampion) == int(championId): # one is str, one is int               
                    champNames.append(name)
                    champIcons.append("http://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/" + name + ".png")

        return (champNames, champIcons)
    else:
        return "Error"

def get_lol_account(game_name, tag_line):
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        account_id = response.json()["puuid"]
    else:
        return "Error"

    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{account_id}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        id = response.json()["id"]
        account_name = response.json()["name"]
        account_lvl = response.json()["summonerLevel"]
        account_icon = "http://ddragon.leagueoflegends.com/cdn/11.16.1/img/profileicon/" + str(response.json()["profileIconId"]) + ".png"
        return (account_name, account_id, account_lvl, account_icon, id)
    else:
        return "Error"

def get_lol_ranks(id):

    url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    
    calls = {0:"queueType", 1:"tier", 2:"rank", 3:"leaguePoints", 4:"wins", 5:"losses"}
    ranks = []
    try:
        for i in range(len(response.json())):
            for j in range(6):
                ranks.append(response.json()[i][calls[j]])
    except:
        return "Error"

    return (ranks)

def get_lol_masteries(id):
    count = 5
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{id}/top?count={count}"
    headers = {
        "X-Riot-Token": lol_api_key
    }
    response = requests.get(url, headers=headers)
    champIds = []
    champLvl = []
    champPts = []

    for champion in response.json():
        champIds.append(champion['championId'])
        champLvl.append(champion['championLevel'])
        champPts.append(champion['championPoints'])

    champions_db = []
    # find champion by id and convert to name    
    champions_db = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()    
    
    champions = []

    # listing all champions
    [champions.append(champion) for champion in champions_db['data']]        

    champNames = []
    champIcons = []

    # get ordered list champion names and include avatars
    for championId in champIds:
        for name in champions:
            wantedChampion = champions_db['data'][name]['key']             
            if int(wantedChampion) == int(championId): # one is str, one is int               
                champNames.append(name)
                champIcons.append("http://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/" + name + ".png")

    return (champNames, champPts, champLvl, champIcons)