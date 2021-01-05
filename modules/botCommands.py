def getCommands(debugPrint = False):
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