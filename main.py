# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(10)
        folder = "." + self.path
        list_of_dir = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html>\n<head>\n<title>dish dish</title>\n</head>\n", "utf-8"))
        self.wfile.write(bytes("<body>\n", "utf-8"))
        for name in list_of_dir:
            self.wfile.write(bytes(f'<a href="{name}/">{name}<br></a>\n', "utf-8"))
        self.wfile.write(bytes("</body>\n</html>\n", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")