    @commands.Cog.listener()
    async def on_message(self, ctx, msg):
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