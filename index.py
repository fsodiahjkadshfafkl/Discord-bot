import discord
token = "ODU3MzI5OTkwOTA3ODU0ODk4.YNOAxg.y2LAQbvTKWEd5dPxzejYlG7AHnA"
client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready")
    print(client.user)

client.run(token)