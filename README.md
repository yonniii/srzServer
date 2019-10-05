# srzServer
server-client 간의 metadata 이동 구현
## ver.0920
### 1. 기능
#### server
    1. client가 전송한 파일정보(파일이름,생성시간,파일경로)로 MD5생성하여 DB에 저장하는 기능
    2. DB에서 MD5로 검색하는 기능
    3. DB에서 MD5로 삭제하는 기능
    4. 시간정보가 주어졌을 때 이전의 데이터 모두 지우는 기능
    5. 데이터를 모두 client로 전송하는 기능
#### client
    1. srz manager
        metadata 전송 - ctime,filename,path
    2. recovery manager
        request file recovery
        
### 2. 환경
* lang : python 3.6
* webserver for test : ubuntu16.04, apache2
* DB : mysql

### 3. 실행
#### server
    $pip3 install pymysql
    $python3 server.py

#### client
    $python3 client.py
