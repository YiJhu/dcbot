import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import datetime
from core.classes import Cog_Extension

class Owner(Cog_Extension):

    @cog_ext.cog_slash(name='load')
    @commands.is_owner()
    async def _load(self, ctx: SlashContext, extension):
        '''Load extension'''
        self.bot.load_extension(f'cmds.{extension}')
        embed = discord.Embed(title=f'Loaded {extension} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='reload')
    @commands.is_owner()
    async def _reload(self, ctx: SlashContext, extension):
        '''Reload extension'''
        self.bot.reload_extension(f'cmds.{extension}')
        embed = discord.Embed(title=f'Reload {extension} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='unload')
    @commands.is_owner()
    async def _unload(self, ctx: SlashContext, extension):
        '''Unload extension'''
        self.bot.unload_extension(f'cmds.{extension}')
        embed = discord.Embed(title=f'Unload {extension} success.', color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='send')
    @commands.is_owner()
    async def _send(self, ctx: SlashContext, *, msg:str):
        '''Send the text of the command'''
        await ctx.send('%s' %(msg))
    
    @cog_ext.cog_slash(name='del_msg')
    @commands.guild_only()
    @commands.is_owner()
    async def _del_msg(self, ctx: SlashContext, num:int):
        '''Delete the number of chat records in the server'''
        await ctx.channel.purge(limit = num+1)
        embed = discord.Embed(description=f"Delete {num} Msg", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='Aria_off')
    @commands.is_owner()
    async def _Aria_off(self, ctx: SlashContext):
        '''Terminate program execution'''
        embed = discord.Embed(description="即將終止程式", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])
        await self.bot.close()


def setup(bot):
    bot.add_cog(Owner(bot))
