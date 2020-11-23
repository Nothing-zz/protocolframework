# 测试解密接口
from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testdecioher:
    def __init__(self):
        self.gs=Getsession()
        self.db = Operatdb()

    # 测试
    def test_decipher(self,protocolname,caseid,casetitle,meth,url,data,exc):
        self.gs.login()
        print(data)
        res,code=self.gs.reques_meth(meth,url,data)
        print(res,code)
        if code==200 and exc==res:
            print("测试成功")
            self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")




