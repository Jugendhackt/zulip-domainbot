class CommandHandler:
    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        # TODO: List all commands
        content = "Ich bin eine Hilfe"
        bot_handler.send_reply(message, content)
