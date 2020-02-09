class ASBHelp:
    def run(msgArr, message, bot_handler):
        content = "Ich bin eine Hilfe"
        bot_handler.send_reply(message, content)



        # bot_handler.send_message(dict(
        #     type='private',  # can be 'stream' or 'private'
        #     to="user330@community.jugendhackt.org",  # either the stream name or user's email
        #     subject="",  # message subject
        #     content="Jemand hat mir was geschieben",  # content of the sent message
        # ))