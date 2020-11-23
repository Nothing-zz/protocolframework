# 数据处理
from configparser import ConfigParser

import xlrd


class Getdata:
    def __init__(self):
        pass

    # 获取Excel每个模块的参数
    def get_model_data(self,num,path="../test_data/接口测试文档1.xlsx"):
        book=xlrd.open_workbook(f"{path}")
        sheet=book.sheets()[num]
        li=[]
        # 键值
        key_li=sheet.row_values(0)
        # print(key_li)
        for i in range(1,sheet.nrows):
            dic = {}
            li1=sheet.row_values(i)
            # print(li1)
            li2=li1[6].split("\n")
            dic1={}
            # 把传入参数生成字典
            for q in li2:
                li3=q.split("=")
                dic1[li3[0]]=li3[-1]
                li1[6]=dic1
            # print(li1)
            for j in range(len(li1)):
                dic[key_li[j]]=li1[j]
            li.append(dic)
        return li

    # 读取测试配置环境配置信息
    def read_conf(self, file, section, option):
        conf = ConfigParser()  # 实例化
        conf.read(file)
        value = conf.get(section=section, option=option)
        return value

    # 读取配置文件方法二
    def read_all_option(self, file, section):
        conf = ConfigParser()
        conf.read(file)
        value = conf.items(section=section)
        return dict(value)





if __name__ == '__main__':
    S=Getdata()
    print(S.read_conf("../config/env.conf","db","host"))
    print(S.read_all_option("../config/env.conf", "db"))



