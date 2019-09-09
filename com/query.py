import pymysql


class DB:

    def __init__(self):
        self.__db = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='1234',
                                    db='srzserver',
                                    charset='utf8')
        self.__cursor = self.__db.cursor()

    def __executeQuery(self, sql):
        self.__cursor.execute(sql)
        self.__db.commit()

    def insert(self, data):
        sql = """INSERT INTO `metadatas`(`ctime`, `filename`, `path`, `hash`) VALUES (%s,'%s','%s','%s')"""
        values = data.split(',')
        sql = sql % (values[0], values[1], values[2], values[3])
        print(sql)
        self.__executeQuery(sql)

    def deleteHash(self, hash):
        sql = """DELETE FROM metadatas WHERE hash = '%s'""" % (hash)
        print(sql)
        self.__executeQuery(sql)

    def deleteOld(self, time):
        sql = """DELETE FROM metadatas where ctime <= %s""" % (time)
        print(sql)
        self.__executeQuery(sql)

    def restore(self):
        sql = """SELECT * FROM metadatas"""
        self.__executeQuery(sql)
        return self.__cursor.fetchall()