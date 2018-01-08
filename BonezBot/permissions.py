import shutil
import logging
import traceback
import configparser
from .config import Config, ConfigDefaults
import discord
from bot import bot as bot

log = logging.getLogger(__name__)


class PermissionsDefaults:
    bot_configs = Config(ConfigDefaults.options_file)
    serverconf_file = 'config/servers.ini'

    CommandWhiteList = set()
    CommandBlackList = set()
    GrantToRoles = set()
    UserList = set()

class Permissiongroups:
    def __init__(self, config_file):
        self.OwnerID = PermissionsDefaults.bot_configs.owner_id
        self.DevIDs = PermissionsDefaults.bot_configs.dev_ids
        self.serverroles ={}
        self.AdminRoles = []
        self.BotModRoles = []
        self.ModRoles = []
        serverconf = configparser.ConfigParser(interpolation=None)
        serverconf.read(PermissionsDefaults.serverconf_file, encoding='utf-8')

        for section in serverconf.sections():
            if not serverconf.get(section, 'Admin_Roles'):
                print('No Admin Roles set! For: ' + section)
            else:
                adminroles = serverconf.get(section, 'Admin_Roles').split(', ')
                for roleID in adminroles:
                    self.AdminRoles.append(roleID)

            if not serverconf.get(section, 'BotMod_Roles'):
                print('No Bot Mod set! For: ' + section)
            else:
                adminroles = serverconf.get(section, 'BotMod_Roles').split(', ')
                for roleID in adminroles:
                    self.BotModRoles.append(roleID)

            if not serverconf.get(section, 'Mod_Roles'):
                print('No Mod Roles set! For: ' + section)
            else:
                adminroles = serverconf.get(section, 'Mod_Roles').split(', ')
                for roleID in adminroles:
                    self.ModRoles.append(roleID)

class permissions:
    def __init__(self, configfile,bot):
        serverconf = configparser.ConfigParser(interpolation=None)
        serverconf.read(PermissionsDefaults.serverconf_file, encoding='utf-8')
        self.AdminPerms = serverconf.get('Permissions', 'Admin_Perm').split(', ')
        self.BotModPerms = serverconf.get('Permissions', 'BotModPerm').split(', ')
        self.ModPerms = serverconf.get('Permissions', 'Mod_Perm').split(', ')
        self.bot = bot


class test:
    def test():
        mytest1 = Permissiongroups(ConfigDefaults.options_file)
        mytest2 = permissions(configfile=ConfigDefaults.options_file, bot=bot)
        print(mytest1.AdminRoles)
