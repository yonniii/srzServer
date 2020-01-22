import pymysql
from md5hash import md5hash


class DB:

    def __init__(self):
        self.__db = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='',
                                    db='srz_db',
                                    charset='utf8')
        self.__cursor = self.__db.cursor()

    def __executeQuery(self, sql):
        self.__cursor.execute(sql)
        self.__db.commit()

    def insert(self, data):
        hash = md5hash()
        sql = """INSERT INTO `metadata`(`ctime`, `filename`, `path`, `hash`) VALUES (%s,'%s','%s','%s') ON DUPLICATE KEY UPDATE hash='%s'"""
        values = data.split(',')
        md5 = hash.getHash('%s,%s' % (values[2], values[0]))
        sql = sql % (values[0], values[1], values[2], md5, md5)
        print(sql)
        self.__executeQuery(sql)

    def serchMD5(self,md5):
        sql= """SELECT * FROM srz_db.metadata WHERE hash='%s'"""
        sql = sql%(md5)
        self.__executeQuery(sql)
        return self.__cursor.fetchall()

    def deleteHash(self, hash):
        sql = """DELETE FROM metadata WHERE hash = '%s'""" % (hash)
        print(sql)
        self.__executeQuery(sql)

    def deleteOld(self, time):
        sql = """DELETE FROM metadata where ctime <= %s""" % (time)
        print(sql)
        self.__executeQuery(sql)

    def restore(self):
        sql = """SELECT * FROM metadata order by ctime DESC """ # 최근에 생성된 순으로 정렬
        self.__executeQuery(sql)
        return self.__cursor.fetchall()