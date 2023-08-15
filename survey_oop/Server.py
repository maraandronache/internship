from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from ValidationUtil import ValidationUtil

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("server.html", "r") as html_file:
            content = html_file.read()

        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        age = data.get("age")
        city = data.get("city")

        if not ValidationUtil.validate_number(age) or not ValidationUtil.validate_city(city):
            response_message = "Invalid input(s)"
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": response_message}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        response_message = "Survey submitted successfully"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": response_message}
        self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
