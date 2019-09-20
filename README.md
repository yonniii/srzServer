# srzServer
server-client 간의 metadata 이동 구현
## ver.0920
###1. 기능
####server
    1. insert metadatas
    2. search for MD5
    3. delete for MD5
    4. delete old data
    5. restore
####client
    1. srz manager
        send metadata - ctime,filename,path
    2. recovery manager
        request file recovery
        
###2. 환경
* lang : python 3.6
* webserver for test : ubuntu16.04, apache2
* DB : mysql

###3. 실행
####server
    $pip3 install pymysql
    $python3 server.py

####client
    $python3 client.py