from person import Person
import json
import logging

class PersonMachine:
    def proses(self,string_to_process,connection):
        p = Person()
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='put'):
                logging.warning("put")
                nama_file = cstring[1].strip()
                p.create_data(nama_file,connection)
                return json.dumps("File Sent")
            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (command=='get'):
                logging.warning("get")
                nama_file = cstring[1].strip()
                hasil = p.get_data(nama_file,connection)
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"