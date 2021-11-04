from discord import Embed, FFmpegPCMAudio, FFmpegOpusAudio
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
from asyncio import run_coroutine_threadsafe
from discord_components import SelectOption, Select
import requests


class Music():
    def __init__(self, client) -> None:
        self.client = client
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True',}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


    @staticmethod
    def parse_duration(duration):
        m, s = divmod(duration, 60)
        h, m = divmod(m, 60)
        return f'{str(h)+":" if h > 0 else ""}{str(m)+":" if m > 0 or h > 0 else ""}{s if s > 10 else "0"+str(s)}'


def setup(bot):
    bot.add_cog(Music(bot))