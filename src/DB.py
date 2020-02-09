import json

class DB:
    def start:
        cfg = readConfig()

    def readConfig():
        f = open("mongocfg", "r")
        cfg = json.loads(f.read()))
        return cfg