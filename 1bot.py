import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = 'NTI3NDI2NzE5NjUzODIyNDY3.DwTkIA.qhlwyoj-dg3yQVzPwaV5gURmtqM'

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='.help'))
    print('Bot Is Ready')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def ping():
    await client.say('pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


client.run(TOKEN)
