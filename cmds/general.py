import discord
from discord.ext import commands
import asyncio
import datetime
import time
from core.classes import Cog_Extension

class General(Cog_Extension):

    @commands.command()
    async def speed(self, ctx):
        """Test bot latency"""
        await ctx.send('%s s' %(self.bot.latency))

    @commands.command()
    async def time(self, ctx):
        """Show now time (UTC+8)"""
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        await ctx.send('現在時間：%s' %(now))

    @commands.command()
    async def my_name(self, ctx):
        """Get your user name"""
        await ctx.send('%s' %(ctx.author))

    @commands.command()
    async def server_id(self, ctx):
        """Get server system id"""
        embed=discord.Embed(title="server id", description="%s" %(ctx.guild.id), color=0xfe5901)
        await ctx.send(embed=embed)
        
        

    @commands.command()
    async def my_id(self, ctx):
        """Get your system id"""
        embed=discord.Embed(title="user id", description="%s" %(ctx.author.id), color=0xfe5901)
        await ctx.send(embed=embed)

    @commands.command()
    async def tagme(self, ctx):
        """Tag you"""
        await ctx.send('{0.author.mention}'.format(ctx))

def setup(bot):
    bot.add_cog(General(bot))
