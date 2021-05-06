# Diese Datei ist dafür gedacht aus der command Line ausgeführt zu werden
#       Hier wird eine Datei erstellt für einen neuen Befehl
#
#               Diese Datei bitte NICHT importieren
#

from os import path

default_base = "test"

base = input("Command Gruppe: ").lower().replace(" ", "_")
base = base if base != "" else default_base

name = input("Befehlname: ").lower().replace(" ", "_")
beschreibung = input("Beschreibung: ")

print("Argumente")
print("Um die Argumentauswahl zu beenden, einfach beim namen enter drücken")

args = []
while True:
    _name = input("Name von Argument: ").lower().replace(" ", "_")
    if _name == "":
        break
    _description = input("Beschreibung vom Argument: ")
    _type = int(input("Typ: "))
    _pflicht = True if input("Pflicht?: ").lower() == "true" else False
    args.append((_name, _description, _type, _pflicht))

s = f"""import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

def register(client: commands.Bot):
    slash: SlashCommand = client.slash
    @slash.subcommand(base='{base}', name="{name}", description="{beschreibung}\""""
    
if len(args) > 0:
    s += """, options=["""

argsString = ""
for i in range(len(args)):
    arg = args[i]
    if(i > 0):  # Wenn momentanes argument nicht das erste ist
        s+=", "
    s += "{" + f'"name": "{arg[0]}", "description": "{arg[1]}", "type": {arg[2]}, "required": {arg[3]}' + "}"
    argsString += f", {arg[0]}{' = None' if arg[3] == False else ''}"
if len(args) > 0:
    s += "]"
s+= ")"
s += f"""
    async def command(ctx: SlashContext{argsString}):
        pass"""

filePath = f"{path.dirname(path.abspath(__file__))}{path.sep}..{path.sep}commands{path.sep}sora_{name}.py"
if(path.exists(filePath)):
    print("Diese Datei existiert schon")
    exit()

f = open(filePath, "w+", encoding="utf-8")
f.write(s)
f.close()
