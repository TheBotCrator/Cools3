from BonezBot import Commands
import os
from discord.ext import commands
from .config import Config, ConfigDefaults
from .permissions import Test
import random

__author__ = "SpBonez"
__version__ = "0.0.1"

modulePath = os.path.join(os.getcwd(), "BonezBot", "modules")

botconfig = Config(ConfigDefaults.options_file)
cmd_prefix = botconfig.command_prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(cmd_prefix), description='BonezBot Test Mode')

bot.remove_command('help')
Commands.load_all_modules(modulePath, bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    Test.test()

bot.run(botconfig._login_token)
