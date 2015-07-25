#!/usr/bin/python

"""
Uses CGIHTTPServer to run a testing instance of Potassium.
"""

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/src"]

httpd = server(server_address, handler)
httpd.serve_forever()
