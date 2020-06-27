import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from janitor import Janitor, config
from filereader import filereader


load_dotenv()
janitor = Janitor()
inifile = filereader("bot.ini")
config=config.config
botclient = commands.Bot(command_prefix=config.get('General', 'Sign'))
content={}

def addcomands():
    inifile.readbetween("[CustomCommands]", "[EOFCustomCommands]")
    for line in inifile.commands:
        line = line.split("=")
        line = [linecontent.strip() for linecontent in line]
        content[line[0]]=line[1]
        

    print("Content added")

async def process_own_commands(message):
    for key in content:
        if message.content == config.get('General', 'Sign')+key:
            if "@author" in content[key]:
                await message.channel.send(message.author.mention + content[key].strip("@author"))
            else:
                await message.channel.send(content[key])

    await janitor.sweep(message)
    await botclient.process_commands(message)

    

@botclient.command()
async def daerich(ctx):
    await ctx.channel.send("@Forged by DaErich#4668 in 2020@")
    print("daerich command executed")

@botclient.event
async def on_ready():
    addcomands()
    print(content)
    print("Successfully logged in!")

@botclient.event
async def on_message(message):
    await process_own_commands(message)
    #await janitor.sweep(message)
    #await botclient.process_commands(message) # https://stackoverflow.com/questions/50050194/discord-py-bot-functionality-does-not-work-after-adding-new-codes

botclient.run(os.getenv("TOKEN"))