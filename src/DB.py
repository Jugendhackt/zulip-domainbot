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

    # project management

    def create_project(self, project_name: str, admin_user: str) -> bool:
        """
        Creates the project
        :param project_name:
        :param admin_user:
        :return:
        """
        projects = list(self.db.projects.find({"name": project_name}))
        if len(projects) == 0:
            # Create project
            insert_project = self.db.projects.insert_one({"name": project_name, "description": ""})
            # Create MongoDB object
            self.db.user_projects.insert_project.inserted_id
        else:
            return False
        pass

    def add_user_to_project(self, project_name: str, user_email: str):
        """
        Adds an user to the project
        :param project_name:
        :param user_email:
        :return:
        """
        pass
