# importing the imports wee need
import discord
from discord.ext import commands
from discord import app_commands
import json


config = json.load(open("config.json", encoding="utf-8")) # defining the config file
client = commands.Bot(command_prefix="?", intents=discord.Intents.all()) # defining our client


# defining our startup command
@client.event 
async def on_ready():
    print(f"Logged in as {client.user}.")
    await client.tree.sync() # syncing bot when the bot starts

# ban command
@client.tree.command(name="ban", description="Ban a person from the server")
@app_commands.describe(user="The user that you want to ban", reason="The reason why you want to ban this user") # describing the command options
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = None): # defining the options you can use

    await user.ban(reason=reason) # banning the user with the reason provided

    embed = discord.Embed(
        description=f"Successfully banned {user.mention} from {interaction.guild.name}.", # you could customize the embed over here
        color=discord.Color.dark_purple() # you could customize the color of the embed here ( Ex:  discord.Color.green())
    )

    await interaction.response.send_message(embed=embed) # over here we are sending the embed to the discord, if you want to make this message invisible for other members do the following: Replace "await interaction.response.send_message(embed=embed)" with "await interaction.response.send_message(embed=embed, ephemeral=True)" 


client.run(config["bot_token"]) # over here the bot gets the bot token from the config file.

# DONT FORGET TO JOIN DISCORD.GG/TIJNS