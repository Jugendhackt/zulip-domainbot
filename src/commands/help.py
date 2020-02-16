class CommandHandler:
    def run(self, msg_arr: list, message: dict, bot_handler, helper: dict):
        if len(msg_arr) == 0:
            content = "**Hilfe**\n\nEine Liste aller verfügbarer Commands:\n"
            for k in helper.keys():
                content += f"* {k}\n"
        else:
            cmd = msg_arr[0].lower()
            if cmd in helper:
                content = f"**Hilfe ({cmd})**\n\n{helper[cmd]}"
            else:
                content = f"**Hilfe**\n\n Den Command {cmd} gibt es nicht!"

        bot_handler.send_reply(message, content)


usage = "help [<Command>]"
