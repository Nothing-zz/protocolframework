from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testtracksrc:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    # 测试
    def test_tracksrc(self,protocolname, caseid, casetitle,meth,url,data,exc):
        try:
            self.gs.login()
            # print(url)
            # 调用资源跟踪接口
            res, code = self.gs.reques_meth(meth, url, data)
            # print(res, code)
            # 数据库断言
            ids=data["id"]
            sql="SELECT " \
                "cus.last_status 'status'," \
                "stu.need_fee fee," \
                "cus.last_tracking_remark remark," \
                "cus.customer_id id," \
                "cus.next_tracking_time nextTime," \
                "cus.priority priority " \
                "FROM " \
                "customer cus,student stu " \
                "WHERE " \
                "stu.student_customer_id = cus.customer_id " \
                f"AND cus.customer_id = '{ids}' ;"
            li,num=self.db.read_db(sql)
            print(li)
            # 3个条件断言
            if code == 200 and exc == res and li[0]==data:
                print("测试成功")
                self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
            else:
                print("测试失败")
                self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")
        except Exception as e:
            self.db.insert_res(protocolname, caseid, casetitle, "error", e)