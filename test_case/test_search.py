import json

from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testsearch:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    # 测试
    def test_search(self,protocolname, caseid, casetitle,meth,url,data,exc):
        self.gs.login()
        # 调用解密接口----不然查询结果含****
        ur="http://localhost:8080/WoniuBoss3.5/second"
        da={"vp":"woniu123"}
        self.gs.reques_meth("post",ur,da)
        # 调用查询接口----处理返回结果
        res,code = self.gs.reques_meth(meth, url, data)
        # print(exc)
        # print(res)
        if code==200 and res==exc:
            print("测试成功")
            self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
        else:
            print("测试失败")
            self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")





if __name__ == '__main__':
    s=Testsearch()
    '''
    {"qq":"0","work_id":"WNCD000","applposition":null,"next_tracking_time":null,"last_status":"新入库","employee_name":"测试账号","source":"智联招聘",
    "priority":"","tracking_times":0,"last_tracking_remark":null,"name":"刘润岑","last_tracking":null,"tel_source":null,
    "tel":"18281216976","customer_id":593307,"region":"成都","age":null}
    '''


