import http.server
import socketserver
from os.path import sep

from src.DB import DB

dbinst = DB()


# Webserver to serve shortlinks created by the bot
class WebServer:

    # Start method of the server
    def start(self):
        PORT = 8000

        handler = GetHandler
        httpd = socketserver.TCPServer(("", PORT), handler)
        print("serving at port", PORT)
        httpd.serve_forever()


# Handler handling get requests to the webserver
class GetHandler(http.server.SimpleHTTPRequestHandler):

    # 
    def do_GET(self):
        patharr = self.path.split("/")

        if patharr[1] == "assets":
            self.send_response(200)
            self.send_header('Content-type', 'image/svg+xml')
            self.end_headers()
            self.wfile.write(open(f'.{sep}src{sep}wspages{sep.join(patharr)}', "r").read().encode())

        else:
            if len(patharr) > 2 and patharr[2] == "info":
                target = dbinst.get_slug(patharr[1])
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write(
                    open(f'.{sep}src{sep}wspages{sep}slug-info.html', "rb").read().replace("{creatorName}".encode(),
                                                                                           target[
                                                                                               "creatorName"].encode()).replace(
                        "{slug}".encode(), patharr[1].encode()).replace("{timestamp}".encode(),
                                                                        target["timestamp"].encode()))
            else:
                try:
                    target = dbinst.get_slug(patharr[1])

                    if target is not None:
                        print(target)
                        self.send_response(301)
                        self.send_header('Location', target["target"])
                        self.end_headers()
                    else:
                        self.send_response(404)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        # Send the html message
                        self.wfile.write(open(f'.{sep}src{sep}wspages{sep}not-found.html', "rb").read())
                except Exception as e:
                    print(e)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    # Send the html message
                    self.wfile.write(open(f'.{sep}src{sep}wspages{sep}internal-server-error.html', "rb").read())
