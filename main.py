import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os,  configparser

config = configparser.ConfigParser()
config.read(".\\config.ini")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=config['bot_set']['prefix'],  intents=intents)
slash = SlashCommand(bot, sync_commands=True, override_type = True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="DN-Team|Aria helper"))
    print(f'Discord BOT {bot.user.name} is Online!')
    print(f'BOT NAME : {bot.user.name}')
    print(f'USER ID : {bot.user.id}')
    print('------'*5)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(config['bot_login']['Token'])
