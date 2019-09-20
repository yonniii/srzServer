
from socket import *
import threading
import time
from query import DB


class srzServer:

    def exeReq(self,typeData,reqData):
        reqType = typeData
        if reqType is 48:
            self.insertMetadata(reqData)
        elif reqType is 49:
            self.restoreMetadata()

    def receive(self,sock):
        while True:
            recvData = sock.recv(1024)
            self.exeReq(recvData[0],recvData[1:].decode())

    def insertMetadata(self,data):
        db = DB()
        db.insert(data)

    def searchMD5(self,data):
        db = DB()
        db.serchMD5(data)

    def deleteMD5(self,data):
        db = DB()
        db.deleteHash(self,data)

    def deleteOld(self,data):
        db = DB()
        db.deleteOld(data)

    def restoreMetadata(self):
        db = DB()
        datas = db.restore()
        print(datas)

    def run(self):
        receiver = threading.Thread(target=self.receive, args=(connectionSock,))

        receiver.start()

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

s = srzServer()
s.run()

while True:
    time.sleep(1)
    pass