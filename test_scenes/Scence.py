# 测试场景
import json
from woniuboss_protocol_framework.comm.rddata import Getdata
from woniuboss_protocol_framework.test_case.test_addsrc import Testaddsrc
from woniuboss_protocol_framework.test_case.test_cookie import Testcookie
from woniuboss_protocol_framework.test_case.test_decipher import Testdecioher
from woniuboss_protocol_framework.test_case.test_login import TestLogin
from woniuboss_protocol_framework.test_case.test_paymoney import Testpaymoney
from woniuboss_protocol_framework.test_case.test_safe import Testsafe
from woniuboss_protocol_framework.test_case.test_search import Testsearch
from woniuboss_protocol_framework.test_case.test_searchfin import Testsearchfin
from woniuboss_protocol_framework.test_case.test_tracksrc import Testtracksrc
from woniuboss_protocol_framework.test_case.test_upload import Testupload


class Testscesce:
    def __init__(self):
        self.rd=Getdata()
        self.path=self.rd.read_conf("../config/env.conf","data","excl")
    # 登录场景
    def login_scence(self):
        # 读取登录的用例
        li=self.rd.get_model_data(0,self.path)
        # print(li)
        # 调用测试登录
        for dic in li:
            lg=TestLogin()
            lg.test_login(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"],dic["参数"],dic["响应正文"])

    # 解密接口
    def decipher_scence(self):
        li=self.rd.get_model_data(1,self.path)
        # print(li)
        for dic in li:
            deciph=Testdecioher()
            deciph.test_decipher(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"],dic["参数"],dic["响应正文"])

    # 新增资源接口
    def addsrc_scence(self):
        li = self.rd.get_model_data(3,self.path)
        # print(li)
        for dic in li:
            addsrc = Testaddsrc()
            addsrc.test_addsrc(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"], dic["参数"], dic["响应正文"])

    # 查询资源接口
    def search_scence(self):
        li = self.rd.get_model_data(4,self.path)
        # print(li)
        for dic in li:
            search = Testsearch()
            search.test_search(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"], dic["参数"], dic["响应正文"])

    # 跟踪资源接口
    def track_scence(self):
        li = self.rd.get_model_data(5,self.path)
        for dic in li:
            # print(li)
            tk= Testtracksrc()
            tk.test_tracksrc(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"], dic["参数"], dic["响应正文"])

    # 缴费接口
    def paymoney_scence(self):
        li = self.rd.get_model_data(6,self.path)
        for dic in li:
            pm = Testpaymoney()
            pm.test_paymoney(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"], dic["参数"], dic["响应正文"])

    # 查询待缴费接口
    def searchfin_scence(self,):
        li = self.rd.get_model_data(7,self.path)
        for dic in li:
            sf = Testsearchfin()
            sf.test_searchfinance(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"],dic["接口地址"], dic["参数"], dic["响应正文"])

    # 上传简历接口
    def upload_scence(self):
        li = self.rd.get_model_data(2,self.path)
        for dic in li:
            upl= Testupload()
            # print(dic["请求方式"], dic["接口地址"], dic["参数"], dic["响应正文"])
            upl.test_upload(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"], dic["接口地址"], dic["参数"], dic["响应正文"])

    # cookie验证
    def verify_cookie(self):
        li=self.rd.get_model_data(-2,self.path)
        for dic in li:
            ck=Testcookie()
            ck.test_cookie(dic["接口名称"],dic["用例编号"],dic["标题"],dic["请求方式"], dic["接口地址"], dic["参数"], dic["响应正文"])

    # 越权验证
    def safe_scence(self):
        li = self.rd.get_model_data(-1,self.path)
        for dic in li:
            sf = Testsafe()
            sf.test_safe(dic["接口名称"], dic["用例编号"], dic["标题"], dic["请求方式"], dic["接口地址"], dic["参数"], dic["响应正文"])



if __name__ == '__main__':
    s=Testscesce()
    # s.login_scence()
    # s.decipher_scence()
    # s.addsrc_scence()
    # s.search_scence()
    # s.track_scence()
    # s.paymoney_scence()
    # s.searchfin_scence()
    s.upload_scence()
    # s.verify_cookie()
    # s.safe_scence()
<<<<<<< HEAD
    #俺在此
    
=======
    sada
>>>>>>> 9915d5e28f8cde8d223ba86779701f5bc92c80ad
