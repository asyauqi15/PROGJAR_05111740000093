import sys
import socket

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

data = connection.recv(1024).decode()
print(f"received {data}")

filename = open(data[:-4]+"_test"+data[-4:], 'wb')
data_content = connection.recv(1024)

while data_content:
    filename.write(data_content)
    data_content = connection.recv(1024)
    
filename.close()

print("file received")

# Clean up the connection
connection.close()
