# checkout/updata --从代码仓库中获取源码
# svn checkout 仓库路径 本地path --username 用户名 --password 密码  （进入想创建地方的路劲）
# svn updata 本地path
'''
1.获取源码
2.源码构建
3.部署环境
4.执行测试
5.发送邮件
'''
import os
import time

from woniuboss_protocol_framework.comm.rddata import Getdata
from woniuboss_protocol_framework.comm.send_email import SendEmail
from woniuboss_protocol_framework.test_suite.runner import Runner


class Citest:
    def __init__(self):
        self.rd=Getdata()
        self.get_url()

    # # 读取配置文件的路劲参数
    def get_url(self):
        self.rar=self.rd.read_conf(r"E:\wnb_framework_3.5\config\env.conf","mail","rar") # 压缩文件路劲
        self.rared = self.rd.read_conf(r"E:\wnb_framework_3.5\config\env.conf", "mail", "rared")  # 被压缩文件路劲
        self.tomcat = self.rd.read_conf(r"E:\wnb_framework_3.5\config\env.conf","mail", "tomcat")  # tomcat文件路劲

    # 获取源码：DOS命令
    def get_rsc(self):
        # 删除原有的文件
        # self.truncate_file()
        # time.sleep(1)
        if not os.path.exists("woniuboss"):
            cmd="svn checkout https://192.168.11.28/svn/woniuboss ../ci/woniuboss --username zhangrui "
            # os.system(cmd)
            rest=os.popen(cmd).read()
            if "Checked out revision" in rest:
                print("获取源码成功")
            else:
                print("获取源码失败")
        else:
            cmd="svn update ../ci/woniuboss"
            rest=os.popen(cmd).read()
            if "Updating" in rest:
                print("更新成功")
            else:
                print("更新失败")

    # 修改数据库配置文件
    def change_db(self):
        # 删除历史数据库文件
        dbpath=self.rd.read_conf("../config/env.conf","mail","dbconf")
        # print(dbpath)
        with open(f"{dbpath}","r")as f:
            cont=f.read()
            cont=cont.replace("password=root","password=123456")
            with open(f"{dbpath}","w")as w:
                w.write(cont)

    # # 源码构建
    # def build_rsc(self):
    #     # 使用ant文件 本机装在D盘  需要配置环境变量
    #     cmd="ant -f ../ci/woniusales001/build.xml"
    #     rest=os.popen(cmd).read()
    #     # print(rest)
    #     if "BUILD SUCCESSFUL" in rest:
    #         print("源码构建成功")
    #     else:
    #         print("源码构建失败")

    # 部署环境
    def deploy_rsc(self):
        # 删除历史war包 del /S /Q
        rest=os.popen(rf"del /S /Q {self.tomcat}\webapps\WoniuBoss3.5.war").read()
        # print(rest)
        if "删除文件" in rest:
            print("删除成功")
        else:
            print("删除失败")
        # 删除历史源码文件 rd/rmdir /S /Q
        os.popen(rf"rd /S /Q {self.tomcat}\webapps\WoniuBoss3.5")
        # 复制war包至服务器路径
        path=os.path.abspath("woniuboss/woniuboss3.5/WoniuBoss3.5.war")
        rest=os.popen(rf"copy {path} {self.tomcat}\webapps").read()
        # print(rest)
        if "已复制" in rest:
            print("复制成功")
        else:
            print("复制失败")
        time.sleep(1)
        # 打开服务,解析war包
        os.system("startup.bat") # 配置环境变量后 启动tomcat
        time.sleep(40)
        # 关闭服务
        os.system("taskkill /f /im java.exe")
        # 修改数据库配置文件
        self.change_db()
        # 开启服务
        os.system("startup.bat")


    # 执行测试
    def start_test(self):
        bg=Runner()
        bg.run()

    # 发送邮件
    def send_mail(self):
        sd=SendEmail()
        self.get_rar(self.rar,self.rared) # 准备压缩包
        with open(f"{self.rared}","r",encoding="utf-8") as f:
            cont=f.read()
            url=os.path.abspath(f"{self.rar}")
            sd.email(cont,url)

    # 压缩文件，以备附件上传
    def get_rar(self,rar,rared):
        os.system(f"rar a {self.rar} {self.rared}")

    # # 每次执行前删除之前的项目文件
    # def truncate_file(self):
    #     if os.path.exists(r"E:\cbtframework\ci\woniusales001"):
    #         os.popen(r"rd /S /Q E:\cbtframework\ci\woniusales001")
    #     if os.path.exists(r"E:\cbtframework\main\temp"):
    #         os.popen(r"rd /S /Q E:\cbtframework\main\temp")


if __name__ == '__main__':
    s=Citest()
    s.get_rsc()
    # s.build_rsc()
    s.deploy_rsc()
    s.start_test()
    s.send_mail()
    # s.truncate_file()

















