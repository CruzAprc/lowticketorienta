#!/usr/bin/env python3
"""Serve a LP clone em http://127.0.0.1:8281/"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".js": "application/javascript",
        ".css": "text/css",
        ".woff": "font/woff",
        ".woff2": "font/woff2",
        ".ttf": "font/ttf",
        ".svg": "image/svg+xml",
        ".mp4": "video/mp4",
        ".json": "application/json",
    }

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("0.0.0.0", 8281), Handler)
    print("LP clone em http://127.0.0.1:8281/")
    httpd.serve_forever()
