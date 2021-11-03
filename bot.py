import os
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()

class HALBot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.getenv('ACCESS_TOKEN'),
                         client_id=os.getenv('CLIENT_ID'),
                         prefix='!',
                         initial_channels=['HAL451'])

    async def event_ready(self):
        print('halbot is ready.')

    async def event_message(self, message):
        print(message.content)
        if message.content.startswith('!'):
            await self.handle_commands(message)

    @commands.command(name='test')
    async def test_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = HALBot()
bot.run()
