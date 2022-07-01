import discord
import generateMsg

from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from dotenv import load_dotenv
import os

# Write a discord bot that uses gpt-3 to generate text.
# The bot should be able to generate text from a single command.

intents = discord.Intents.default()
intents.members = True

# Create a discord client
class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await self.change_presence(activity=discord.Game(name='Generating text...'))

    async def on_message(self, message):
        if not message.content.startswith("!"): return
        if message.author == self.user:
            return

        messageWithOutPrefix = message.content[1:]
        command = messageWithOutPrefix.split()[0]
        arguments = messageWithOutPrefix.split()[1:]
            

        if command == '!':
            # Make the bot look like it's typing
            await message.channel.trigger_typing()
            if len(arguments) == 0:
                await message.channel.send("usage: !generate <text>")
                return
            
            await message.channel.send(generateMsg.generate(" ".join(arguments)))
            # Make the bot look like it's not typing
            await message.channel.trigger_typing()
            return

        elif command == 'egg':
            await message.channel.send('spam')

        elif command == 'spam':
            for i in range(0, 5):
                await message.channel.send('UwU')

            print('spam')

load_dotenv()


client = Client()
client.run(os.getenv("DISCORD_TOKEN"))





