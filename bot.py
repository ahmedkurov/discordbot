import requests
import json
import discord

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']



with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()
    
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
    print('------')

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith('thankan'):
        await message.channel.send('Nikan thankan aaranen ariyo')
    
    if message.content.startswith('chiri'):
        await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)