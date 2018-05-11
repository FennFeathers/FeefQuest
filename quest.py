import discord
from discord.ext import commands

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

bot.run('NDQzNzI1NjY4NDYzOTM1NDg5.DddcrA.4uTsGpk6zm3SqpY0cmIGdYt4RZ0')
