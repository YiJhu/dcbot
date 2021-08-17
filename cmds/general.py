import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import time, datetime
from core.classes import Cog_Extension

class General(Cog_Extension):

    @cog_ext.cog_slash(name='ping')
    async def _ping(self, ctx: SlashContext):
        """Ping latency"""
        embed = discord.Embed(title="ping latency", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        command_latency = (datetime.datetime.utcnow() - ctx.created_at).total_seconds() * 1000
        embed.add_field(name="Command latency", value="%s ms" %(f'{round(command_latency)}'), inline=False)
        embed.add_field(name="Api latency", value="%s ms" %(f'{round(self.bot.latency*1000)}'), inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='time')
    async def _time(self, ctx: SlashContext):
        """Show now time (UTC+8)"""
        now = time.strftime('%Y-%m-%d %I:%M:%S %p')
        embed = discord.Embed(title="Now time", description="%s" %(now), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='my_name')
    async def _my_name(self, ctx: SlashContext):
        """Get your user name"""
        embed = discord.Embed(description="%s" %(ctx.author), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='server_id')
    @commands.guild_only()
    async def _server_id(self, ctx: SlashContext):
        """Get server system id"""
        embed = discord.Embed(title="server id", description="%s" %(ctx.guild.id), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='channel_id')
    @commands.guild_only()
    async def _channel_id(self, ctx: SlashContext):
        """Get server channel id"""
        embed = discord.Embed(title="Channel Name", description="%s" %(ctx.channel.name), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="channel id", value="%s" %(ctx.channel.id))
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='my_id')
    async def _my_id(self, ctx: SlashContext):
        """Get your system id"""
        embed = discord.Embed(description="%s" %(ctx.author.id), color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='tagme')
    async def _tagme(self, ctx: SlashContext):
        """Tag you"""
        #await ctx.send('{0.author.mention}'.format(ctx))
        embed = discord.Embed(description="{0.author.mention}".format(ctx) , color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='server_info')
    @commands.guild_only()
    async def _server_info(self, ctx: SlashContext):
        """Display status of the server"""
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_owner = ctx.guild.owner
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        embed = discord.Embed(title="Server info", color=0xfe5901, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Server Name", value="%s" %(server_name), inline=False)
        embed.add_field(name="Create Time", value="%s" %(server_create_date), inline=False)
        embed.add_field(name="Server Owner", value="%s" %(server_owner), inline=False)
        embed.add_field(name="Server Regin", value=ctx.guild.region, inline=False)
        embed.add_field(name="Total of people", value="%s" %(server_user), inline=False)
        embed.add_field(name="Total of text channel", value="%s" %(text_channel), inline=False)
        embed.add_field(name="Total of voice channel", value="%s" %(voice_channel), inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

    @cog_ext.cog_slash(name='user_info')
    @commands.guild_only()
    async def _user_info(self, ctx: SlashContext, *, user: discord.Member = None):
        """Get User Info"""
        user = user or ctx.author
        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'
        embed = discord.Embed(colour=user.top_role.colour.value, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User Name", value=user, inline=False)
        embed.add_field(name="Nick Name", value=user.nick if hasattr(user, "nick") else "None", inline=False)
        embed.add_field(name="Creat At", value=(user.created_at).strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Join At", value=(user.joined_at).strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="User Id", value=user.id, inline=False)
        embed.add_field(name="User Roles", value=show_roles,inline=False)
        embed.set_footer(text="Aria Helper")
        await ctx.send(embeds = [embed])

def setup(bot):
    bot.add_cog(General(bot))
