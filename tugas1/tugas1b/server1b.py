import sys
import socket
import os

host = 'localhost'
port = 31000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = (host, port)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print("waiting for a connection")
connection, client_address = sock.accept()
print(f"connection from {client_address}")
request_file = connection.recv(1024).decode()

if os.path.isfile(request_file):
    size = os.path.getsize(request_file)
    connection.send(size.to_bytes(4,byteorder='big'))
    with open(request_file, 'rb') as sending_file:
        for data in sending_file:
            connection.sendall(data)
    sending_file.close()

    message = "complete"
    print(message)
    # connection.sendall(message.encode())
else:
    message = "file not found"
    print(message)
    # connection.sendall(message.encode())

# Clean up the connection
connection.close()
