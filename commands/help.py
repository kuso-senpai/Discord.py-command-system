#region imports
from typing import List
import discord
from config import color
#endregion

async def main(message: discord.Message, args: List[str], client: discord.Client):
    
    helpEmbed = discord.Embed()
    helpEmbed.set_author(name="Help", url=client.user.avatar_url)

    from modules.botCommands import getCommands
    for c in getCommands():
        helpEmbed.add_field(name=c.name, value=c.desc, inline=False)
    helpEmbed.color = color
    await message.channel.send(embed=helpEmbed)


#region commandInfos needed
name = "help"                                                 # Name of the command
desc = "Help with all commands"                               # Description of the command
alias = ["?"]                                                 # Alias
#endregion