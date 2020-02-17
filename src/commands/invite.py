from src.BotUtil import BotUtil


class CommandHandler:
    usage = "invite <Mention> <Projektname>"

    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        invite_user = BotUtil.get_user_by_tag(msg_arr[0])
        invite_project = msg_arr[1]
        resp = dbinst.invite_user_to_project(invite_user['email'], invite_project, message['sender_email'])

        if resp == 0:
            content = f"*{invite_user['full_name']}* wurde erfolgreich zu *{invite_project}* hinzugefügt!"
        elif resp == 1:
            content = f"*{invite_project}* gehört **nicht** dir!"
        elif resp == 2:
            content = f"*{invite_user['full_name']}* wurde bereits dem Projekt {invite_project} hinzugefügt"
        else:
            content = "An error occurred, please refer to an admin"

        bot_handler.send_reply(message, content)
