#!/usr/bin/env python3
import http.server
import os

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]
        if not os.path.splitext(path)[1]:
            html_path = path.rstrip('/') + '.html'
            if os.path.exists('.' + html_path):
                self.path = html_path
        super().do_GET()

if __name__ == '__main__':
    http.server.test(HandlerClass=CleanURLHandler, port=8080, bind='localhost')
