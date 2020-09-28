import discord
from discord.ext import commands
import asyncio
from core.classes import Cog_Extension

class Owner(Cog_Extension):

    @commands.command()
    @commands.is_owner()
    async def send(self, ctx, *, msg):
        await ctx.send('%s' %(msg))
    
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def del_msg(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    @commands.is_owner()
    async def Aria_off(self, ctx):
        embed = discord.Embed(description="即將終止程式", color=0xfe5901)
        await ctx.send(embed = embed)
        await self.bot.close()


def setup(bot):
    bot.add_cog(Owner(bot))
