import discord
import os
from dotenv import load_dotenv
from janitor import Janitor


load_dotenv()
client = discord.Client()
janitor = Janitor()

@client.event
async def on_ready():
   print("Successfully logged in")

@client.event
async def on_message(message):
    await janitor.sweep(message)


client.run(os.getenv("TOKEN"))