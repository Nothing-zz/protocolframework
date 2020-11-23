# 测试无权限人员越权操作
from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testsafe:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    def test_safe(self,protocolname, caseid, casetitle,meth,url,data,exc):
        self.gs.login("wncd123","woniu123")
        res,code=self.gs.reques_meth(meth,url,data)
        # print(res)
        if code==200 and exc in res:
            print("测试成功")
            self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")





