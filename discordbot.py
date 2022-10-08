import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load .env
load_dotenv()

PREFIX = os.environ.get('PREFIX')
TOKEN = os.environ.get('TOKEN')

# Intents 명시
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name}이 연결 되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def 안녕(ctx):
    await ctx.send('{}님, 반갑습니다.'.format(ctx.author.mention))


bot.run(TOKEN)
