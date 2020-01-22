
from socket import *
import threading
import time
from query import DB


class srzServer:

    def exeReq(self,typeData=None,reqData=None):
        reqType = typeData
        if reqType is 48:
            self.insertMetadata(reqData)
        elif reqType is 49:
            self.restoreMetadata()
        elif reqType is 50:
            self.searchMD5(reqData)
        elif reqType is 51:
            self.deleteMD5(reqData)
        elif reqType is 52:
            self.deleteOld(reqData)
        else:
            return false

    def receive(self,sock):
        while True:
            recvData = sock.recv(1024)
            self.exeReq(typeData = recvData[0], reqData = recvData[1:].decode())

    def insertMetadata(self,data):
        db = DB()
        db.insert(data)

    def searchMD5(self,data):
        db = DB()
        db.serchMD5(data)

    def deleteMD5(self,data):
        db = DB()
        db.deleteHash(data)

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

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d waiting...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), ' connetced')

s = srzServer()
s.run()

while True:
    time.sleep(1)
    pass