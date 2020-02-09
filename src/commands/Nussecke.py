class Nussecke:
    def run(self, msgArr: list(), message: dict(), bot_handler, dbinst):
        content = ":nussecke:"
        bot_handler.send_reply(message, content)