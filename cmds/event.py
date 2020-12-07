import discord
from discord.ext import commands
import asyncio, random, datetime
from core.classes import Cog_Extension


class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            text = '歡迎 {0.mention} 加入 {1.name}!'.format(member, guild)
            embed = discord.Embed(description="%s" %(text), color=0xfe5901, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Aria Helper")
            await guild.system_channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            text = '{0.mention} 離開了 {1.name} ...讓我們祝福他'.format(member, guild)
            embed = discord.Embed(description="%s" %(text), color=0xfe5901, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Aria Helper")
            await guild.system_channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            embed = discord.Embed(description="%s" %(error), color=0xff0000, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Aria Error!")
            await ctx.send(embed = embed)
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.startswith('game'):
            await msg.channel.send('猜一個介於1到100之間的數字。')

            def is_correct(m):
                return m.author == msg.author and m.content.isdigit()

            answer = random.randint(1, 100)

            try:
                guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await msg.channel.send('抱歉，您花了太長時間 {}。'.format(answer))

            if int(guess.content) == answer:
                await msg.channel.send('恭喜答對!')
            else:
                await msg.channel.send('很抱歉，正確答案是 {}。'.format(answer))

def setup(bot):
    bot.add_cog(Event(bot))
