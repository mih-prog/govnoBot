import discord
from discord.ext import commands
from discord_components import SelectOption, Select


helpCommands = {
    "info":{"name":"📒 Информация", "commands":[
            {"name":"help", "description":"Показывает команды"},
            {"name":"user", "description":"Показывает информацию о пользователе"},
            {"name":"guild", "description":"Показывает информацию о гильдии"},
            {"name":"bot", "description":"Показывает информацию о боте"},
            {"name":"icon", "description":"Показывает иконку пользователя"},
        ]},
    "moderation":{"name":"🖲️ Модерация", "private":True, "commands":[
            {"name":"clear", "arguments":"[количество]", "description":"Очищает чат"},
            {"name":"warn", "description":"🛠️ В разработке"},
            {"name":"warns", "description":"🛠️ В разработке"},
            {"name":"unwarn", "description":"🛠️ В разработке"},
            {"name":"mute", "description":"🛠️ В разработке"},
            {"name":"unmute", "description":"🛠️ В разработке"},
            {"name":"kick", "description":"🛠️ В разработке"},
            {"name":"ban", "description":"🛠️ В разработке"},

        ]},
    "levls":{"name":"🔰️ Уровни", "commands":[
            {"name":"levl", "description":"🛠️ В разработке"},
        ]},
    "music":{"name":"🎵 Музыка", "commands":[
            {"name":"play", "arguments":"[ссылка]", "description":"🛠️ В разработке"},
        ]},
    "entertainment":{"name":"🎉 Развлечения", "commands":[
            {"name":"pat", "description":"🛠️ В разработке"},
            {"name":"hug", "description":"🛠️ В разработке"},
            {"name":"kiss", "description":"🛠️ В разработке"},
        ]},
    "music":{"name":"💸 Экономика",},
    
}


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.config = self.client.GBC.config

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Команды бота', color=self.config.get('colors')['blue'])
        embed.set_thumbnail(url=self.client.user.avatar_url)
        options = []


        for classCommandIndex in helpCommands:
            classCommand = helpCommands.get(classCommandIndex)
            value = ""

            if classCommand.get("commands") is not None:
                options.append(SelectOption(label=classCommand.get("name"), value="help."+classCommandIndex))
                for command in classCommand.get("commands"):
                    value += command.get("name")+", "
                value = value[:-2]
            else:
                value = "🛠️ В разработке"
            embed.add_field(name=classCommand.get("name"), value=value, inline=False)

        components = [Select(placeholder='Выберете интресующию категорию', options=options)]

        embed.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.client.GBC.config.get("mainGuilaId"))}')
        await ctx.send(embed=embed, components=components)

    @commands.Cog.listener()
    async def on_select_option(self, interaction):
        print(interaction.user.name)
        try:
            pathOptions = interaction.values[0].split(".")
        except:
            pathOptions = []

        if pathOptions[0] == "help":
            embed = discord.Embed(color=self.config.get('colors')['blue'])

            embed.add_field(name=self.config.get('prefix')+'help',
                            value='Показывает команды',
                            inline=False)

            embed.add_field(name=self.config.get('prefix')+'user',
                            value='Показывает информацию о пользователе',
                            inline=False)

            embed.add_field(name=self.config.get('prefix')+'guild',
                            value='Показывает информацию о гильдии',
                            inline=False)
            
            embed.add_field(name=self.config.get('prefix')+'bot',
                            value='Показывает информацию о боте',
                            inline=False)
            
            embed.add_field(name=self.config.get('prefix')+'icon',
                            value='Показывает иконку пользователя',
                            inline=False)

            await interaction.respond(type=6)
            await interaction.send(embed=embed, components=[Select(placeholder='📒 Информация')], options=interaction.message.options)
        elif interaction.values[0] == "Help #2":
            
            embed = discord.Embed(color=self.config.get('colors')['blue'])
            embed.add_field(name='🖲️ Модерация',
                                value='clear [количество] - очищает чат\n''logs [On, Off] или logs [Clear_on, Clear_off] - включает логи или функции логов.\n'f'guild - показывает информацию о гильдии\n'f'bot - показывает информацию о боте\n''icon - показывает иконку пользователя\n',
                                inline=False)
            await interaction.respond(type=6)
            await interaction.send(embed=embed)


def setup(client):
    client.add_cog(Information(client))