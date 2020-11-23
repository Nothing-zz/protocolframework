# 获取session
import requests

from woniuboss_protocol_framework.comm.rddata import Getdata


class Getsession:
    def __init__(self):
        self.session=requests.session()
        self.rd = Getdata()

    # 请求方法
    def reques_meth(self,meth,url,data,file=None):
        res=self.session.request(method=meth,url=url,data=data,files=file)
        rest = res.text
        code=res.status_code
        # print(rest,code)
        return rest,code
    def login(self,user="WNCD056",pwd="woniu123"):
        url= self.rd.read_conf("../config/env.conf", "herf", "loginurl")
        data={'userName':f'{user}','userPass':f'{pwd}','checkcode':'0000'}
        res,code=self.reques_meth("post",url,data)
        print(res,code)



if __name__ == '__main__':
    s=Getsession()
    s.login()