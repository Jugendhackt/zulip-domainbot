class CommandHandler:
    usage = "Projects zeigt eine Liste von Projekten, zu denen man gehört.\n*Benutzung:* `projects`"

    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        content = dbinst.get_projects(message["sender_email"])
        print(content)
        if len(content) != 0:
            c = []
            for p in content:
                c.append(p["projectname"])
            content = "\n * ".join(c)
            bot_handler.send_reply(message, "Du bist an folgenden Projekten beteiligt: \n * " + content)
        else:
            bot_handler.send_reply(message, "Du bist an keinen Projekten beteiligt")
