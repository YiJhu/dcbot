import discord
from discord.ext import commands
import asyncio
from core.classes import Cog_Extension

class Owner(Cog_Extension):

    @commands.command()
    @commands.is_owner()
    async def send(self, ctx, msg):
        await ctx.send('%s' %(msg))

    @commands.command()
    @commands.is_owner()
    async def Aria_off(self, ctx):
        await ctx.send('即將終止程式!')
        await self.bot.close()


def setup(bot):
    bot.add_cog(Owner(bot))
