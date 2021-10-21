import discord
from discord.ext import commands
from discord_components import DiscordComponents, SelectOption, Select


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.config = self.client.GBC.config

    @commands.command()
    async def help(self, ctx):
        Help = discord.Embed(title='Команды бота', color=self.config.get('blue'))
        Help.add_field(name='📒 Информация', value='help, user, guild, bot, icon', inline=False)
        Help.add_field(name='🖲️ Модерация', value='clear, logs, warn, warns, unwarn, mute, unmute, kick, ban',
                       inline=False)
        Help.add_field(name='🔰️ Уровни', value='lvl', inline=False)
        Help.add_field(name='🎵 Музыка', value='*🛠️ В разработке*', inline=False)
        Help.add_field(name='🎉 Развлечение', value='pat, hug, kiss', inline=False)
        Help.add_field(name='💸 Экономика', value='*🛠️ В разработке*', inline=False)
        Help.add_field(name='👋 Приветствие', value='welcome, welcome_chat, welcome_media, welcome_off', inline=False)
        Help.add_field(name='🎴 Прощание', value='goodbye, goodbye_chat, goodbye_media, goodbye_off', inline=False)
        Help.set_thumbnail(url=self.client.user.avatar_url)
        Help.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.client.GBC.config.get("mainGuilaId"))}')
        await ctx.send(embed=Help, components=[Select(placeholder='Выберете интресующию категорию', options=[
            SelectOption(label="📒 Информация", value="Help #1"),
            SelectOption(label="🖲️ Модерация", value="Help #2"),
            SelectOption(label="🔰️ Уровни", value="Help #3"),
            SelectOption(label="🎵 Музыка", value="Help #4"),
            SelectOption(label="🎉 Развлечение", value="Help #5"),
            SelectOption(label="💸 Экономика", value="Help #6"),
            SelectOption(label="👋 Приветствие", value="Help #7"),
            SelectOption(label="🎴 Прощание", value="Help #8"),
            SelectOption(label="🖨️ Логи", value="Help #9")
        ])])

    @commands.Cog.listener()
    async def on_select_option(self, interaction):
        print(1)
        try:
            await interaction.respond(type=6)
        except:
            pass
        if interaction.values[0] == "Help #1":
            Help = discord.Embed(color=self.config.get('blue'))
            Help.add_field(name='📒 Информация',
                           value='help - показывает команды\n''user - показывает информацию о пользователе\n'f'guild - показывает информацию о гильдии\n'f'bot - показывает информацию о боте\n''icon - показывает иконку пользователя\n',
                           inline=False)
            await interaction.channel.send(embed=Help)
        elif interaction.values[0] == "Help #2":
            Moderation = discord.Embed(color=self.config.get('blue'))
            Moderation.add_field(name='🖲️ Модерация',
                                 value='clear [количество] - очищает чат\n''logs [On, Off] или logs [Clear_on, Clear_off] - включает логи или функции логов.\n'f'guild - показывает информацию о гильдии\n'f'bot - показывает информацию о боте\n''icon - показывает иконку пользователя\n',
                                 inline=False)
            await interaction.send(embed=Moderation)

    @commands.command()
    async def user(self, ctx, member: discord.Member = None, guild: discord.Guild = None):
        if member == None:
            member = ctx.message.author
        emb = discord.Embed(title="Информация о пользователе", color=self.config.get('blue'))
        emb.add_field(name="👥Имя:", value=member.display_name, inline=False)
        emb.add_field(name="🆔:", value=member.id, inline=False)

        emb.set_thumbnail(url=member.avatar_url)

        status = member.status
        if status == discord.Status.online:
            d = "🟢В сети"
        elif status == discord.Status.offline:
            d = "🔘Не в сети"
        elif status == discord.Status.idle:
            d = "🌙Неактивен"
        elif status == discord.Status.dnd:
            d = "⛔️Не беспокоить"

        emb.add_field(name="💬Статус:", value=d, inline=False)
        emb.add_field(name="ℹ️ Пользовательский статус:", value=member.activity, inline=False)
        emb.add_field(name="⛑ Роль на сервере:", value=f"{member.top_role.mention}", inline=False)
        emb.add_field(name="🗓 Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=False)
        emb.add_field(name="🕓 Присоеденился к серверу:",
                        value=ctx.message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        emb.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.config.get("mainGuilaId"))}')
        await ctx.send(embed=emb)

    @commands.command()
    async def guild(self, ctx):
        guild = ctx.guild

        emb = discord.Embed(title="Информация о Сервере", color=self.config.get('blue'))
        emb.add_field(name="👥Название:", value=f"**{guild.name}**", inline=False)
        emb.add_field(name="🆔:", value=guild.id, inline=False)
        emb.add_field(name="🔱 Владелец:", value=guild.owner.mention, inline=False)
        emb.add_field(name="🌍 Регион:", value=guild.region, inline=False)
        emb.add_field(name="🎎 Количество участников:", value=guild.member_count, inline=False)
        emb.add_field(name="🕓 Создан сервер:", value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                      inline=False)
        emb.set_thumbnail(url=guild.icon_url)
        emb.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.config.get("mainGuilaId"))}')
        await ctx.send(embed=emb)

    @commands.command()
    async def bot(self, ctx):
        Bot = discord.Embed(title='О боте', color=self.config.get('blue'))
        Bot.add_field(name="👥 Назване:", value=f'{self.client.user.name}', inline=False)
        Bot.add_field(name="🛠️ Версия:", value=f'{self.config.get("version")}', inline=False)
        Bot.add_field(name="🛰️ Поддержка:", value=f'Поддержку видёт сервер {self.client.get_guild(self.config.get("mainGuilaId"))}', inline=False)
        Bot.add_field(name="🖱️ Разработчики:", value=f'{" ".join(["<@"+str(id)+">" for id in self.config.get("developersId")])}', inline=False)
        Bot.add_field(name="🔧 Тех-поддержка:", value=f'{self.config.get("invitationMainGildUrl")}', inline=False)
        Bot.set_thumbnail(url=self.client.user.avatar_url)
        Bot.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.config.get("mainGuilaId"))}')
        await ctx.send(embed=Bot)

    @commands.command()
    async def icon(self, ctx, user: discord.User = None):
        if not user:
            user = ctx.author
        embed = discord.Embed(title='Иконка пользователя', color=self.config.get('blue'))
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.config.get("mainGuilaId"))}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Information(client))