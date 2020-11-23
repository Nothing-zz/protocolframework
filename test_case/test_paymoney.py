from comm.get_session import Getsession
from comm.operatdb import Operatdb


class Testpaymoney:
    def __init__(self):
        self.gs = Getsession()
        self.db = Operatdb()

    def test_paymoney(self,protocolname, caseid, casetitle,meth,url,data,exc):
        try:
            self.gs.login()
            # print(url)
            # 调用缴费接口
            detail_record=data["student_name"]
            res, code = self.gs.reques_meth(meth, url, data)
            # 数据库查询
            sql = f'SELECT * FROM finance_detail WHERE expend_name="{detail_record}";'
            li,num=self.db.read_db(sql)
            # print(res,exc)
            # print(num)
            if code == 200 and exc == res and num==1:
                print("测试成功")
                self.db.insert_res(protocolname, caseid, casetitle, "success", "无")
            else:
                print("测试失败")
                self.db.insert_res(protocolname, caseid, casetitle, "failed", "无")
        except Exception as e:
            self.db.insert_res(protocolname, caseid, casetitle, "error",e)



if __name__ == '__main__':
    s=Testpaymoney()
    data={'student_id': '1382', 'student_name': '刘润岑', 'student_no': 'WNCD201806034', 'student_class': 'WNCD035', 'student_newstatus': '已缴清', 'finance.borrow': '16800', 'all.money': '16800元', 'deal.dealings_subject2': '支付宝', 'deal.changeInaccount': '基本户(成都)', 'addMoretxt': '111'}
    url="http://192.168.11.8:8080/WoniuBoss2.5/finance/saveStudentPay"
    s.test_paymoney(1,1,1,"post",url,data,1)