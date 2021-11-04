from discord import Embed, FFmpegPCMAudio, FFmpegOpusAudio
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
from asyncio import run_coroutine_threadsafe
from discord_components import SelectOption, Select
import requests

class Music(commands.Cog, name='Musique'):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True',}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        self.message = {}

    @staticmethod
    def parse_duration(duration):
        result = []
        m, s = divmod(duration, 60)
        h, m = divmod(m, 60)
        return f'{h}:{m}:{s}'

    @staticmethod
    def search(author, arg):
        with YoutubeDL(Music.YDL_OPTIONS) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)

        embed = (Embed(title='🎵 Сейчас играет :', description=f"[{info['title']}]({info['webpage_url']})", color=0x3498db)
                .add_field(name='Продолжительность', value=Music.parse_duration(info['duration']))
                .add_field(name='Песня запущена ', value=author)
                .add_field(name='С канала', value=f"[{info['uploader']}]({info['channel_url']})")
                .add_field(name="Очередь", value=f"Нет песен в очереди!")
                .set_thumbnail(url=info['thumbnail']))

        return {'embed': embed, 'source': info['formats'][3]['url'], 'title': info['title']}

    async def edit_message(self, ctx):
        embed = self.song_queue[ctx.guild][0]['embed']
        content = "\n".join([f"({self.song_queue[ctx.guild].index(i)}) {i['title']}" for i in self.song_queue[ctx.guild][1:]]) if len(self.song_queue[ctx.guild]) > 1 else "Нет песен в очереди!"
        embed.set_field_at(index=3, name="Песни в очереди :", value=content, inline=False)
        await self.message[ctx.guild].edit(embed=embed)

    def play_next(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if len(self.song_queue[ctx.guild]) > 1:
            del self.song_queue[ctx.guild][0]
            run_coroutine_threadsafe(self.edit_message(ctx), self.bot.loop)
            voice.play(FFmpegPCMAudio(self.song_queue[ctx.guild][0]['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)
            run_coroutine_threadsafe(self.message[ctx.guild].delete(), self.bot.loop)

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, video: str):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        song = Music.search(ctx.author.mention, video)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if not voice.is_playing():
            self.song_queue[ctx.guild] = [song]
            self.message[ctx.guild] = await ctx.send(embed=song['embed'])
            await ctx.message.delete()
            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        else:
            self.song_queue[ctx.guild].append(song)
            await self.edit_message(ctx)

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await ctx.message.delete()
            if voice.is_playing():
                await ctx.send('⏸️ Музыка на паузе!', delete_after=5.0)
                voice.pause()
            else:
                await ctx.send('⏯️ Музыка снята с паузы!', delete_after=5.0)
                voice.resume()

    @commands.command(aliases=['pass'])
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            await ctx.message.delete()
            await ctx.send('⏭️ Песня пропущена!', delete_after=5.0)
            voice.stop()

    @commands.command(brief='.remove')
    async def remove(self, ctx, *, num: int):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            del self.song_queue[ctx.guild][num]
            await ctx.message.delete()
            await self.edit_message(ctx)


def setup(bot):
    bot.add_cog(Music(bot))
