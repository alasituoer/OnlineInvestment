# -*- coding: utf-8 -*-

# Scrapy settings for olinvm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'olinvm'

SPIDER_MODULES = ['olinvm.spiders']
NEWSPIDER_MODULE = 'olinvm.spiders'

ITEM_PIPELINES = {
    'olinvm.pipelines.OlinvmPipeline': 1,
}
#设置延迟
#一是防止服务器拒绝响应请求
#二是能顺序处理反馈（特别是需要将结果按时间排序）
#但是这样做的坏处就是会降低程序的运行速度
DOWNLOAD_DELAY = 0.25

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'olinvm (+http://www.yourdomain.com)'
