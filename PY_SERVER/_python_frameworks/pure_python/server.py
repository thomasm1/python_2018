from os import path
from http.server import BaseHTTPRequestHandler, HTTPServer

from jinja2 import Template

class SimpleHandler(BaseHTTPRequestHandler):

    index_path = path.join(
        # Grab the parent directory path
        path.dirname(path.abspath(path.dirname(__name__))),
        "template",
        "index.html"
    )

    def do_GET(self):
        with open(str(self.index_path), 'r') as fstream:
            template = Template(fstream.read())
        output = template.render(
            title="Simple Http Server",
            description="Using pretty much pure python"
        )
        output = output.encode('ascii')
        # Send the response
        self.send_response(200)
        # Set the headers
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(output))
        # Finish the headers
        self.end_headers()
        # What happens if you pass a string rather than bytes?
        self.wfile.write(output)
        # Flush the output file
        self.wfile.flush()


if __name__ == "__main__":
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()