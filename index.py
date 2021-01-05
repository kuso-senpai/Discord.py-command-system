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
    #region command Values
    command = message.content.replace(prefix, "", len(prefix))
    command = command.split()[0]
    args = message.content.split()
    del args[0]
    #endregion

    from modules.botCommands import getCommands
    for c in getCommands():
        if c.name.lower() == command.lower() or command.lower() in map(lambda x: x.lower(), c.alias):
            try:
                await c.main(message, args, client)
            except Exception as ex:
                print(ex)
                message.channel.send(embed=discord.Embed(title="Error", description=f"Sorry, but an error occured!", color=0xFF0000))



client.login(token)