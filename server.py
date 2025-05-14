from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

# Start the HTTP server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
