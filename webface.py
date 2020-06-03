import SimpleHTTPServer
import SocketServer

def runweb():

    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "localhost:",PORT
    httpd.serve_forever()

runweb()
