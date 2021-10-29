import time
import discord

class log():
    def __init__(self, config):
        self.__LogChennel = None
        self.__LogFile = open(config.get("LogFileName"), 'a', buffering=1)

        # type log
        self.logInfo = ("Info", discord.colour.Colour.dark_orange())
        self.logError = ("Error", discord.colour.Colour.dark_red())
        self.logDebug = ("Debug", discord.colour.Colour.dark_purple())


    def setLogChannel(self, Channel):
        self.__LogChennel = Channel

    async def sendLog(self, logText = None, type = None,  embed = None):
        if logText is not None:
            type = type if type is not None else self.logInfo

            log = f'{time.strftime("%a.%X")};{type[0]};{logText}'
            print(log)
            self.__LogFile.write(log+'\n')
            self.__LogFile.flush()
            embed = discord.Embed(title=f'log{type[0]}', description=logText, colour=type[1])
            await self.__LogChennel.send(embed=embed)
        elif embed is not None:
            log = f'{time.strftime("%a.%X")};{embed.title}:{embed.description}'
            print(log)
            self.__LogFile.write(log+'\n')
            self.__LogFile.flush()
            await self.__LogChennel.send(embed=embed)
        else:
            raise "invalid argument"
