from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testsearchfin:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    def test_searchfinance(self,protocolname, caseid, casetitle,meth,url,data,exc):
        # 登录
        self.gs.login()
        # 调用解密接口----不然查询结果含****
        ur = "http://localhost:8080/WoniuBoss3.5/second"
        da = {"vp": "woniu123"}
        self.gs.reques_meth("post", ur, da)
        res, code = self.gs.reques_meth(meth, url, data)
        # print(res)
        # 查询数据库
        if code == 200 and exc == res:
            print("测试成功")
            self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")
