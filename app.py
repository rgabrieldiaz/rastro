from http.server import BaseHTTPRequestHandler
from pathlib import Path

_HTML_PATH = Path(__file__).resolve().parent / "index.html"


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = _HTML_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
