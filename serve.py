from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import codecs

#http://wiki.python.org/moin/BaseHttpServer

def get_content():

    f = codecs.open('name.raw', 'rb', 'utf-8')
    raw = f.read()
    f.close()
    return raw

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        body  = get_content()
        #http://bugs.python.org/issue1410
        body  = body.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Length', len(body)) 
        self.send_header('Content-Type', 'text/xml; charset=utf-8') 
        self.end_headers() 
        self.wfile.write(body)

def run():
    addr = ('', 8001)
    httpd = HTTPServer(addr, Handler)
    httpd.serve_forever()


if __name__ == "__main__":
	run()