import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="DN-Team|Aria helper"))
    print('Discode Aria_helper is Online!')
    print('BOT NAME : %s'%(bot.user.name))
    print('USER ID : %s' %(bot.user.id))
    print('------'*5)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run('NzQ2MjY5NTE3MzM1NzU2ODEw.Xz93pQ.18MJ89K8cNjZCcIDsuxAv4VmHzE')
