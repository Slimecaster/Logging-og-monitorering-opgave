# controller.py
import logging
import http.server
import socketserver

logger = logging.getLogger(__name__)

PORT = 8000

class LoggingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logger.info(f"{self.address_string()} - {format % args}")

Handler = LoggingHTTPRequestHandler

def do_something():
    logger.info('Doing something')

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logger.info(f"Serving at port {PORT}")
        httpd.serve_forever()







