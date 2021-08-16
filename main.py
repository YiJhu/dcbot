import discord
from discord.ext import commands
import os,  configparser

config = configparser.ConfigParser()
config.read(".\\config.ini")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config['bot_set']['prefix'],  intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="DN-Team|Aria helper"))
    print('Discord Aria_helper is Online!')
    print('BOT NAME : %s'%(bot.user.name))
    print('USER ID : %s' %(bot.user.id))
    print('------'*5)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(config['bot_login']['Token'])
