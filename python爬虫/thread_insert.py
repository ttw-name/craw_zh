


import connt_mysql
import settings
def gouzhao(q_get):
    while True:
        sql_cont = q_get.get()
        sql = settings.INSERT_START+sql_cont+settings.INSERT_END
        sql_ex = connt_mysql.Connt_mysqldb()
        sql_ex.execute_db(sql)
        sql_ex.commit_db()
        sql_ex.close()
        if q_get.qsize() == 0:
            break
