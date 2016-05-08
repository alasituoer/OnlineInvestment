# -*- coding: utf-8 -*-
import numpy as np
null = '' # 将null定义为全局变量
id_fund = [['000198', 62, '天虹余额宝货币'],
           ['000389', 51, '广发天天红货币A'],
           ['000330', 52, '汇添富现金货币'],
           ['000343', 49, '华夏财富宝货币'],
           ['000464', 47, '嘉实活期宝货币'],
           ['202301', 186, '南方现金增利货币A'],
           ['003003', 189, '华夏现金增利货币A'],
           ['482002', 150, '工银货币'],
           ['180008', 165, '银华货币A'],
           ['519505', 166, '海富通货币A'],
           ['020007', 161, '国泰货币'],
           ['020031', 50, '国泰现金管理货币A'],
           ['000009', 47, '易方达天天理财货币A'],
           ['000539', 46, '中银活期宝货币'],
           ['000371', 38, '民生加银现金宝货币'],
           ['519588', 152, '交银货币A'],
           ['000528', 34, '工银薪金货币A'], ]

class OlinvmPipeline(object):
    global null 
    def __init__(self):
        self.file1 = open(id_fund[6][2] + id_fund[6][0] + '.csv', 'wb')
        self.file1.write("日期 " + "七日年化收益率 " + "每日万份收益\n" )

    def process_item(self, item, spider):
        str1 = item['pre_text']
	x1 = '{"data"'
        x2 = '"total_num'
        str1 = str1[str1.index(x1)+8 : str1.index(x2)-1]
	#python eval() and ast.literal_eval()均不支持处理null, None表示空值
	str1.replace('null', '')

	if str1[0] == '{':
	    s1 = eval(str1)
	    # 新建一个二维数组将爬取结果按日期进行排序后再存入CSV文件
	    a = [[0 for col in range(3)] for row in range(len(s1))]
	    for i in range(len(s1)):
		a[i][0] = s1[s1.keys()[i]]['fbrq'][0:10]
		a[i][1] = s1[s1.keys()[i]]['nhsyl']
		a[i][2] = s1[s1.keys()[i]]['dwsy']
	    a.sort(reverse = True)
	    for i in range(len(s1)):
	        self.file1.write(a[i][0] + " ") 
	        self.file1.write(a[i][1] + " ") 
	        self.file1.write(a[i][2] + "\n") 
	if str1[0] == '[':
	    s2 = eval(str1)
            for i in range(len(s2)):
                self.file1.write(s2[i]['fbrq'][0:10] + " ")
		self.file1.write(s2[i]['nhsyl'] + " ")
		self.file1.write(s2[i]['dwsy'] + "\n")
	#得到的列表外层有引号
	#为了将字符串类型转换为列表类型,然后以键值对的形式调用所需信息
	#用eval()函数去掉该列表外层的引号

        return item

  
    def spider_closed(self, spider):
        self.file1.close()
