from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "" // ENTER YOUR IP
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "image/jpeg")
        self.end_headers()
        exec(open("./camera.py").read())
        in_file = open("image.jpg", "rb")
        data = in_file.read()
        in_file.close()
        self.wfile.write(bytes(data))
        #self.wfile.write(bytes(img.read()
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p?" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))
        #self.wfile.write(bytes(html, "utf-8"))
                         
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close()
    print("Server stopped.")
    
