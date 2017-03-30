from pathlib import Path, PurePath
import json


class ConfigReader:
    """Read configure information from a specified file"""

    FILENAME = 'conway.cfg'

    def __init__(self):
        self.width = 10
        self.height = 10
        self.numofseed = 50

    def read(self, path):
        try:
            config_file = open(str(PurePath(path, self.FILENAME)), 'r')
            config_json = json.load(config_file)
            self.width = config_json['width']
            self.height = config_json['height']
            self.numofseed = config_json['numofseed']
        except:
            config_file = open(str(PurePath(path, self.FILENAME)), 'w+')
            json.dump(self.__dict__, config_file)






