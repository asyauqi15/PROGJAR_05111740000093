import sys
import socket

host = 'localhost'
port = 31000
filename = 'tugas1/tugas1b/contoh.txt'
flag = 0

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (host, port)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    sock.sendall(filename.encode())
    data = sock.recv(1024)
    size = int.from_bytes(data, byteorder='big')
    current_size = 0

    with open(filename[:-4]+"_test"+filename[-4:], 'wb') as request_file:
        while current_size<size:
            data = sock.recv(1024)
            if not data:
                break
            if len(data)+current_size>size:
                data = data[:size-current_size]
                data_dump = data[(size-current_size):current_size]
                flag = 1
            request_file.write(data)
            current_size = current_size+len(data)
    request_file.close()

    if flag == 0:
        abc = sock.recv(1024)
        print(abc.decode)
        flag = 0
        
finally:
    print("closing")
    sock.close()
