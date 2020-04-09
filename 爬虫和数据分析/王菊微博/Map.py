from wordcloud import WordCloud
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 创建数据
#参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud( r'.\simhei.ttf',background_color = 'White', max_words = 150,width=350,height=200)

name = ["女性","摩羯座","20岁","21岁","22岁","23岁","24岁","25岁","广州","杭州","成都","武汉","长沙","上海","北京","海外","美国","深圳"]
value = [20,20,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]#词的频率
dic = dict(zip(name, value))#词频以字典形式存储
wc.generate_from_frequencies(dic)#根据给定词频生成词云

plt.imshow(wc)
plt.axis("off")#不显示坐标轴
plt.show()
wc.to_file('word.jpg')

