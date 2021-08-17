import discord
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import create_option
import datetime
from core.classes import Cog_Extension

class Permissions(Cog_Extension):

    @cog_ext.cog_slash(name='ban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx: SlashContext, member: discord.Member, *, reason:str):
        '''Ban user from the server'''
        await member.ban(reason)
        embed = discord.Embed(title=f'Ban {member} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='kick', pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx: SlashContext, member: discord.Member, *, reason:str):
        '''Kick user out from the server'''
        await member.kick(reason)
        embed = discord.Embed(title=f'Kick out {member} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])
        






def setup(bot):
    bot.add_cog(Permissions(bot))