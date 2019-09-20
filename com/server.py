
from socket import *
import threading
import time
from query import DB


def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    db = DB()
    while True:
        recvData = sock.recv(1024)

def insertMetadata(data):
    db = DB()
    db.insert(data)

def searchMD5(data):
    db = DB()

def deleteMD5(data):
    db = DB()
    db.deleteHash(data)

def deleteOld(data):
    db = DB()
    db.deleteOld(data)

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass