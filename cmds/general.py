import discord
from discord.ext import commands
import asyncio
import datetime
import time
from core.classes import Cog_Extension

class General(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        """Ping latency"""
        embed = discord.Embed(title="ping latency", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Bot latency", value="%s s" %(self.bot.latency), inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    async def time(self, ctx):
        """Show now time (UTC+8)"""
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        embed = discord.Embed(title="Now time", description="%s" %(now), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    async def my_name(self, ctx):
        """Get your user name"""
        embed = discord.Embed(description="%s" %(ctx.author), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.guild_only()
    async def server_id(self, ctx):
        """Get server system id"""
        embed = discord.Embed(title="server id", description="%s" %(ctx.guild.id), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)
        
        

    @commands.command()
    async def my_id(self, ctx):
        """Get your system id"""
        embed = discord.Embed(description="%s" %(ctx.author.id), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    async def tagme(self, ctx):
        """Tag you"""
        #await ctx.send('{0.author.mention}'.format(ctx))
        embed = discord.Embed(description="{0.author.mention}".format(ctx) , color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    async def server_info(self, ctx):
        """Display status of the server"
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        embed = discord.Embed(title="Server info", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Server Name", value="%s" %(server_name), inline=False)
        embed.add_field(name="Create Time", value="%s" %(server_create_date), inline=False)
        embed.add_field(name="Total of people", value="%s" %(server_user), inline=False)
        embed.add_field(name="Total of text channel", value="%s" %(text_channel), inline=False)
        embed.add_field(name="Total of voice channel", value="%s" %(voice_channel), inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(General(bot))
