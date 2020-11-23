from comm.get_session import Getsession
from comm.operatdb import Operatdb


class TestLogin:
    def __init__(self):
        self.gs=Getsession()
        self.db=Operatdb()

    def test_login(self,protocolname,caseid,casetitle,meth,url,data,exc):
        res,code=self.gs.reques_meth(meth,url,data)
        print(res,code)
        if code==200 and exc in res:
            print("测试通过")
            self.db.insert_res(protocolname,caseid,casetitle,"success","无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")


if __name__ == '__main__':
    s=TestLogin()
    s.test_login()