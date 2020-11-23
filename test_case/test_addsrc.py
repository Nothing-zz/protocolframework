from woniuboss_protocol_framework.comm.get_session import Getsession
from woniuboss_protocol_framework.comm.operatdb import Operatdb


class Testaddsrc:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    def test_addsrc(self,protocolname, caseid, casetitle,meth,url,data,exc):
            self.gs.login()
            res, code = self.gs.reques_meth(meth, url, data)
            # 构建数据 与 数据库查询出来的作对比
            li1 = []
            dic = {}
            dic.update({"age": data["cus.age"], "sex": data["cus.sex"], "email": data["cus.email"], "school": data["cus.school"]})
            li1.append(dic)
            mail = data["cus.email"]
            sql = f'SELECT age,sex,email,school FROM customer WHERE email="{mail}";'
            # 得到数据库查询结果
            dbli,num= Operatdb().read_db(sql)
            # print(li1,dbli)
            # print(exc,res)
            if code == 200 and exc == res and li1==dbli:
                print("测试成功")
                self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
            else:
                print("测试失败")
                self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")