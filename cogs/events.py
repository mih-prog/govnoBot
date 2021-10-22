import discord
from discord.ext import commands
from discord_components import DiscordComponents, SelectOption, Select

green = 0x6DFC03
red = 0xFC0E03
blue = 0x1E90FD

class Db(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.GBC.logger.setLogChannel(self.client.get_channel(self.client.GBC.config.get("logChannelld")))
        self.client.GBC.logger.log('Bot is ready')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass


def setup(client):
    client.add_cog(Db(client))