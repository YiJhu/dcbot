import discord
import asyncio
import time, random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Discode Aria_helper is Online!')
        print('BOT NAME : %s'%(self.user.name))
        print('USER ID : %s' %(self.user.id))
        print('------'*5)

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = '歡迎 {0.mention} 加入 {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = '{0.mention} 離開了 {1.name} ...讓我們祝福他'.format(member, guild)
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('/game'):
            await message.channel.send('猜一個介於1到100之間的數字。')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 100)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('抱歉，您花了太長時間 {}。'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('恭喜答對!')
            else:
                await message.channel.send('很抱歉，正確答案是 {}。'.format(answer))

        if message.content.startswith('hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('/get_my_name'):
            await message.channel.send('%s' %(message.author))
        if message.content.startswith('/get_my_user_id'):
            await message.channel.send('%s' %(message.author.id))
        if message.content.startswith('/time'):
            now = time.strftime('%Y-%m-%d %I:%M:%S %p')
            await message.channel.send('現在時間 %s' %(now))
        if message.content.startswith('/me'):
            await message.channel.send('{0.author.mention}'.format(message))
        if message.content.startswith('/help'):
            await message.channel.send("【一般指令】\n[/me]\n[/time]\n[/get_my_name]\n[/get_my_user_id]\n[/game]")
###############################################################################
        elif message.author.id == "386776879161671681":
            return
        
        if message.content.startswith('/send:'):
            msg_x = message.content[6:]
            await message.channel.send('%s' %(msg_x))
        if message.content.startswith('/help'):
            await message.channel.send('\n\n【進階指令】\n[/send:]\n[/Aria:off]')
        if message.content.startswith('/Aria:off'):
            await message.channel.send('即將終止程式!')
            await client.close()
        
            
client = MyClient()
client.run('NzQ2MjY5NTE3MzM1NzU2ODEw.Xz93pQ.18MJ89K8cNjZCcIDsuxAv4VmHzE')
