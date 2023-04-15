from colorama import Fore
from twitchio.ext import commands

from .config import BOTS, CHANNELS, TOKEN, USERNAME
from .suppress import Suppress


def run():
    bot = Bot()
    bot.run()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TOKEN, nick=USERNAME, prefix='!', initial_channels=CHANNELS
        )

        self.greetings = Suppress('greetings.tmp')

    async def event_ready(self):
        self.channel = self.get_channel(self.nick)

        print(
            Fore.GREEN
            + f'🎉 | Successfully connected to the channel @{self.nick} on Twitch.'
        )

    async def event_message(self, ctx):
        datetime = ctx.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        print(
            Fore.BLUE + f'💬 | {datetime} | @{ctx.author.name}: {ctx.content}.'
        )
        await self.handle_greeting(ctx)
        await self.handle_commands(ctx)

    async def event_command_error(error):
        print(Fore.RED + '⚠️ ' + error)

    async def handle_greeting(self, ctx):
        name = ctx.author.name
        if name not in BOTS and self.greetings.add(name):
            await ctx.channel.send(f'{name} olá! 👋')

    @commands.command(name='cmd')
    async def cmd_list(self, ctx):
        comandos = list(self.commands.keys())
        await ctx.send(
            f"""{ctx.author.name}, nossos comandos são: !
            {" | !".join(comandos)}."""
        )

    @commands.command(name='amor')
    async def cmd_love(self, ctx):
        await ctx.send('❤️ 🧡 💛 💚 💙 💜 🤎 🖤 🤍')

    @commands.command(name='tchau')
    async def cmd_bye(self, ctx):
        await ctx.send(
            f"""Obrigado por estar com a gente {ctx.author.name}! Você é 
            importante 🥰"""
        )

    @commands.command(name='lurk')
    async def cmd_lurk(self, ctx):
        await ctx.send(f'Obrigada pelo lurk {ctx.author.name}! 💜')

    @commands.command(name='bttv')
    async def cmd_bttv(self, ctx):
        await ctx.send(
            """blobDance ThisIsFine bongoTap POGSLIDE FireElmo NoGodNo SnoopPls 
            epicSax BBYodaS PepeDoor gopherDance HollowDance Gandalf CuteDog 
            WeSmart"""
        )

    @commands.command(name='tema')
    async def cmd_theme(self, ctx):
        await ctx.send('Moonlight II Italic')

    @commands.command(name='terminal')
    async def cmd_terminal(self, ctx):
        await ctx.send('https://bit.ly/3qTqJ3S')

    @commands.command(name='linux')
    async def cmd_linux(self, ctx):
        await ctx.send('Minha distro é a Debian 12 Bookworm RC1 (testing)')
        await ctx.send('https://www.debian.org/')

    @commands.command(name='playlists')
    async def cmd_playlists(self, ctx):
        await ctx.send('https://music.apple.com/profile/amandamx')
        await ctx.send('https://sptfy.com/6ClB')

    @commands.command(name='eastereggs')
    async def cmd_easter_eggs(self, ctx):
        await ctx.send(
            """Temos alguns easter eggs (segredos) por aqui, tente descobrir, 
            quer uma dica? Eles são comandos do chatbot..."""
        )

    @commands.command(name='links')
    async def cmd_links(self, ctx):
        await ctx.send('https://amandamartins.dev')

    @commands.command(name='doação')
    async def cmd_donate(self, ctx):
        await ctx.send('https://streamlabs.com/amandamartinsdev/tip')

    @commands.command(name='apelidos')
    async def cmd_nicknames(self, ctx):
        await ctx.send(
            """Meu nome é Amanda, mas tem quem me chame de Amandita (é! igual 
            os chocolates), Amandinha, Manguinha, Mandioquinha, Amora, Mandys 
            ou só Mandy."""
        )

    @commands.command(name='pronomes')
    async def cmd_pronouns(self, ctx):
        await ctx.send('Meus pronomes são ela/dela 👩‍💻')

    @commands.command(name='sobre')
    async def cmd_about(self, ctx):
        await ctx.send(
            """E aí? Beleza? Tenho 26 anos, sou Application Developer na IBM, 
            natural de São Paulo, capital, e morando em Santa Catarina."""
        )

    @commands.command(name='ghsponsors')
    async def cmd_gh_sponsors(self, ctx):
        await ctx.send(
            """🇧🇷 Agora temos GitHub Sponsors! Basta acessar o link e conferir 
            as opções e prêmios disponíveis!  🇨🇦 We now have GitHub Sponsors! 
            Just access the link and check out the available options and 
            prizes! https://github.com/sponsors/AmandaMartinsDev"""
        )

    @commands.command(name='tcc')
    async def cmd_tcc(self, ctx):
        await ctx.send(
            """Estamos desenvolvendo uma aplicação web para gestão escolar, 
            você pode conferir mais sobre nos links a seguir:"""
        )
        await ctx.send(
            """Infos: 
            https://www.linkedin.com/feed/update/urn:li:activity:7052806685341417472/"""
        )
        await ctx.send(
            'GitHub: https://amandamartinsdev.github.io/senac-escola/'
        )
        await ctx.send(
            'Documentação: https://github.com/AmandaMartinsDev/senac-escola'
        )

    @commands.command(name='mimo')
    async def cmd_mimo(self, ctx):
        await ctx.send(
            """Mimo é um app para aprender a criar sites, programar em Python, 
            bancos de dados SQL e mais! Tudo isso de uma forma divertida e rápida, 
            sendo que uma lição pode ser feita em menos de 5 minutos! Baixe já em 
            https://getmimo.com/invite/433tqi"""
        )

    @commands.command(name='mastodon')
    async def cmd_mastodon(self, ctx):
        await ctx.send(
            """Mastodon é uma rede social gratuita, open-source, 
            descentralizada, livre de anúncios e com diversas instâncias, 
            tendo cada uma seu time de moderação, regras e objetivos. Eu estou 
            na https://bolha.us, vem!"""
        )

    @commands.command(name='caverna')
    async def cmd_caverna(self, ctx):
        await ctx.send('Olha o Patocórnio ai! amanda257Patocornio')

    @commands.command(name='feministech')
    async def cmd_feministech(self, ctx):
        await ctx.send('Nós amamos a amanda257Feministech !')

    @commands.command(name='sejoga')
    async def cmd_se_joga(self, ctx):
        await ctx.send(
            """A "Se Joga!" nasceu com o objetivo de trazer mais mulheres para 
            o cenário dos games no Brasil com toda a segurança e apoio, sejam 
            elas desenvolvedoras, jogadoras ou produtoras de conteúdo.  
            Confira todas as novidades do projeto em 
            https://www.instagram.com/sejoga.garota"""
        )

    @commands.command(name='linuxtips')
    async def cmd_linuxtips(self, ctx):
        await ctx.send(
            """A LINUXtips é uma plataforma brasileira de treinamentos online, 
            inovadora e acessível com diversos cursos para você desenvolver 
            suas habilidades em áreas como DevOps, Desenvolvimento de 
            Software e Segurança da Informação. Confira mais em 
            https://www.linuxtips.io/"""
        )

    @commands.command(name='infopreta')
    async def cmd_infopreta(self, ctx):
        await ctx.send(
            """Quer montar um PC mas não sabe nada de hardware ou precisa de 
            ajuda para consertar o que você já tem? Chama a galera da 
            InfoPreta, https://www.instagram.com/infopreta 👩🏿‍🔧"""
        )
