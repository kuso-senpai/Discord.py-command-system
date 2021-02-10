# Python Command System
Simples Command System für Discord.py

## How it works
Alle Befehle sind in dem `/commands/` Ordner

Ein Befehl ist wie folgt aufgebaut:

```python
async def main(message, args, client):
    # Your command code
name = "Command Name"
desc = "Die Beschreibung vom Befehl"
usage = "Die (Benutzung) [von dem Command]"
examples = ["Beispiel1", "Beispiel2"]
alias = ["commandAlias", "commandAlias2"]
```

Für mehr Infos, einfach `/commands/sample.py` angucken


### Update - Befehl erstellen per Command Line

Man kann jetzt einen Befehl einfach erstellen in CMD/Powershell/Terminal:


Im root ordner von dem Github Projekt hier folgende Befehle eingeben

```cmd
cd tools
python createCommand.py
```

Dann einfach den Anweisungen folgen und eine Datei wird in `/commands/` erstellt

Die Datei enthält dann alles was man braucht.

`pass` dann einfach wegmachen und durch den Command Code ersetzen


Beispiel:

**Der erstellte Befehl**
```
from typing import List
import discord

async def main(message: discord.Message, args: List[str], client: discord.Client):
    pass

name = "sampleCommand"                                          # Name
desc = "This is a Sample Command"                               # Beschreibung
alias = ["sc"]                                                  # Alias
usage = "sampleCommand"                                         # Benutzung
examples = ["sc"]                                               # Beispiele
```

**zu**

```
from typing import List
import discord

async def main(message: discord.Message, args: List[str], client: discord.Client):
    print("command aufgerufen")

name = "sampleCommand"                                          # Name
desc = "This is a Sample Command"                               # Beschreibung
alias = ["sc"]                                                  # Alias
usage = "sampleCommand"                                         # Benutzung
examples = ["sc"]                                               # Beispiele
```



## Help command

Ein _help_ Befehl ist schon erstellt

Durch `help Befehl` werden die Infos über einen Befehl gesendet

Mit `help` werden dann einfach alle Befehle angezeigt

## Wie der Hase läuft

Das meiste findet in `/modules/botCommands.py` statt. Dort wird einfach durch jede Datei im `/commands` Ordner durchgeguckt.
Es wird dann überprüft, ob der Command Name dem entspricht was gesendet wurde, oder ob das was gesendet wurde in den Aliasen
von einem Befehl enthalten ist. Wenn ja, wird dann die `main` Funktion aufgerufen und der Code ausgeführt.