#!/usr/bin/env python3

import argparse

import sys
import itertools
import socket
from socket import socket as Socket



def main():

    # Command line arguments. Use a port > 1024 by default so that we can run
    # without sudo, for use as a real server you need to use port 80.
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    # Create the server socket (to handle tcp requests using ipv4), make sure
    # it is always closed by using with statement.
    with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(('', args.port))
        server_socket.listen(1)

        print("server ready")

        while True:

            with server_socket.accept()[0] as connection_socket:
                request = connection_socket.recv(1024).decode('ascii')
                reply = http_handle(request)
                connection_socket.send(reply.encode('ascii'))


            print("\n\nReceived request")
            print("======================")
            print(request.rstrip())
            print("======================")


            print("\n\nReplied with")
            print("======================")
            print(reply.rstrip())
            print("======================")


    return 0


def http_handle(request_string):
    assert not isinstance(request_string, bytes)
	

    pass



if __name__ == "__main__":
sys.exit(main())