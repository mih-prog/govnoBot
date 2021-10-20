from discord.ext import commands
from modules import config
from utils import configUtils
config = config.configs("config")
configUtils.checkConfigs(config, correction = True)


def get_prefix(bot, msg):
    prefixes = [config.get("prefix"), f'<@{bot.user.id}>']
    # 1 префикс из конфигов. 2 упоминание бота как префикс

    return commands.when_mentioned_or(*prefixes)(bot, msg)

class govnoBotComponents:
    # класс для обращения к конфигам и бд из любова cog'а.
    config = config


client = commands.Bot(command_prefix=get_prefix, description='')  # создание клиента
client.remove_command('help')
client.GBC = govnoBotComponents  # вставка класса в класс клиент

exts = ['cogs.music', 'cogs.Information']  # list с путями к cog'ам, при создании cog'а добавить его сюда


for i in exts:  # цикл который добовляет cog'и
    client.load_extension(i)
    print(f'cog: {i} connect')

def run(): # функция для запуска бота при импорте этого файла
    client.run(config.get('token'))

if __name__ == '__main__':  # выполняется при запус 
    run()
