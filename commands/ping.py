import time
from datetime import datetime

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

def register(client: commands.Bot):
    slash: SlashCommand = client.slash
    @slash.subcommand(base='bot', name="ping", description="Gibt ping zurück")
    async def command(ctx: SlashContext):
        try:
            await ctx.respond(eat=True)
            x = current_milli_time()
            msg = await ctx.send("hmmm...")
            y = (current_milli_time() - x)
            await msg.delete()

            x_e= current_milli_time()
            msg = await ctx.send("hmmm schon wieder?")
            await msg.edit(content="ok.")
            y_e = current_milli_time() - x_e
            await msg.delete()
            await ctx.send(f"`{y}ms` gebraucht um zu senden\n`{y_e}ms` gebraucht zum editieren")
        except Exception as ex:
            print(
                f"\n{type(ex).__name__}: {ex}\n",
                f"{__file__}:{ex.__traceback__.tb_lineno}"
            )

current_milli_time = lambda: round(time.time() * 1000)
