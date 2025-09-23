import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

@bot.tree.command(name="TEST1",desciption="MZAR TEST1")
async def test(interaction: discord.Interaction):
    channel = interaction.channel
        user = interaction.user
            await interaction.response.send_message(f"{user.mention} Selam!")



            bot= commands.Bot(command_prefix="!",intents=discord.Intents.all()) 
            @bot.event
            async def on_message(message):
                if message.content.startswith("sa MZAR"):
                        await message.channel.send("**Aleyküm Selam Hoşgeldin !**")





                        @bot.event
                        async def on_ready():
                            print("BOT ÇALIŞIYOR")
                            bot.run(TOKEN)
