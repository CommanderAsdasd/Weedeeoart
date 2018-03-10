# C:/Python34/python.exe
# -*- coding: utf-8 -*-
import http.server
import socketserver

port = 8080
handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", port), handler)

httpd.serve_forever()