import os
import sys
import socket


class Server:
    def __init__(self, socket_path):
        self.socket_path = socket_path

    def start(self):
        s = self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(self.socket_path)
        s.listen(1)
        try:
            while True:
                connection, address = s.accept()
                sys.stdout.write("connected\n")
                self.accepted(connection, address)
                sys.stdout.write("disconnect\n")
        finally:
            os.remove(self.socket_path)

    def accepted(self, connection, address):
        """echo the received data
        """
        data = connection.recv(1024)
        sys.stdout.write("receive from client: {}\n".format(data.decode()))
        connection.send(data)
        sys.stdout.write("send to client: {}\n".format(data.decode()))


def main():
    server = Server('/tmp/test.sock')
    server.start()

if __name__ == '__main__':
    main()
