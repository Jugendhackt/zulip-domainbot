# General
import zulip
import re
from DB import DB
from os import listdir
from os.path import isfile, join
from importlib import import_module

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

        # Dynamically load the commands
        dir_path = './commands/'
        cmd_dict = dict()
        all_commands = [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and f != '__init__.py' and f.endswith('.py')]

        for cmd_file in all_commands:
            cmd = cmd_file.split('.')[0].lower()
            module = import_module(f"commands.{cmd}")
            cmd_dict[cmd] = module.CommandHandler()
            
        msg: list() = re.split(' +', message['content'])

        if msg[0] in cmd_dict:
            cmd_dict[msg[0]].run(msg, message, bot_handler, dbinst)
        else:
            print(message)
            print(message['content'])

            # https://nwex.de/skateRAUS.gif
            # iamanundefinedfunction()

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
