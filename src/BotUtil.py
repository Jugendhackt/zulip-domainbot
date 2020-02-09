import zulip

class BotUtil:
    @staticmethod
    def getUserByTag(usertag: str):
        usertag = BotUtil.cleanUsertag(usertag)
        for user in BotUtil.getAllUsers()["members"]:
            if (user["full_name"] == usertag):
                return user


    @staticmethod
    def getAllUsers():
        client = zulip.Client(config_file="zuliprc")
        return client.get_members()

    @staticmethod
    def cleanUsertag(usertag: str):
        return usertag.replace("@", "").replace("*", "")