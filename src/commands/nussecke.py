class CommandHandler:
    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        content = ":nussecke:"
        bot_handler.send_reply(message, content)
