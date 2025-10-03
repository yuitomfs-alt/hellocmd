import discord
from discord.ext import commands

TOKEN = 'MTQyMzUyOTU0MDI0ODAxNDk3MQ.Go3Qxs.G6F7CuY3CV60aZwbdNBOV7tp8scHlAau3z0nTI'
PREFIX = '!'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run(TOKEN)