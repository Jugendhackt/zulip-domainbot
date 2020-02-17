class CommandHandler:
    usage = "help [<Command>]"

    def run(self, msg_arr: list, message: dict, bot_handler, helper: dict):
        if len(msg_arr) == 0:
            content = "**Hilfe**\n\nEine Liste aller verfügbaren Commands:\n"
            for k in helper.keys():
                content += f"* {k}\n"
        else:
            cmd = msg_arr[0].lower()
            if cmd in helper:
                content = f"**Hilfe ({cmd})**\n\n{helper[cmd]}"
            else:
                content = "**Hilfe**\n\nDiesen Command gibt es leider nicht :cry:\n\nEine Liste aller verfügbaren Commands:\n"
                for k in helper.keys():
                    content += f"* {k}\n"

        bot_handler.send_reply(message, content)
