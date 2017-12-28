import shutil
import logging
import traceback
import configparser
from .config import Config, ConfigDefaults
import discord

log = logging.getLogger(__name__)


class PermissionsDefaults:
    perms_file = 'config/permissions.ini'
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

        serverconf = configparser.ConfigParser(interpolation=None)
        serverconf.read(PermissionsDefaults.serverconf_file, encoding='utf-8')
        for section in serverconf.sections():
            serverID = serverconf.get(section, 'GuildID')
            self.serverroles = {serverconf.get(section, 'GuildID'): {'Admins': [], 'Mods': []}}
            if not serverconf.get(section, 'Admin_roles') and :
                pass
            else:
                self.serverroles[serverconf.get(section, 'GuildID')]['Admins'].append(serverconf.get(section, 'Admin_roles'))


class test:
    def test():
        mytest = Permissiongroups(PermissionsDefaults.perms_file)
        print(mytest.serverroles)
