"""
Die Index Datei die als erstes ausgeführt wird
"""


#region imports
import discord
from config import token, prefix
#endregion

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message: discord.Message):
    if(not message.content.startswith(prefix) and not message.content.startswith(f'<@!{client.user.id}>') and not message.content.startswith(f'<@{client.user.id}>')):
        return


    #region command Values
    messageWithoutPrefix: str = message.content.replace(prefix, "", len(prefix)).replace(f'<@!{client.user.id}> ', "", len(f'<@!{client.user.id}> ')).replace(f'<@{client.user.id}> ', "", len(f'<@{client.user.id}> '))
    command = messageWithoutPrefix
    command = command.split()[0] if len(command.split()) > 0 else command
    args = messageWithoutPrefix.split()[1:]
    #endregion

    from modules.botCommands import getCommands
    for c in getCommands():
        if c.name.lower() == command.lower() or command.lower() in map(lambda x: x.lower(), c.alias):
            try:
                await c.main(message, args, client)
            except Exception as ex:
                print(ex)
                await message.channel.send(embed=discord.Embed(title="Error", description=f"Sorry, ein Fehler ist aufgetreten!", color=0xFF0000))



client.run(token)