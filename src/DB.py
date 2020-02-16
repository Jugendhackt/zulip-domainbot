import datetime
import json
from os import getenv as ge


from pymongo import MongoClient


class DB:
    def __init__(self):
        self.__client = None
        self.db = None
        self.start()

    def start(self):
        self.__client = MongoClient(host=ge('DBLocation'), port=int(ge("DBPort")), username=ge("DBUser"),
                                    password=ge("DBPassword"), authSource=ge("DBAuthSource"),
                                    authMechanism=ge("DBAuthMechanism"))
        self.db = self.__client.asb

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

    def invite_user_to_project(self, user_email: str, project_name: str, admin_user: str):
        try:
            project = list(self.db.projects.find({"useremail": admin_user, "projectname": project_name}))
            user_project = list(self.db.projects.find({"useremail": user_email, "projectname": project_name}))
            if len(project) == 0:
                return 1

            if len(user_project) > 0:
                return 2

            self.db.projects.insert_one({"useremail": user_email, "projectname": project_name})
            return 0
        except Exception as e:
            print(e)
            return -1

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
