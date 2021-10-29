import discord
from discord.ext import commands
from discord_components import SelectOption, Select


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.config = self.client.GBC.config

    @commands.command()
    async def user(self, ctx, member: discord.Member = None, guild: discord.Guild = None):
        if member == None:
            member = ctx.message.author
        emb = discord.Embed(title="Информация о пользователе", color=self.config.get('colors')['blue'])
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

        emb = discord.Embed(title="Информация о Сервере", color=self.config.get('colors')['blue'])
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
        Bot = discord.Embed(title='О боте', color=self.config.get('colors')['blue'])
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
        embed = discord.Embed(title='Иконка пользователя', color=self.config.get('colors')['blue'])
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.config.get("mainGuilaId"))}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Information(client))