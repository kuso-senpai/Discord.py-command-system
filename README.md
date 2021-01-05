# Python Command System
This is a simple command system for `discord.py`

## How it works
All you need is a folder (`/commands/`) with all your commands in it

A command should look like this

```python
async def main(message, args, client):
    # Your command code
name = "Your command name"
desc = "The Description of the command"
alias = ["commandAlias", "commandAlias2"]
```

For more information, look at a command sample in `/commands/sample.py`

## Help command

There is a default help command included, which will add a field for every command in `/commands/` and add the description as field value and the name from the command as the name of the field

## How it works

the module `botCommands.py` will check for every command in the `commands` folder and add it to an array

In the `index.py` file, it will check if the command in the message equals to the name of the current command in the for loop or the command in the message is included in the `alias` arayy. If yes, it will execute the `main` function