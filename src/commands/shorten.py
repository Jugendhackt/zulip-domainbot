import random
import string


class CommandHandler:
    def run(self, msg_arr: list, message: dict, bot_handler, dbinst):
        if len(msg_arr) == 1:
            bot_handler.send_reply(message,
                                   "Du kannst mich so um Short-URLs bitten: `@AlpacaSpaceBot shorten <url> [<slug>]`")
        else:
            if len(msg_arr) == 2:
                slg = self.generate_random_string()

                if dbinst.get_slug(slg) is None:
                    dbinst.set_slug(slg, message["sender_email"], message["sender_full_name"], msg_arr[1])
                    bot_handler.send_reply(message,
                                           "Short-URL erfolgreich erstellt :tada:\nhttps://alpaka.space/" + slg)
                else:
                    self.run(msg_arr, message, bot_handler, dbinst)

            else:
                if dbinst.get_slug(msg_arr[2]) is None:
                    dbinst.set_slug(msg_arr[2], message["sender_email"], message["sender_full_name"], msg_arr[1])
                    bot_handler.send_reply(message,
                                           "Short-URL erfolgreich erstellt :tada:\nhttps://alpaka.space/" + msg_arr[2])
                else:
                    bot_handler.send_reply(message, "**Der Slug " + msg_arr[
                        2] + " existiert leider schon.**\nSuch' dir bitte einen anderen aus oder lass' mich einen aussuchen.")

    def generate_random_string(self):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(8))


usage = "shorten <url> [<slug>]"