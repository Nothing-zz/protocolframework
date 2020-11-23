# 验证未登录直接调用接口
from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testcookie:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    # 调用接口
    def test_cookie(self,protocolname, caseid, casetitle,meth,url,data,exc):
        res,code=self.gs.reques_meth(meth,url,data)
        # print(res)
        if code==200 and exc in res:
            print("测试成功")
            self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")




