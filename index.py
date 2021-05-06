import os
from os import path

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

from config import token

client = commands.Bot(command_prefix=";", help_command=None)
slash = SlashCommand(client, sync_commands=True, )
client.slash = slash

@client.listen('on_connect')
async def on_connect():
    filePath = f"{path.dirname(path.abspath(__file__))}{path.sep}"
    
    for x in [c for c in os.listdir(f"{filePath}/commands/") if c != "__init__.py" and c != "__pycache__"]:
        try:
            x = __import__(f"commands.{x.replace('.py', '')}", globals(), locals(), [x])
            x.register(client)
            print(f"✅ {x}")
        except Exception as x:
            print(f"❌ {x}\n{type(x)}")

@client.listen('on_ready')
async def on_ready():
    print("Ready")

client.run(token)
