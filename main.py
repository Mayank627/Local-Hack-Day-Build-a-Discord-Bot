import discord
import os
import requests
import json
import random

client = discord.Client()

text_messages = ["developers", "swags", "open source", "development", "build", "bots","contribution","PR","Github"]

bot_responses = ["Keep developing.","Keep contributing","You can win developer swags on contributing.","Keep up your development.","Learning to code is never out of fashion."]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n𝘈𝘶𝘵𝘩𝘰𝘳: " + json_data[0]['a']
  return(quote)

@client.event 
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in text_messages):
    await message.channel.send(random.choice(bot_responses))

    
os.environ['TOKEN']
client.run(os.getenv('TOKEN'))
