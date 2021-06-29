import os
import random
from pybooru import Danbooru
from dotenv import load_dotenv

# 1
from discord.ext import commands

client = Danbooru('danbooru')

load_dotenv()
TOKEN = os.getenv('TOKEN')

# 2
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="sfwyuri")
async def sfwyuri(ctx):
    yuri_list = client.post_list(limit="20", page=random.randint(1, 50), tags="yuri rating:safe")

    await ctx.message.delete()
    await ctx.send(yuri_list[random.randint(0, 19)].get("large_file_url"))


@bot.command(name="gm")
async def gm(ctx):
    await ctx.message.delete()
    await ctx.send("gm streaks")


@bot.command(name="sfwyuribomb")
async def sfwyuribomb(ctx):
    count = int(ctx.message.content.split(" ")[1])

    await ctx.message.delete()

    for i in range(count):
        yuri_list = client.post_list(limit="20", page=random.randint(1, 50), tags="yuri rating:safe")

        await ctx.send(yuri_list[random.randint(0, 19)].get("large_file_url"))


@bot.command(name="sfwyb")
async def sfwyuribombshortcut(ctx):
    await sfwyuribomb(ctx)


@bot.command(name="nsfwyuri")
async def nsfwyuri(ctx):
    yuri_list = client.post_list(limit="20", page=random.randint(1, 50), tags="yuri -rating:safe -age_difference")

    await ctx.message.delete()
    await ctx.send(yuri_list[random.randint(0, 19)].get("large_file_url"))

bot.run(TOKEN)
