#region imports
from typing import List
import discord
from config import color
#endregion

async def main(message: discord.Message, args: List[str], client: discord.Client):
    await message.channel.send(embed=discord.Embed(description="This is a sample command", color=color))


#region commandInfos needed
name = "sampleCommand"                                          # Name of the command
desc = "This is a Sample Command"                               # Description of the command
alias = ["sc"]                                                  # Alias
#endregion