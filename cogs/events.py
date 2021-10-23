import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.GBC.logger.setLogChannel(self.client.get_channel(self.client.GBC.config.get("logChannelld")))
        await self.client.GBC.logger.sendLog('Bot is ready', type=self.client.GBC.logger.logInfo)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass


def setup(client):
    client.add_cog(Events(client))