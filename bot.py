import discord
from discord.ext import commands

feefQuest.login('XVxJDf0wkm5wlQ32BseH7UijaEcSnDk9')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run()
