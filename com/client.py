from socket import *
import threading
import time
from getFile import getFiles

class SRZManager:
    def __init__(self,sock):
        self.__sock = sock

    def sendMeta(self):
        g = getFiles()
        list = g.exe()
        for i in list:
            data='0'+i
            self.__sock.send(data.encode('utf-8'))
            time.sleep(1)
        print('Send file info')

    def reqMeta(self):
        reqM = '1'
        self.__sock.send(reqM.encode('utf-8'))

    def inputCmd(self):
        print('SADFASDFSA')
        while True:
            sendData = input('0:sendMeta / 1:reqMeta / 2+md5 :search / 3+md5:delete / 4+time : delete before\n')
            if sendData is '0':
                self.sendMeta()
            elif sendData is '1':
                self.reqMeta()
            else:
                self.__sock.send(sendData.encode('utf-8'))

    def run(self):
        sender = threading.Thread(target=self.inputCmd)
        sender.start()
        sender.join()

class RecoveryManager:
    def __init__(self,sock):
        self.__sock = sock

    def send(self):
        self.__sock.send('request'.encode())

    def receive(self):
        print('receive')
        f=open('metadata.txt',mode='wt', encoding='utf-8')
        while True:
            recvData = self.__sock.recv(1024)
            print(recvData.decode())
            if recvData.decode() is '0':
                f.close()
            self.writeMeta(recvData.decode(),f)

    def writeMeta(self,recvData,f):
        f.write(recvData+'\n')

    def run(self):
        sender = threading.Thread(target=self.send )
        receiver = threading.Thread(target= self.receive)
        sender.start()
        receiver.start()
        sender.join()
        receiver.join()

# def send(sock):
#     while True:
#         sendData = input('>>>')
#         sock.send(sendData.encode('utf-8'))

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('connect')

# sender = threading.Thread(target=send, args=(clientSock,))
# sender.start()
srzmanager = SRZManager(clientSock)
srzmanager.run()
recovery = RecoveryManager(clientSock)
recovery.run()

while True:
    time.sleep(1)
    pass