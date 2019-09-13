from discord.ext import commands
from yangvstrump import yangvstrump
from primary import primary_polls

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command(pass_context=True)
async def primary(ctx):
    await primary_polls(ctx)


@bot.command(pass_context=True)
async def general(ctx):
    await yangvstrump(ctx)


bot.run('NjIxMzI3MDU2NzU5ODE2MjIz.XXjvSQ.9MA1fEHuBYKGaBZDyObbNkgkTOQ')
