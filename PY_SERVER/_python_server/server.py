class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers();
    
    self.wfile.write(b"<!DOCTYPE html>")
    self.wfile.write(b"<html lang='en'>")
    self.wfile.write(b"<head>")
    self.wfile.write(b"<title>TMM Python</title>") 
    self.wfile.write(b"</head>")
    self.wfile.write(b"</html")
    
port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()
    
