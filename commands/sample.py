import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

def register(client: commands.Bot):
    slash: SlashCommand = client.slash
    @slash.subcommand(base='bot', name="test", description="Testet den Bot")
    async def command(ctx: SlashContext):
        await ctx.send("Erfolgreich")
