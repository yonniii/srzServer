import pymysql


class DB:

    def __init__(self):
        self.__db = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='1010duftl17',
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
