import json

from pymongo import MongoClient


class DB:
    def __init__(self):
        self.__client = None
        self.db = None
        self.start()

    def start(self):
        cfg = self.read_config()
        print(cfg)
        self.__client = MongoClient(host=cfg["location"], port=cfg["port"], username=cfg["user"],
                                    password=cfg["password"], authSource=cfg["authSource"],
                                    authMechanism=cfg["authMechanism"])
        self.db = self.__client.asb
        print('working')

    def read_config(self):
        f = open("mongocfg", "r")
        cfg = json.loads(f.read())
        return cfg

    def get_projects(self, useremail):
        return list(self.db.projects.find({"useremail": useremail}))
