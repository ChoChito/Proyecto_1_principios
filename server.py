# -*- coding: utf-8 -*-
#afkahbfk
#hoasdknasdasjnd
"""
Created on Sat May  4 18:32:49 2019
@author: Max
"""

import socket
import threading
import sys
import pickle

class client():

  def __init__(self, conn, balance, username):
      self.username=username
      self.balance=balance
      self.conn=conn

  def getBalance(self):
      return(self.balance)
  
  def getUsername(self):
      return(self.username)
      
  def getClient(self):
      return(self.conn)


class Servidor():
    """docstring for Servidor"""
    def __init__(self, host="localhost", port=4000):
        
        self.clientes = []
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)
        
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        
        aceptar.daemon = True
        aceptar.start()
        
        procesar.daemon = True
        procesar.start()
        while True:
            msg = input('me:')
            if msg == 'salir':
                self.sock.close()
                sys.exit()
            elif msg == ':u':
                print(self.clientes)
            else:
                pass
            
    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)
                
    def aceptarCon(self):
        print("AceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                usuario='[Server] Cliente: Usuario'+str(addr[1])
                print(usuario+' se ha conectado!')
                self.clientes.append(conn)
            except:
                pass
            
    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            msg=pickle.loads(data)
                            print(msg)
                            if msg==':q':
                                usuario='usuario'
                                print(usuario+' se ha desconectado!')
                                self.msg_to_all(usuario+' se ha desconectado!',c)
                            else:       
                                self.msg_to_all(data,c)
                    except:
                        pass
  
                  
s = Servidor()
