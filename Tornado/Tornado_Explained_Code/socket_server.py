# -*- coding utf-8 -*-

import socket

class SimpleEchoServer(object):

    bufsize = 1024

    def __init__(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self, host='', port=8080):
        try:
            self.soc.bind((host, port))
            self.soc.listen(5)
        except Exception, e:
            print e
        else:
            print 'listening on ' + str((host, port))


    def start(self):
        while True:
            conn, address = self.soc.accept()
            print 'Connection is constructed: '+str(address)
            buf = ''
            tmp = conn.recv(SimpleEchoServer.bufsize)
            buf += tmp
            while tmp[-3:] != "EOF":
                buf += tmp
                tmp = conn.recv(SimpleEchoServer.bufsize)
            buf = buf[:-3] # strip EOF
            print 'Received: '+buf
            print 'Sending back: '+buf
            conn.send(buf+"EOF")
            conn.close()

    def close(self):
        self.soc.close()

def main():
    try:
        server = SimpleEchoServer()
        server.listen()
        server.start()
    finally:
        server.close()

if __name__ == '__main__':
    main()