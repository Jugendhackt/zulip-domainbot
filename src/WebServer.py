import http.server
import socketserver
from src.DB import DB

dbinst = DB

class WebServer:
    def start(self):
        PORT = 8000

        Handler = GetHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print("serving at port", PORT)
        httpd.serve_forever()

class GetHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        patharr = self.path.split("/")

        try:
            target = dbinst.getSlug(patharr[1])

            if (target != ""):
                self.send_response(301)
                self.send_header('Location','https://google.com')
                self.end_headers()
            else:
                self.send_response(404)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write(open("wspages/not-found.html"))
        except:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("<b>Unser flauschiger Suchtrupp macht grade pause.</b><br>Bitte komm' später nochmal wieder (500)".encode())
