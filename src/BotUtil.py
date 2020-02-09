import zulip


class BotUtil:
    @staticmethod
    def get_user_by_tag(usertag: str):
        usertag = BotUtil.clean_user_tag(usertag)
        for user in BotUtil.get_all_users()["members"]:
            if user["full_name"] == usertag:
                return user

    @staticmethod
    def get_all_users():
        client = zulip.Client(config_file="zuliprc")
        return client.get_members()

    @staticmethod
    def clean_user_tag(usertag: str):
        return usertag.replace("@", "").replace("*", "")
