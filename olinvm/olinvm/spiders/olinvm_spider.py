# -*- coding:utf-8 -*-
import scrapy
from olinvm.items import OlinvmItem

class olinvmSpider(scrapy.Spider):
    name = "olinvm"
    allowed_domains = ["stock.finance.sina.com.cn"]

#    def __init__(self, category=None, *args, **kwargs):
#        super(olinvmSpider, self).__init__(*args, **kwargs)
        

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

    start_urls =[]
    for i in range(id_fund[6][1]):
        start_urls.append(     
            "http://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNavcur?callback=jQuery111206373235338915035_1462325512626&symbol=%s&datefrom=&dateto=&page=%s&_=1462325512717" % (id_fund[6][0], str(i+1))
	)

    def parse(self, response):
        olinvm = OlinvmItem()
        olinvm['pre_text'] = response.body
        return olinvm

#    def parse(self, response):
#        filename = "he"
#        with open(filename, 'wb') as f:
#            f.write(response.body)
