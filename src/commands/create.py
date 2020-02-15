from src.DNSManager import DNSManager


class CommandHandler:
    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        if not len(msg_arr) > 1:
            bot_handler.send_message(':cry:', message)
            pass

        project_name = msg_arr[0]

        DNSManager.create_subdomain(project_name)

        dbinst.create_project(project_name, message['useremail'])


        # Add user to project

        pass
