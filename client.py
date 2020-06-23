import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from janitor import Janitor, config


load_dotenv()
janitor = Janitor()
config=config.config
botclient = commands.Bot(command_prefix=config.get('General', 'Sign'))

@botclient.command()
async def daerich(ctx):
    await ctx.channel.send("@Forged by DaErich#4668 in 2020@")
    print("daerich command executed")

@botclient.event
async def on_ready():
    print("Successfully logged in!")

@botclient.event
async def on_message(message):
    await janitor.sweep(message)
    await botclient.process_commands(message) # https://stackoverflow.com/questions/50050194/discord-py-bot-functionality-does-not-work-after-adding-new-codes

botclient.run(os.getenv("TOKEN"))