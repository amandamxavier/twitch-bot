from twitchio.ext import commands

from .utils.config import TOKEN, USERNAME, CHANNELS
from .utils.suppress import Suppress
from .commands.hello import Hello


def run():
    bot = Bot()
    bot.run()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=TOKEN, nick=USERNAME, prefix='!', initial_channels=CHANNELS)

        self.hello = Suppress('hello.tmp')

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(f'🎉 | Successfully connected to the channel @{self.nick} on Twitch.')

    async def event_message(self, message):
        print(f'💬 | {message.timestamp} | @{message.author.name}: {message.content}.')
        await Hello.handle_hello(self, message)

    async def event_command_error(self, error):
        print(error)
