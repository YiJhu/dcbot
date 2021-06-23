import discord
from discord.ext import commands
import asyncio
import datetime
import time
from core.classes import Cog_Extension

class About(Cog_Extension):

    @commands.command()
    async def botinfo(self, ctx):
        '''Bot Info'''
        embed = discord.Embed(description="Bot info", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Bot Name", value=ctx.bot.user.name, inline=False)
        embed.add_field(name="Creator", value="Michael Wu#4229 (<@!386776879161671681>)", inline=False)
        embed.add_field(name="Creat at", value=(ctx.bot.user.created_at).strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Service server", value=f"{len(self.bot.guilds)}", inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(About(bot))
