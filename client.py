import socket
import threading
import sys
import pickle

class Cliente():
    """docstring for Cliente"""
    def __init__(self, host="localhost", port=4000):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        
        msg_recv = threading.Thread(target=self.msg_recv)
        
        msg_recv.daemon = True
        msg_recv.start()
        print ('Bienvenido al mejor chat del universo!')
        print( )
        while True:
            msg = input('->')
            if msg != ':q':
                self.send_msg(msg)
            else:
                self.send_msg(msg)
                self.sock.close()
                print('Te has desconectado del mejor chat del universo!')
                sys.exit()
                
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
            
    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))
        
        
c = Cliente()
