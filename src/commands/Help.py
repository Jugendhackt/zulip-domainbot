class Help:
    def run(self, msgArr: list(), message: dict(), bot_handler):
        content = "Ich bin eine Hilfe"
        bot_handler.send_reply(message, content)