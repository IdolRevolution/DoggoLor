import discord
from discord.ext import commands
from decouple import config

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
    print("Salve, Salve Yodinha!!!!")

@client.command()
async def ola(ctx):
    await ctx.send(f'Olá! {ctx.author}, quer um biscoito?')

client.run(config("DISCORD_TOKEN"))