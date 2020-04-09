'''
    Json 详解 json 是一种轻量级的数据交换结构  xml是一种重量级的  html是一种特殊的xml
    1 易理解性 2 跨语言的  3 可读性
    NoSql mongodb
'''

import json

# 可以是 dict 字典  []数组 集合  ()元组
# 布尔类型 json 在python中自动转换为大写
json_str = '[{"name":"连加未","age":18},{"name":"yes","marry":false}]'

# 反序列化  解析json 到python
info = json.loads(json_str)
for i in info:
    print(i["name"])

# 序列化 python 到json 字符串
json_str1 = [{"name":"连加未","age":18},{"name":"yes","marry":False}]
info1 = json.dumps(json_str1)

print(info)
print(type(info))
print(info1)
print(type(info1))


'''
    json            python
    object          dict
    array           list
    string          str
    number          int
    number          float
    true            True
    null            None
'''
'''
    JSON 和JSP 没有直接关系
    JSON 对象     JSON        JSON字符串
    
    在JSP中 存在json对象，但是python中是不存在JSON对象的
    JSON 是不同语言的中间公共转换
    JSON 有自己的数据类型 虽然它和javascript相似
'''


