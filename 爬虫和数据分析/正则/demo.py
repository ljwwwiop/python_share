'''
    正则表达式练习  用法
'''
import re
'''
    贪婪 和 非贪婪 可以?转换未非贪婪模式  默认是贪婪模式
    ？只能重复0次或者1次    *是重复0或者无数次   .匹配所有字符除了换行\n
    {1,2}重复次数 1-2次
'''
# a = "pytho0python1pythonn2"

# ？只能重复0次或者1次
# r = re.findall("python?",a)

# {1,2}重复次数 1-2次 并且现在是贪婪模式 相似结果全部出来
# 添加？后 非贪婪模式 限定次数0或1 找到python 结束不找到pythonn
# r = re.findall("python{1,2}?",a)

'''
    边界匹配 ,假如QQ \d{4,8} 数字 4-8位之间的 ,表示到
    前^ 后$ 限定 匹配4-8之间的 ^0 0开头 1$ 1结尾
'''

# a = "1206957838"
# r = re.findall("^\d{4,8}$",a)

'''
    组的重复处理 需要匹配的内容()里面{}限定次数
    [] 和 ()区别[]里面字符是或的关系  ()是切的关系
'''
# a = "pythonpythonpythonpythondaspcopythonpython"
# r = re.findall("(python){1}",a)

'''
    re.findall 的模式参数 re.I 忽略参数大小写 | - and关系  re.S 匹配换行符\n
    .匹配除换行符\n之外的所有字符 \s空白字符\S \w单词字符 \W  
'''

# a = "Python中是javA\n,andC++ is great"
# r = re.findall(r"java.{1}",a,re.I|re.S)

'''
    替换 re.sub("原","新",对象,0) 0表示替换个数 默认是0 所有
    新这个地方 可以用函数替换,原 地方可以写匹配模式
'''
# a = "pythonPythonJavaSePython9999Python"
# a = "A8c351266120CPFLCJDOc22"
# def convert(values):
#     # matched = values.group() 接受了 原来要替换的values
#     matched = values.group()
#     if int(matched)>=5:
#         return '0'
#     else:
#         return '-_-'


# r = re.sub("\d",convert,a)
# r = a.replace("Python","py")

'''
    match 与 search 都是有且仅有一次
    match 从开头开始匹配 如果没有匹配到 则是空
    search 全局搜索 直到第一个找到字符串的结果 返回那一个 r.group输出
'''

'''
    组的意义 group () group(0)是特殊情况 总是完整记录下整个,需要从1开始
    
'''
# s = "life is so short,i need use python,i love python,and l love china"
s = "<a class=x style=height:75px href=http://www.baidu.com/link?url=vatk2Uh-_6N9uNp_de10bno5Fhdu0R2KIgP_ZJPcLd3 target=_blank><img =c-img c-img6 src=https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=212302559,2818254670&amp;fm=58&amp;s=2A62DC16C0E151034C1333570300D0E6&amp;bpow=121&amp;bpoh=75 style=height:75px;></a>"

# s = "<class=x href=www.baidu.com >"
r = re.findall(".*bpoh=75.(.*);",s)
# r1 = re.search("life(.*)python",s)
# style=height:75px;

print(s)
print(r)
# print(r1)
# print(r1.group(1))

