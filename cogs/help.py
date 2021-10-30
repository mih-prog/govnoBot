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
        self.utils = self.client.GBC.utils

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Команды бота', color=self.config.get('colors')['blue'])
        embed.set_thumbnail(url=self.client.user.avatar_url)
        options = []


        for classCommandIndex in helpCommands:
            classCommand = helpCommands.get(classCommandIndex)
            value = ""
            if classCommand.get("private") is not True or self.utils.userIsPersonal(ctx.author.id):
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
        try:
            pathOptions = interaction.values[0].split(".")
        except:
            pathOptions = []

        if pathOptions[0] == "help":
            if pathOptions[1] == "main":
                await interaction.respond(type=6)
                await self.help(interaction)
            else:
                classCommand = helpCommands.get(pathOptions[1])
                embed = discord.Embed(title=classCommand.get("name"), color=self.config.get('colors')['blue'])
                embed.set_thumbnail(url=self.client.user.avatar_url)
                options = [SelectOption(label="main", value="help."+"main")]

                for command in classCommand.get("commands"):
                    if command.get("private") is not True or self.utils.userIsPersonal(interaction.user.id):
                        embed.add_field(name=self.config.get('prefix')+command.get("name"),
                                        value=command.get("description"),
                                        inline=False)
                
                for classCommandIndex in helpCommands:
                    classCommandFor = helpCommands.get(classCommandIndex)
                    if classCommandFor.get("private") is not True or self.utils.userIsPersonal(interaction.user.id):
                        if classCommandFor.get("commands") is not None:
                            options.append(SelectOption(label=classCommandFor.get("name"), value="help."+classCommandIndex))
                
                embed.set_footer(text=f'{self.client.user.name} | {self.client.get_guild(self.client.GBC.config.get("mainGuilaId"))}')
                components = [Select(placeholder=classCommand.get("name"), options=options)]
                await interaction.respond(type=6)
                await interaction.send(embed=embed, components=components)


def setup(client):
    client.add_cog(Information(client))