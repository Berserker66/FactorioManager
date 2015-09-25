__author__ = 'Fabian'

import configparser
from .paths import configpath


class ConfigManager():

    def __init__(self):
        self.config = configparser.ConfigParser()
        print(configpath)
        self.config.read(configpath)

class FactorioContainer():
    def __init__(self, name, binpath, modspath):
        self.binpath = binpath
        self.name = name
        self.modspath = modspath
    def _get(self):
        return self.name, self.binpath, self.modspath

configmanager = ConfigManager()