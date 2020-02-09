from commands.Help import Help
from DB import DB

class BotHandler(object):
    dbinst

    def usage(self):
        global dbinst
        dbinst = DB()
        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message: list(), bot_handler):
        cmdDict = {
            "help": Help()
        }

        msg: list() = message['content'].split(" ")
        if(msg[0] in cmdDict):
            cmdDict[msg[0]].run(msg, message, bot_handler)
        else:
            print(message)
            print(message['content'])

            # https://nwex.de/skateRAUS.gif
            iamanundefinedfunction()



handler_class = BotHandler
