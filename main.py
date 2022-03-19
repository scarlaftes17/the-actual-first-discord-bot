import os
import discord
from checklist import handle_checklist
from wordle import play_wordle
token = os.environ['token']

client = discord.Client()


@client.event
async def on_ready():
  print('{0.user} has connected to Discord!'.format(client))
@client.event
async def on_message(message):
  author = str(message.author)
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  splitmessage = user_message.split(" ")
  if message.author == client.user:
    return
  if channel == "bot":
    #await message.channel.send(f'hello {username} {author} {user_message} {channel}')
    if user_message == 'hi' or user_message == 'hello':
      await message.channel.send('hello! :grin:')
    elif user_message == 'bye' or user_message == 'goodbye':
      await message.channel.send('see you soon! :wave:')
    elif 'power' in user_message:
      await message.channel.send(':cloud_lightning: **UNLIMITED POWER!!** :cloud_lightning:')
    elif  splitmessage[0] == '!cl':
      response = handle_checklist(user_message, author)
      await message.channel.send(response)
    elif splitmessage[0] == '!wordle':
      response = play_wordle(user_message, author)
      await message.channel.send(response)      
  else:
    await message.channel.send('please send messages in **_BOT_  CHANNEL ONLY** :poop:')

client.run(token)

