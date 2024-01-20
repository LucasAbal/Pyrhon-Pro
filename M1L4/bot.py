import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5,*,mesnaje="hola"):
    await ctx.send(mesnaje * count_heh)

bot.run("MTE5NTg1MDc0MTA1NTc2MjQ5Mg.Gep-Bn.txgDfH9r0aN-R90gz779O3_P5ON4T2alb9LPHc")