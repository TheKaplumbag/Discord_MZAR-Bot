import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

bot= commands.Bot(command_prefix="!",intents=discord.Intents.all()) 
@bot.event
async def on_message(message):
    if message.content.startswith("sa MZAR"):
        await message.channel.send("**Aleyküm Selam Hoşgeldin !**")

@bot.event
async def on_ready():
    print("BOT ÇALIŞIYOR")
bot.run(TOKEN)
