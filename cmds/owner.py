import discord
from discord.ext import commands
import asyncio, datetime
from core.classes import Cog_Extension

class Owner(Cog_Extension):

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        '''Load extension'''
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension} success.')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        '''Reload extension'''
        self.bot.reload_extension(f'cmds.{extension}')
        embed = discord.Embed(title=f'Reload {extension} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        '''Unload extension'''
        self.bot.unload_extension(f'cmds.{extension}')
        embed = discord.Embed(title=f'Unload {extension} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.is_owner()
    async def send(self, ctx, *, msg:str):
        await ctx.send('%s' %(msg))
    
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def del_msg(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    @commands.is_owner()
    async def Aria_off(self, ctx):
        embed = discord.Embed(description="即將終止程式", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)
        await self.bot.close()


def setup(bot):
    bot.add_cog(Owner(bot))
