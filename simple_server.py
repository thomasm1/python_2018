from http.server import SimpleHTTPRequestHandler, HTTPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    try:
        server_address = ('localhost', 8001)
        httpd = HTTPServer(server_address, CORSRequestHandler)
        print(f"Serving on port {server_address[1]}...")
        httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")

