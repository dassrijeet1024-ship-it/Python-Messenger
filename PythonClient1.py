import socket
import threading

HEADER_LENGTH = 15
PORT = 1250
HOST = 'localhost'

g = socket.socket()
g.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Eliminates "Address already in use" Error

g.connect(('localhost', 1250))

g.setblocking(True) # Eliminates LockingIOError

message = input("Client -> ")

while True:
    g.sendall(message.encode()) # Sends message to client after converting the same to bytes
    text = g.recv(1024) # Receives data from server, 1024 bytes at a time

    data = text.decode() # Decodes byte data from server

    print('Server -> ' + data)  # Prints message from server

    message = input("Client -> ")  # Taking input to send to server

g.close()