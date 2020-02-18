import sys
import socket

host = 'localhost'
port = 31000
filename = 'tugas1/tugas1a/contoh.txt'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (host, port)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    # Send data
    sock.sendall(filename.encode())
    file_send = open(filename, 'rb')
    print("sending "+filename)
    sending = file_send.read(1024)

    while sending:
        sock.send(sending)
        sending = file_send.read(1024)
    
    print("complete")

finally:
    print("closing")
    sock.close()
