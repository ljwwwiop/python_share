from scrapy import cmdline
import  uuid

# uuid 通用唯一标识符 全局唯一 不会重复
# #产生启动脚本
# 方便
id = str(uuid.uuid4()).replace('-','')
cmdline.execute("scrapy crawl jobs -o result_{0}.csv".format(id).split())