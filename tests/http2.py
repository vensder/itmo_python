import SimpleHTTPServer
import SocketServer
import sys

PORT = 5555

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)

#sys.stderr = open('logfile.txt', 'a')
httpd.serve_forever()
