import pymysql


import settings



class Connt_mysqldb():
    def __init__(self):
        try:
            self.con = pymysql.connect(host=settings.HOST,user=settings.USER,password=settings.PASSWORD,database=settings.DATABASWE)
            self.cousr = self.con.cursor()
        except:
            print('数据库连接出错')


    def execute_db(self,sql):
        try:
            self.cousr.execute(sql)
            return self.cousr
        except:
            return None
    def commit_db(self):
        self.con.commit()

    def close(self):
        self.cousr.close()
        self.con.close()


# con = Connt_mysqldb()
# con.execute_db('''create table if not exists test(id int primary key,name char(20) not null);''')
# e = con.execute_db('''insert into test set id=1,name="kui";''')
# cons = con.execute_db('''select * from test''')
# con.commit_db()
# con.close()
# print(cons.fetchall())
# print(e)

