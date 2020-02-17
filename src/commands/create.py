from src.DNSManager import DNSManager


class CommandHandler:
    usage = "create <Projekt Name>"

    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        if not len(msg_arr) > 0:
            bot_handler.send_reply(message, ':cry:')
            return

        project_name = msg_arr[0]
        DNSManager.create_subdomain(project_name)
        resp = dbinst.create_project(project_name, message['sender_email'])

        if resp == 0:
            content = f"*{project_name}* erfolgreich erstellt: [{project_name}.alpaca.space](https://{project_name}.alpaca.space)!"
        elif resp == 1:
            content = f"Project *{project_name}* gibt es bereits!"
        else:
            content = "An error occurred, please refer to an admin!"

        bot_handler.send_reply(message, content)
