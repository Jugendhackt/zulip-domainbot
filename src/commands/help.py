class CommandHandler:
    def run(self, msgArr: list(), message: dict(), bot_handler, dbinst):
        content = "Ich bin eine Hilfe"
        bot_handler.send_reply(message, content)