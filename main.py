from discord.ext import commands
from modules import config
config = config.configs("config")


def get_prefix(bot, msg):
    prefixes = [config.get("prefix"), f'<@{bot.user.id}>']
    # Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)


bot = commands.Bot(command_prefix=get_prefix, description='')
exts = ['cogs.music']  # Add your Cog extensions here


for i in exts:
    bot.load_extension(i)
    print(f'cog: {i} connect')

def run():
    bot.run(config.get('token'))

if __name__ == '__main__':
    run()
