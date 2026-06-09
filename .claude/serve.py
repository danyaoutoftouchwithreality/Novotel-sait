import functools, http.server, socketserver, os
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 4521), Handler) as httpd:
    print("serving", DIR, "on 4521")
    httpd.serve_forever()
