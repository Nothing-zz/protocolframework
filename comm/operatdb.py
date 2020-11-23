# 数据库操作
import pymysql
from pymysql.cursors import DictCursor


class Operatdb:
    
    def __init__(self):
        pass

    # 连接数据库
    def conect_sql(self):
        con = pymysql.connect(host="localhost",port=3306,user="root",password="123456", db="woniuboss3.5")
        cur = con.cursor(cursor=DictCursor)
        return con, cur

    # 关闭连接关闭游标
    def close_sql(self, con, cur):
        con.commit()
        cur.close()
        con.close()

    # 读取数据库
    def read_db(self,sql):
        con,cur=self.conect_sql()
        # sql = f"select version,testmodule,testtype,caseid,casetitle,result,runtime,erromsg,screenshot from guidata;"
        num=cur.execute(sql)
        res = cur.fetchall()
        # 关闭数据库
        self.close_sql(con, cur)
        return res,num

    # 连接本地数据库
    def local_sql(self):
        con = pymysql.connect(host="localhost",port=3306,user="root",password="123456", db="report")
        cur = con.cursor(cursor=DictCursor)
        return con, cur

    # 向本地数据库插入测试结果
    def insert_res(self,protocolname,caseid,casetitle,rest,error):
        con,cur=self.local_sql()
        sql=f"insert into protocol value(DEFAULT,'{protocolname}','{caseid}','{casetitle}','{rest}',CURRENT_TIMESTAMP(),'{error}')"
        cur.execute(sql)
        cur.fetchall()
        # 关闭数据库
        self.close_sql(con,cur)

    # 读取测试结果
    def read_result(self):
        con,cur=self.local_sql()
        cur = con.cursor(cursor=DictCursor)
        sql = f"select protocolname,caseid,casetitle,result,runtime,erromsg from protocol;"
        num=cur.execute(sql)
        res = cur.fetchall()
        # 关闭数据库
        self.close_sql(con, cur)
        return res,num

    # 清除数据库表数据
    def trunc_data(self):
        con,cur=self.local_sql()
        cur.execute("TRUNCATE TABLE protocol;")
        self.close_sql(con,cur)

    # 读取测试完后成功失败的结果
    def get_num(self,res):
        con,cur=self.local_sql()
        sql=f"select * from protocol where result='{res}'"
        num=cur.execute(sql)
        cur.fetchall()
        self.close_sql(con,cur)
        return str(num)

if __name__ == '__main__':
    s=Operatdb()
    sql='SELECT age,sex,email,school FROM customer WHERE email="378473924@qq.com";'
    # res=s.read_db(sql)
    # print(res)
    # print(s.read_result())
    print(s.read_result())














