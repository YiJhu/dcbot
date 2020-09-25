import discord
from discord.ext import commands
import asyncio
from core.classes import Cog_Extension


class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            text = '歡迎 {0.mention} 加入 {1.name}!'.format(member, guild)
            await guild.system_channel.send(text)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            text = '{0.mention} 離開了 {1.name} ...讓我們祝福他'.format(member, guild)
            await guild.system_channel.send(text)

def setup(bot):
    bot.add_cog(Event(bot))
