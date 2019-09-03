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

def send(sock):
    while True:
        g = getFiles()
        list = g.exe()
        for i in list:
            clientSock.send(i.encode('utf-8'))
        time.sleep(100)


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

# sender.start()
srzmanager = SRZManager(clientSock)
srzmanager.send()
receiver.start()

while True:
    time.sleep(1)
    pass