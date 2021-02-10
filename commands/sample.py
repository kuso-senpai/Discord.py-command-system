#region imports
from typing import List
import discord
from config import color
#endregion

async def main(message: discord.Message, args: List[str], client: discord.Client):
    await message.channel.send(embed=discord.Embed(description="This is a sample command", color=color))


#region commandInfos needed
name = "sampleCommand"                                          # Name
desc = "Das hier ist ein Beispiel Befehl"                       # Beschreibung
alias = ["sc", "sample"]                                        # Alias
usage = "sampleCommand"                                         # Benutzung
examples = ["sc", "sampleCommand"]                              # Beispiele
#endregion