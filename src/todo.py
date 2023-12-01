import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

todo_list = []

def todo(bot):
    def cmp_date(d1, d2):
        list1 = d1.split("/")
        list2 = d2.split("/")
        if list1[1] == list2[1]:
            if list1[0] < list2[0]:
                return True
            return False
        return list1[1] < list2[1]
    
    @bot.tree.command(name="todo_a", description="Adds a task to the todo list")
    async def todo_add(interaction: discord.Interaction, day: str, task: str):
        try:
            is_in = 0
            k = 0
            while todo_list != [] and k < len(todo_list):
                if todo_list[k] == day:
                    todo_list[k + 1] += f"\n{task}"
                    is_in = 1
                    break
                elif cmp_date(day, todo_list[k]):
                    todo_list.insert(k, day)
                    todo_list.insert(k + 1, task)
                    is_in = 1
                    break
                k += 2
            if is_in == 0:
                todo_list.append(day)
                todo_list.append(task)
            await interaction.response.send_message(f"Task \"{task}\" added on {day}")
        except Exception as e:
            await interaction.response.send_message(f"Adding task failed")

    @bot.tree.command(name="todo_r", description="Removes a task to the todo list")
    async def todo_remove(interaction: discord.Interaction, day: str, task: str):
        try:
            i = len(todo_list)
            for j in range(0, i):
                if todo_list[j] == task:
                    if todo_list[j - 1] == day:
                        todo_list.pop(j)
                        todo_list.pop(j-1)
                        break
            await interaction.response.send_message(f"Task \"{task}\" removed on {day}")
        except Exception as e:
            await interaction.response.send_message(f"Removing task failed")

    @bot.tree.command(name="todo", description="Prints the todo list")
    async def todo_print(interaction: discord.Interaction):
        try:
            if todo_list:
                embed = discord.Embed(title="TODO List", color=discord.Color.blue())
                for j in range(0, len(todo_list), 2):
                    embed.add_field(name=todo_list[j], value=todo_list[j + 1], inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message(f"Empty")
        except Exception as e:
            await interaction.response.send_message(f"Printing list failed")

    @bot.tree.command(name="todo_c", description="Clears the todo list")
    async def todo_print(interaction: discord.Interaction):
        try:
            if todo_list:
                todo_list.clear()
                await interaction.response.send_message(f"TODO List cleared")
            else:
                await interaction.response.send_message(f"Empty")
        except Exception as e:
            await interaction.response.send_message(f"Clearing list failed")