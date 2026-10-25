import socket
import threading

HOST = 'localhost'
PORT = 1250
HEADER_LENGTH = 15

s = socket.socket() # Creating the socket object and specifying the TCP/IP Protocol
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Eliminates "Address already in use" Error
s.bind((HOST, PORT)) # Assigning specified IP Address and port number to the socket object
s.listen() # Listens to client connection

conn, addr = s.accept() # Returns a tuple containing a connection object and the 

print(f"Connections made on {HOST} on port {PORT}")

print(f"Connected to ", str(addr)) # Prints IP Address and port number to which client has connected

while True:
   
    text = conn.recv(1024)

    data = text.decode() # Converting byte data from client 
    print("Client -> ", str(data)) # Printing text from client after converting the same to string

    data = input('Server -> ')
    conn.sendall(data.encode())  # send data to the client

# Closes the connection
conn.close()
s.close()
