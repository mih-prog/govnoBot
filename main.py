import discord
from discord.ext import commands
from modules import config, logger, utils
import motor.motor_asyncio

config = config.configs("config")


def get_prefix(bot, msg):
    prefixes = [config.get("prefix"), f'<@{bot.user.id}>']
    # 1 префикс из конфигов. 2 упоминание бота как префикс

    return commands.when_mentioned_or(*prefixes)(bot, msg)

class govnoBotComponents:
    # класс для обращения к конфигам и бд из любова cog'а.
    config = config
    utils = utils.Utils(config)
    utils.checkConfigs(correction = True)
    logger = logger.log(config)
    if config.get('mongoDbPassword') is None or config.get('mongoDbLogin') is None :
        raise Exception
    __client = motor.motor_asyncio.AsyncIOMotorClient(F"mongodb+srv://{config.get('mongoDbLogin')}:{config.get('mongoDbPassword')}@maindb.dyjqs.mongodb.net/maindb?retryWrites=true&w=majority")
    db = __client.botdb

client = commands.Bot(command_prefix=get_prefix, description='', Intents=discord.Intents.all())  # создание клиента
client.remove_command('help')
client.GBC = govnoBotComponents  # вставка класса в класс client

exts = [
    'cogs.music', 
    'cogs.Information',
    'cogs.events',
    'cogs.help',
    ]  # list с путями к cog'ам, при создании cog'а добавить его сюда


for i in exts:  # цикл который добовляет cog'и
    client.load_extension(i)
    print(f'cog: {i} connect')

def run(): # функция для запуска бота при импорте этого файла
    client.run(config.get('token'))

if __name__ == '__main__':  # выполняется при запус 
    run()
