from comm.get_session import Getsession
from comm.operatdb import Operatdb
from comm.rddata import Getdata


class Testupload:

    def __init__(self):
        self.gs = Getsession()
        self.da=Getdata()

    def test_upload(self,protocolname, caseid, casetitle,meth, url, data,exc):
        file=data["token"]
        data.pop("token")
        db = Operatdb()
        try:
            self.gs.login()
            if file!="":
                fil= {"batchfile": ("Asdf.xls", open(rf"{file}", mode="rb").read())}
                # print(data,fil)
                # 构建数据 与 数据库查询出来的作对比
            else:
                fil=""
            li = self.da.get_model_data(0, file)
            res, code = self.gs.reques_meth(meth, url, data, fil)
            print(res, code)
            li1=[]
            dic={}
            dic.update({"age":str(int(li[0]["年龄"])),"sex":li[0]["性别"],"email":li[0]["电子邮件"],"school":li[0]["学校名称"]})
            li1.append(dic)
            mail=li1[0]["email"]
            print(mail)
            # 数据库查询
            sql = f'SELECT age,sex,email,school FROM customer WHERE email="{mail}";'
            # 得到数据库查询结果
            dbli,num=db.read_db(sql)
            # print(code==200)
            # print(li1==dbli)
            # print(li1)
            # print(dbli)
            # print(exc==res)
            # 断言
            if code == 200 and exc == res and li1==dbli:
                print("测试成功")
                db.insert_res(protocolname, caseid, casetitle, "success", "无")
            else:
                print("测试失败")
                db.insert_res(protocolname, caseid, casetitle, "failed", "无")
        except Exception as e:
            print(e)
            db.insert_res(protocolname, caseid, casetitle, "error","出错了")


if __name__ == '__main__':
    s=Testupload()
    # s.test_upload()