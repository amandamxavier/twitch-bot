from ..utils.config import BOTS


class Hello:
    async def handle_hello(self, message):
            name = message.author.name
            if name not in BOTS and self.hello.add(name):
                await message.channel.send(f'{name} olá! 👋')
                