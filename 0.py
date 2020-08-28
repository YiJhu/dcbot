import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('Discode Aria_helper is Online!')
    print('BOT NAME : %s'%(client.user.name))
    print('USER ID : %s' %(client.user.id))
    print('------'*5)

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        text = '歡迎 {0.mention} 加入 {1.name}!'.format(member, guild)
        await guild.system_channel.send(text)

@client.event
async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel is not None:
        text = '{0.mention} 離開了 {1.name} ...讓我們祝福他'.format(member, guild)
        await guild.system_channel.send(text)

# send msg

@client.command()
async def speed(ctx):
    await ctx.send('%s s' %(client.latency))

@client.command()
async def time(ctx):
    import time
    now = time.strftime('%Y-%m-%d %I:%M:%S %p')
    await ctx.send('現在時間：%s' %(now))

@client.command()
async def myname(ctx):
    await ctx.send('%s' %(ctx.author))

@client.command()
async def myid(ctx):
    a = ctx.author
    await ctx.send('%s' %(a.id))






client.run('NzQ2MjY5NTE3MzM1NzU2ODEw.Xz93pQ.18MJ89K8cNjZCcIDsuxAv4VmHzE')