class Projects:
    def run(self, msgArr: list(), message: dict(), bot_handler, dbinst):
        content = dbinst.getProjects(message["sender_email"])
        if(len(content) != 0):
            c = []
            for p in content:
                c.append(p["projectname"])
            content = "\n * ".join(c)
            bot_handler.send_reply(message, "Du bist an folgenden Projekten beteiligt: \n * "+content)
        else:
            bot_handler.send_reply(message, "Du bist an keinen Projekten beteiligt")
