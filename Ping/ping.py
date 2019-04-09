#!/usr/bin/env python3

import sys
import argparse

import time
import socket
from socket import socket as Socket

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--server-port', '-p', default=2081, type=int,
                        help='Server_Port to use')
    
    parser.add_argument('--run-server', '-s', action='store_true',
                        help='Run a ping server')
    
    parser.add_argument('server_address', default='localhost',
                        help='Server to ping, no effect if running as a server.')
    
    args = parser.parse_args()


    if args.run_server:
        return run_server(args.server_port)
    else:
        return run_client(args.server_address, args.server_port,)

def run_server(server_port):
    with Socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', server_port))
        print("Ping server ready on port", server_port)
        while True:
            _, client_address = server_socket.recvfrom(1024)
            server_socket.sendto("Pong".encode(), client_address)

    return 0


def run_client(server_address, server_port):
	with Socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # raise NotImplementedError
		message = "Ping"
		i=10
		while i>0:
			client_socket.sendto(message.encode(), (server_address, server_port))
			returnedMessage, serverAdress = client_socket.recvfrom(1024)
			print(message)
			print(returnedMessage.decode())
			i=i-1	
		client_socket.close()
	


if __name__ == "__main__":
	sys.exit(main())