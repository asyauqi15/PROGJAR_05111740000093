import sys
import socket
import os
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host = '127.0.0.1'#input('host: ')
port = 8889#int(input('port: '))
server_address = (host, port)
print(f"connecting to {server_address}")
sock.connect(server_address)
while True:
    string = input()
    cstring = string.split(" ")
    try:
        command = cstring[0].strip()
        if command=='put':
            nama_file = cstring[1].strip()
            if os.path.exists(nama_file):
                sock.sendall(string.encode())

                size = os.path.getsize(nama_file)
                print(size)
                val = size.to_bytes(4,byteorder='big')
                sock.send(val)

                print(f"uploading {nama_file}")
                with open(nama_file, 'rb') as file_to_send:
                    for byte in file_to_send:
                        sock.sendall(byte)
                file_to_send.close()
                response = sock.recv(1024)
                responses = response.decode()
                string_response = json.loads(responses[:-2])
                print(string_response)      
            else:
                print('file not found')
        elif command=='list':
            sock.sendall(string.encode())
            response = sock.recv(1024)
            responses = response.decode()
            list_response = json.loads(responses[:-2])
            for objects in list_response:
                i,j = objects.values()
                print(f'{i}\t-updated {j}')
        elif command=='get':
            sock.sendall(string.encode())
            get_size = sock.recv(4)
            file_size = int.from_bytes(get_size,byteorder='big')
            if file_size :
                nama_file = cstring[1].strip()
                with open(nama_file, 'wb+') as file_recv:
                    recv_size = 0
                    while recv_size < file_size:
                        byte_n = sock.recv(2)
                        recv_size += len(byte_n)
                        if not byte_n:
                            break
                        file_recv.write(byte_n)
                file_recv.close()
            response = sock.recv(1024)
            responses = response.decode()
            string_response = json.loads(responses[:-2])
            print(string_response)   
        else:
            print("ERRCMD")
    except:
        print("ERROR")