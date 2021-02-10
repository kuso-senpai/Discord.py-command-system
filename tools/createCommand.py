# Diese Datei ist dafür gedacht aus der command Line ausgeführt zu werden
#       Hier wird eine Datei erstellt für einen neuen Befehl
#
#               Diese Datei bitte NICHT importieren
#

dateiName = str(input("Datei name (ohne .py): "))
befehlName = str(input("Name von Befehl: "))
befehlBeschreibung = str(input("Beschreibung: "))
alias = str(input("Aliase (getrennt mit ', '): ")).split(", ")
benutzung = str(input("Benutzung: "))
beispiele = str(input("Beispiele (getrennt mit ', '): ")).split(", ")


char = "'"

sample = f"""
from typing import List
import discord

async def main(message: discord.Message, args: List[str], client: discord.Client):
    pass

name = '{befehlName}'
desc = '{befehlBeschreibung}'
alias = [{', '.join(map(lambda x: char + x + char, alias))}]
usage = '{benutzung}'
examples = [{', '.join(map(lambda x: char + x + char, beispiele))}]

"""

file = open(f"../commands/{dateiName}.py", "a")
file.write(sample)
file.close()