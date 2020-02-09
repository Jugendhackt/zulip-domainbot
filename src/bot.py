from commands.ASBHelp import ASBHelp

class BotHandler(object):
    def usage(self):
        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message, bot_handler):
        cmdDict = {
            "help": ASBHelp()
        }

        msg = message['content'].split(" ")
        if(msg[0] in cmdDict):
            cmdDict[msg[0]].run(msg, message, bot_handler)
        else:
            print(message)
            print(message['content'])



handler_class = BotHandler
