import http.server
import socketserver

PORT = 5000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
