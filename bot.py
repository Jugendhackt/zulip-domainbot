# General
import zulip
import threading
from DB import DB
from importlib import import_module
from os import listdir
from os.path import isfile, join

import zulip

from src.DB import DB

# Util import
from BotUtil import BotUtil
from WebServer import WebServer

dbinst = DB()
client = zulip.Client(config_file="zuliprc")
t1 = threading.Thread(target = WebServer().start)
t1.start()

class BotHandler(object):
    def usage(self):
        # Dynamically load the commands
        dir_path = './src/commands/'
        all_commands = [f for f in listdir(dir_path) if
                        isfile(join(dir_path, f)) and f != '__init__.py' and f.endswith('.py')]

        for cmd_file in all_commands:
            cmd = cmd_file.split('.')[0].lower()
            module = import_module(f"src.commands.{cmd}")
            COMMANDS[cmd] = module.CommandHandler()

        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message: list, bot_handler):
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

        msg = message['content'].split()

        if msg[0] in COMMANDS:
            COMMANDS[msg[0]].run(msg, message, bot_handler, dbinst)
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
