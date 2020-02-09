class BotHandler(object):
    def usage(self):
        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message, bot_handler):
        content = "beep"
        bot_handler.send_reply(message, content)


handler_class = BotHandler
