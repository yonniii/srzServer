from socket import *
import threading
import time
from getFile import getFiles

class SRZManager:
    def __init__(self,sock):
        self.__sock = sock

    def send(self):
        g = getFiles()
        list = g.exe()
        for i in list:
            self.__sock.send(i.encode('utf-8'))
            time.sleep(1)
        print('file info를 전송했습니다.')

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

port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

srzmanager = SRZManager(clientSock)
recovery = RecoveryManager(clientSock)
recovery.run()

while True:
    time.sleep(1)
    pass