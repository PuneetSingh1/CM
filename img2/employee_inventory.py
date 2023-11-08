import http.server
import socketserver

# Set the port on which you want to run the server
port = 8000

# Create a custom handler to serve your HTML file
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

# Start the HTTP server
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()

