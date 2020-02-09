# General
from DB import DB
import zulip

# Command imports 
from commands.Help import Help
from commands.Projects import Projects
from commands.Nussecke import Nussecke

# Util import
from BotUtil import BotUtil



dbinst = DB()
client = zulip.Client(config_file="zuliprc")

class BotHandler(object):
    def usage(self):
        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message: list(), bot_handler):
        rec = []

        try:
            for x in message["display_recipient"]:
                rec.append(x["email"])

            print(rec)
            client.set_typing_status({
                'op': 'start',
                'to': rec
            })
            pass
        except:
            pass
        

        global dbinst
        cmdDict = {
            "help": Help(),
            "projects": Projects(),
            "nussecke": Nussecke()
        }

        msg: list() = message['content'].split(" ")
        if(msg[0] in cmdDict):
            cmdDict[msg[0]].run(msg, message, bot_handler, dbinst)
        else:
            print(message)
            print(message['content'])

            # https://nwex.de/skateRAUS.gif
            iamanundefinedfunction()

        try:
            for x in message["display_recipient"]:
                rec.append(x["email"])

            print(rec)
            client.set_typing_status({
                'op': 'stop',
                'to': rec
            })
            pass
        except:
            pass



handler_class = BotHandler
