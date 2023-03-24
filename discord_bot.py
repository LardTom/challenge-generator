

import discord
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black", "white"]
garments = ['t-shirt', 'jeans', 'sweater', 'dress', 'skirt', 'jacket', 'hoodie', 'shorts', 'blouse', 'coat']
settings = ['casual', 'formal', 'sporty', 'business', 'beachwear', 'evening', 'streetwear', 'retro', 'festival', 'Halloween', 'costume party', 'wedding', 'Christmas', 'Easter']

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!challenge'):
        print('Received command !challenge from {0.author}'.format(message))
        random_color = colors[random.randint(0, len(colors) - 1)]
        random_garment = garments[random.randint(0, len(garments) - 1)]
        random_setting = settings[random.randint(0, len(settings) - 1)]
        response = 'Create a ' + random_color + " " + random_setting + " " + random_garment
        print('Sending response "{0}" to {1.author}'.format(response, message))
        await message.channel.send(response)

client.run('DISCORD_TOKEN')
