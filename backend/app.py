from http.server import BaseHTTPRequestHandler
from pathlib import Path

_BASE_DIR = Path(__file__).resolve().parent
_HTML_PATH = _BASE_DIR / "index.html"
_DECK_PATH = _BASE_DIR / "deck" / "index.html"
if not _DECK_PATH.exists():
    _DECK_PATH = _BASE_DIR / "deck.html"


def get_body(path: str) -> tuple[bytes, str]:
    if path.startswith("/deck"):
        if _DECK_PATH.exists():
            return _DECK_PATH.read_bytes(), "text/html; charset=utf-8"
    return _HTML_PATH.read_bytes(), "text/html; charset=utf-8"


def app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    body, ctype = get_body(path)
    start_response(
        "200 OK",
        [
            ("Content-Type", ctype),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]


application = app


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body, ctype = get_body(self.path)
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
