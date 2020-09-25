import discord
from discord.ext import commands
import asyncio
from core.classes import Cog_Extension

class General(Cog_Extension):
    
    @commands.command()
    async def speed(self, ctx):
        await ctx.send('%s s' %(self.bot.latency))

    @commands.command()
    async def time(self, ctx):
        import time
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        await ctx.send('現在時間：%s' %(now))

    @commands.command()
    async def my_name(self, ctx):
        await ctx.send('%s' %(ctx.author))

    @commands.command()
    async def server_id(self, ctx):
        a = ctx.guild
        await ctx.send('%s' %(a.id))

    @commands.command()
    async def my_id(self, ctx):
        a = ctx.author
        await ctx.send('%s' %(a.id))

    @commands.command()
    async def tagme(self, ctx):
        await ctx.send('{0.author.mention}'.format(ctx))

def setup(bot):
    bot.add_cog(General(bot))
