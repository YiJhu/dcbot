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
        embed = discord.Embed(title="bot latency", description="%s s" %(self.bot.latency), color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)

    @commands.command()
    async def time(self, ctx):
        """Show now time (UTC+8)"""
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        embed = discord.Embed(title="now time", description="%s" %(now), color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)

    @commands.command()
    async def my_name(self, ctx):
        """Get your user name"""
        embed = discord.Embed(description="%s" %(ctx.author), color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)

    @commands.command()
    @commands.guild_only()
    async def server_id(self, ctx):
        """Get server system id"""
        embed = discord.Embed(title="server id", description="%s" %(ctx.guild.id), color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)
        
        

    @commands.command()
    async def my_id(self, ctx):
        """Get your system id"""
        embed = discord.Embed(description="%s" %(ctx.author.id), color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)

    @commands.command()
    async def tagme(self, ctx):
        """Tag you"""
        #await ctx.send('{0.author.mention}'.format(ctx))
        embed = discord.Embed(description="{0.author.mention}".format(ctx) , color=0xfe5901, timestamp=datetime.datetime.now(tz=utc))
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(General(bot))
