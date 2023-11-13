import http.server
import socketserver

# Set the port on which you want to run the server
port = 8000

# Create a custom handler to serve your HTML file
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            # http.server.SimpleHTTPRequestHandler.end_headers(self)
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

        elif self.path == '/inventory':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            # http.server.SimpleHTTPRequestHandler.end_headers(self)
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            super().do_GET()

# Start the HTTP server
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()

