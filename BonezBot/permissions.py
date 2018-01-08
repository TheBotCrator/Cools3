import shutil
import logging
import traceback
import configparser
from .config import Config, ConfigDefaults
import discord
from .bot import bot

log = logging.getLogger(__name__)


class PermissionsDefaults:
    bot_configs = Config(ConfigDefaults.options_file)
    serverconf_file = 'config/servers.ini'

    CommandWhiteList = set()
    CommandBlackList = set()
    GrantToRoles = set()
    UserList = set()


class Permissiongroups:
    def __init__(self):
        self.OwnerID = PermissionsDefaults.bot_configs.owner_id
        self.DevIDs = PermissionsDefaults.bot_configs.dev_ids
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


class Permissions:
    def __init__(self, Bot):
        serverconf = configparser.ConfigParser(interpolation=None)
        serverconf.read(PermissionsDefaults.serverconf_file, encoding='utf-8')
        self.AdminPerms = serverconf.get('Permissions', 'Admin_Perm').split(', ')
        self.BotModPerms = serverconf.get('Permissions', 'BotModPerm').split(', ')
        self.ModPerms = serverconf.get('Permissions', 'Mod_Perm').split(', ')
        self.bot = Bot


class Test:
    def test():
        mytest1 = Permissiongroups()
        mytest2 = Permissions(Bot=bot)
        print(mytest1.AdminRoles)
