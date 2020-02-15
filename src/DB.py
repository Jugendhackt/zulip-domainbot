import datetime
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

    def read_config(self):
        f = open("mongocfg", "r")
        cfg = json.loads(f.read())
        return cfg

    def get_projects(self, useremail: str):
        return list(self.db.projects.find({"useremail": useremail}))

    # project management

    def create_project(self, project_name: str, admin_user: str) -> int:
        """
        Creates the project
        :param project_name:
        :param admin_user:
        :return:
        """
        try:
            projects = list(self.db.projects.find({"projectname": project_name}))
            print(projects)
            if len(projects) == 0:
                # Create project
                insert_project = self.db.projects.insert_one({"projectname": project_name, "useremail": admin_user})
                return 0
            else:
                return 1
        except Exception as e:
            print(e)
            return -1

    def add_user_to_project(self, project_name: str, user_email: str):
        """
        Adds an user to the project
        :param project_name:
        :param user_email:
        :return:
        """
        pass

    def get_slug(self, slug):
        return self.db.shortlinks.find_one({"slug": slug})

    def set_slug(self, slug, creator, creatorName, target):
        return self.db.shortlinks.insert_one({
            "creator": creator,
            "creatorName": creatorName,
            "timestamp": str(datetime.datetime.now().timestamp()),
            "slug": slug,
            "target": target
        })
