#region imports
from typing import List
import discord
from config import prefix, color
from modules.botCommands import getCommands, findCommand
#endregion

async def main(message: discord.Message, args: List[str], client: discord.Client):

    if(len(args) < 1):
        helpEmbed = discord.Embed(description=f"```css\nPrefix: {prefix}```")
        helpEmbed.set_author(name=f"Hilfe für {client.user.name}", icon_url=client.user.avatar_url)

        for c in getCommands():
            helpEmbed.add_field(name=c.name, value=c.desc, inline=False)
        helpEmbed.color = color
        await message.channel.send(embed=helpEmbed)
    else:
        # Command finden
        command = findCommand(args[0])

        if not command:
            return await message.channel.send(f"Tut mir leid, ich konnte den Befehl `{args[0].capitalize()}` nicht finden")

        nl = '\n'                           # NewLine in einer Variabe speichern, weil sonst bei den Beispielen nicht genutzt werden kann (es kommt Fehlermeldung wenn man '\n' in f"{}" benutzt)
        # Formatiert alle Infos in eine Nachricht:
        # 
        # Titel     =       Der name vom Command aber capitalized (test -> Test)
        # ::Beschreibung::
        # Benutzung
        # 
        await message.channel.send(embed=discord.Embed(color=color, title=command.name.capitalize(),
        description=f"{command.desc}\n\n**Benutzung:** ```{prefix}{command.usage}```\n**Beispiel{'e' if len(command.examples) > 1 else ''}:** ```\n{nl.join(map(lambda x: prefix + x, command.examples))}```\n**Alias{'e' if len(command.alias) > 1 else ''}:** {', '.join(map(lambda x: '`' + prefix + x + '`', command.alias))}"))
        


#region commandInfos needed
name = "help"                                                 # Command name
desc = "Die Befehlshilfe"                                     # Beschreibung
usage = "help (Befehl)"                                       # Benutzung
alias = ["?", "hilfe"]                                        # Alias
examples = ["help", "help sample"]                            # Beispiele
#endregion