import time
from comm.genrate_report import Get_report
from comm.operatdb import Operatdb
from comm.rddata import Getdata
from test_scenes.Scence import Testscesce


class Runner:
    def __init__(self):
        self.start=Testscesce()
        self.db=Operatdb()
        self.report=Get_report()
        self.rd=Getdata()

    # 开始测试
    def run(self):
        # 清空数据库
        self.db.trunc_data()
        # 执行测试
        print("登录接口".center(50, "*"))
        self.start.login_scence()
        time.sleep(3)
        print("解密接口".center(50,"*"))
        self.start.decipher_scence()
        print("上传简历接口".center(50, "*"))
        self.start.upload_scence()
        print("新增资源接口".center(50, "*"))
        self.start.addsrc_scence()
        print("查询资源接口".center(50, "*"))
        self.start.search_scence()
        print("跟踪资源接口".center(50, "*"))
        self.start.track_scence()
        print("缴费接口".center(50, "*"))
        self.start.paymoney_scence()
        print("待缴费接口".center(50, "*"))
        self.start.searchfin_scence()
        print("验证cookie".center(50, "*"))
        self.start.verify_cookie()
        print("权限验证".center(50, "*"))
        self.start.safe_scence()
        # 生成报告
        self.makereport()

    # 生成测试结果
    def makereport(self):
        success=self.db.get_num("success")
        faile=self.db.get_num("failed")
        error=self.db.get_num("erron")
        project=self.rd.read_conf("../config/env.conf","head","model")
        modpath=self.rd.read_conf("../config/env.conf", "head", "modelpath")
        report=self.rd.read_conf("../config/env.conf", "head", "reportpath")
        print(project)
        self.report.make_report(project,success,faile,error,modpath,report)







if __name__ == '__main__':
    s=Runner()
    # s.run()
    s.makereport()
    # Operatdb().trunc_data()
