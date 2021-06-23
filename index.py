import discord
import os

access_token = os.environ["BOT TOKEN"]  

token = "access_token"
client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready")
    print(client.user)

access_token = os.environ["BOT TOKEN"]    
    
client.run(token)
