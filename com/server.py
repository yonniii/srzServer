
from socket import *
import threading
import time
from query import DB


def exeReq(typeData,reqData):
    reqType = typeData
    if reqType is 48:
        insertMetadata(reqData)
    elif reqType is 49:
        restoreMetadata()

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        exeReq(recvData[0],recvData[1:].decode())

def insertMetadata(data):
    db = DB()
    db.insert(data)

def searchMD5(data):
    db = DB()
    db.serchMD5(data)

def deleteMD5(data):
    db = DB()
    db.deleteHash(data)

def deleteOld(data):
    db = DB()
    db.deleteOld(data)

def restoreMetadata():
    db = DB()
    datas = db.restore()
    print(datas)

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

receiver = threading.Thread(target=receive, args=(connectionSock,))

receiver.start()

while True:
    time.sleep(1)
    pass