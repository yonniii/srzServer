
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
        db.insert(recvData.decode())
        db.deleteHash('14f18045f8648ba6c05c8c0c486d2f55')
        db.deleteOld('1567046609.8834774')
        print('상대방 :', recvData.decode('utf-8'),'을 DB에 insert')


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