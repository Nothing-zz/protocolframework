# 处理数据
import time
from comm.operatdb import Operatdb


class Get_report:
    def __init__(self):
        self.db=Operatdb()
    # 报告数据收集：$product $passed $failed $error $runtime $tr
    def make_report(self,product,passed,failed,error,modlepath,reportpath):
        # 读取html模板，进行替换
        with open(modlepath, "r", encoding="utf-8") as f:
            cont = f.read()
            cont = cont.replace("$product", product)
            cont = cont.replace("$passed", passed)
            cont = cont.replace("$failed", failed)
            cont = cont.replace("$error", error)
            cont = cont.replace("$runtime", time.strftime("%Y-%m-%d %H:%M:%S"))
            # 获取测试完成后构造好的结果
            res=self.make_table()
            print(res)
            # 替换结果
            cont = cont.replace("$table-tr",res)
            with open(reportpath, "w", encoding="utf-8") as w:
                print(reportpath)
                w.write(cont)
        print(1)
    # 构造测试结果表格内数据
    def make_table(self):
        # 读取数据库数据
        li,num=self.db.read_result()
        print(li)
        rest=""
        for i in li:
            # print(i)
            rest += '<tr height="40">\n'
            rest += f'<td width="7%">{i["protocolname"]}</td>\n'
            rest += f'<td width="9%">{i["caseid"]}</td>\n'
            rest += f'<td width="10%">{i["casetitle"]}</td>\n'
            if i["result"]=="failed" or i["result"]=="error":
                rest += f'<td width="7%" bgcolor="red">{i["result"]}</td>\n'
            else:
                rest += f'<td width="7%" bgcolor="#00FFFF">{i["result"]}</td>\n'
            rest += f'<td width="15%">{i["runtime"]}</td>\n'
            rest += f'<td width="15%">{i["erromsg"]}</td>\n'
            rest+='</tr>'
        return rest



if __name__ == '__main__':
    s=Get_report()

    # s.insert_db('1.5','add','ui','test005','测试5',"success","无","无")
    # s.read_db()
    s.make_table()
    # s.make_report("WoniuBoss2.5",'5','3','2',"../testreport/template.html","../testreport/report.html")