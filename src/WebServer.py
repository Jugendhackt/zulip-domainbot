import http.server
import socketserver
from DB import DB

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
                self.wfile.write("<b>Wir haben eine ganze Herde Alpakas suchen geschickt. Keins ist zurückgekommen :/</b><br>Tipp: Achte auf Groß- und Kleinschreibung.".encode())
        except:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("<b>Unser flauschiger Schtrupp macht grade pause.</b><br>Bitte komm' später nochmal wieder (500)".encode())
