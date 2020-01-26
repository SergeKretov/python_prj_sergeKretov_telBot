import discord
import os
 
from discord.ext import commands

TOKEN = os.environ.get('serge_kretov_tel_bot') #bot token from @botFather in config vars on heroku.com

Bot = commands.Bot(command_prefix = ":")
Bot.remove_command('help')

@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command
async def ping():
    await Bot.say("Pong")
 
# RUN
Bot.run(str(TOKEN))