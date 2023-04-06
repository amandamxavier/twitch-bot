from twitchio.ext import commands

from .config import TOKEN, USERNAME, CHANNELS, BOTS
from .suppress import Suppress


def run():
    bot = Bot()
    bot.run()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=TOKEN, nick=USERNAME, prefix='!', initial_channels=CHANNELS)

        self.greetings = Suppress('greetings.tmp')

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(f'🎉 | Successfully connected to the channel @{self.nick} on Twitch.')

    async def event_message(self, message):
        print(f'💬 | {message.timestamp} | @{message.author.name}: {message.content}.')
        await self.handle_greeting(self, message)

    async def event_command_error(self, error):
        print(error)

    async def handle_greeting(self, message):
        name = message.author.name
        if name not in BOTS and self.greetings.add(name):
            await message.channel.send(f'{name} olá! 👋')