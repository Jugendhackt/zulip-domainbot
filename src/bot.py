class BotHandler(object):
    def usage(self):
        return "This bot registers Jugend hackt Subdomains"

    def handle_message(self, message, bot_handler):
        message_content = message["content"]

        if message_content == "test":
            content = "123"
        elif message_content == "bye":
            content = "Bye-bye"
        else:
            content = "hello, world!"

        bot_handler.send_reply(message, content)


handler_class = BotHandler
