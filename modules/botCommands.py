def getCommands(debugPrint = False):
    """Findet alle Befehle in dem `/commands/` Ordner, importiert diese und gibt ein Array mit allen Commands zurück"""
    # Alle Datei Befehle in einem Array
    commandFiles = []

    import os
    for file in os.listdir("commands"):
        if file.endswith(".py") and not file.startswith("__init__"):
            if debugPrint:
                print(os.path.join("commands", file))
            commandFiles.append(file)            # Fügt Datei zu Array zu

    if debugPrint:
        print(commandFiles)

    # Alle Befehle
    _commands = []

    for command in commandFiles:
        c = __import__("commands." + command.replace(".py", ""), globals(), locals(), [command])
        if debugPrint:
            print(c.name)
        _commands.append(c)     # Fügt Befehlobjekt zum Array

    return _commands


def findCommand(s: str):
    """Findet ein Befehl per Namen/Alias"""
    for c in getCommands():
        if s.lower() == c.name.lower() or s.lower() in map(lambda x: x.lower(), c.alias):
            return c