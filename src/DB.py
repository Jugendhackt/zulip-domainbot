import json
from pymongo import MongoClient

class DB:

    def __init__(self):
        self.client = None
        self.db = None

    def start(self):
        cfg = self.readConfig()
        self.__client = MongoClient(host=cfg.location, port=cfg.port, username=cfg.user, password=cfg.password, authSource=cfg.authSource, authMechanism=cfg.authMechanism)
        self.db = self.__client.asb

    def readConfig(self):
        f = open("mongocfg", "r")
        cfg = json.loads(f.read())
        return cfg