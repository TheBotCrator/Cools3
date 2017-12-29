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
        self.AdminRoles = []
        serverconf = configparser.ConfigParser(interpolation=None)
        serverconf.read(PermissionsDefaults.serverconf_file, encoding='utf-8')

        for section in serverconf.sections():
            if not serverconf.get(section, 'Admin_roles'):
                print('No Admin Roles set! For: ' + section)
            else:
                adminroles = serverconf.get(section, 'Admin_roles').split(', ')
                for roleID in adminroles:
                    self.AdminRoles.append(roleID)


class test:
    def test():
        mytest = Permissiongroups(ConfigDefaults.options_file)
        print(mytest.AdminRoles)
