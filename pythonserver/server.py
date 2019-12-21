import os
from http.server import BaseHTTPRequestHandler
from pathlib import Path

from routes import routes

from response.badRequestHandler import BadRequestHandler
from response.templateHandler import TemplateHandler


class Server(BaseHTTPRequestHandler):

    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        if request_extension is "" or request_extension is ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()

        else:
            handler = BadRequestHandler()

        self.respond({
            'handler': handler
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()
        self.send_response(status_code)
        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 not found"

        self.end_headers()
        return bytes(content, "UTF-8")

    def respond(self, opts):
        content = self.handle_http(opts['handler'])
        self.wfile.write(content)
