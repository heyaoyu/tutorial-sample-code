# -*- coding: utf-8 -*-

import socket
import urllib

class HttpSocketClient(object):

    protocol = "HTTP/1.1"
    bufsize = 1024

    def __init__(self, host, port):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def request(self, method='get', uri='/', headers='', body=''):
        self.soc.connect((self.host, self.port))
        req = self.constructHttpRequest(method, uri, headers, body)
        self.soc.send(req)
        return self.getResponse()

    def constructHttpRequest(self, method, uri, headers, body):
        req_line = ' '.join([method.upper(), uri, HttpSocketClient.protocol])
        header = '\r\n'.join(["%s: %s" % (k, headers[k]) for k in headers])
        req = '\r\n'.join([req_line, header, urllib.urlencode(body)])
        req += '\r\n'
        return req

    def getResponse(self):
        buf = ''
        tmp_buf = self.soc.recv(HttpSocketClient.bufsize)
        buf += tmp_buf
        while len(tmp_buf):
            buf += tmp_buf
            tmp_buf = self.soc.recv(HttpSocketClient.bufsize)
        self.soc.close()
        return buf

class SimpleEchoClient():

    bufsize = 1024

    def __init__(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.soc.connect((host, port))

    def echo(self, msg):
        print "Sending... "+msg
        r = self.soc.send(msg+"EOF")
        print str(r) + " bytes sent."
        response = self.getResponse()
        print response
        self.soc.close()

    def getResponse(self):
        buf = ''
        tmp_buf = self.soc.recv(HttpSocketClient.bufsize)
        buf += tmp_buf
        while tmp_buf[-3:]!="EOF":
            buf += tmp_buf
            tmp_buf = self.soc.recv(HttpSocketClient.bufsize)
        buf = buf[:-3] # strip EOF
        self.soc.close()
        return buf


def main():
    client = HttpSocketClient("www.baidu.com", 80)
    response = client.request(headers={"Host": "www.baidu.com", "Connection":"Close"})
    print response

    echo_client = SimpleEchoClient()
    echo_client.connect('localhost', 8080)
    echo_client.echo('Hello World')

if __name__ == '__main__':
    main()