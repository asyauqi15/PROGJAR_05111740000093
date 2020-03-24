import shelve
import uuid
from datetime import datetime
import os


class Person:
    def __init__(self):
        self.data = shelve.open('mydata.dat')
    def create_data(self,nama=None,connection=None):
        if (nama is None or connection is None):
            return False
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M:%S")

        get_size = connection.recv(4)
        file_size = int.from_bytes(get_size,byteorder='big')

        with open(nama, 'wb+') as file_recv:
            recv_size = 0
            while recv_size < file_size:
                byte_n = connection.recv(32)
                recv_size += len(byte_n)
                if not byte_n:
                    break
                file_recv.write(byte_n)
        file_recv.close()

        duplicate = False
        for i in self.data.keys():
            try:    
                if(self.data[i]['nama_file'].lower()==nama.lower()):
                    temp = self.data[i]
                    temp['last_update'] = current_time
                    self.data[i] = temp
                    duplicate = True
            except:
                duplicate = False
        if not duplicate:
            id=str(uuid.uuid4())
            data = dict(id=id,nama_file=nama,last_update=current_time)
            self.data[id]=data
        return True
    def get_data(self,nama=None,connection=None):
        if (nama is None or connection is None):
            return False

        for i in self.data.keys():
            if (self.data[i]['nama_file'].lower()==nama.lower()):
                size = os.path.getsize(nama)
                val = size.to_bytes(4,byteorder='big')
                connection.send(val)
                with open(nama, 'rb') as file_to_send:
                    for byte in file_to_send:
                        connection.sendall(byte)
                file_to_send.close()
                return "File Downloaded"

        size = 0
        val = size.to_bytes(4,byteorder='big')
        connection.send(val)
        return "No Such File"
    
    def list_data(self):
        k = [{'nama_file':self.data[i]['nama_file'],'last_update':self.data[i]['last_update']} for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = Person()
    p.create_data("vanBasten")
    p.create_data("vanPersie")
    p.create_data("vanNistelroy")
    p.create_data("vanDerVaart")
    print(p.list_data())
    print(p.get_data('vanbasten'))