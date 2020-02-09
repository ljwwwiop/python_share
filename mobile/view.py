#!/usr/bin/env python
'''
    可视化过程
    词云 还有  可视图
    使用蒙版图像可以生成任意形状的wordcloud
    jieba 中文包 词云 不能识别中文 font_path='simfang.ttf' 显示中文
'''
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
# 添加中文包
import jieba

# 读取文本
text = open('HuaWei.txt','r',encoding='utf-8',errors='ignore').read()
# print(text)
# 通过jieba分词进行分词并通过空格分隔
# wordlist_after_jieba = jieba.cut(text, cut_all=True)
# wl_space_split = " ".join(wordlist_after_jieba)

# 打开小米图片
image = np.array(Image.open("timg.jpg"))
# 根据图片给字体上色
# image_colors = ImageColorGenerator(image)
stopwords = set(STOPWORDS)
stopwords.add("said")

# 生成一个词云图像
wordcloud = WordCloud().generate(text)

# matplotlib的方式展示生成的词云图像
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#max_font_size设定生成词云中的文字最大大小
#width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是他对中文支持不好
wordcloud = WordCloud(max_words=350,random_state=200,scale=5,collocations=False,max_font_size=70,background_color="white",font_path=r'D:\python\pycharm\ziti\simhei.ttf',stopwords=stopwords,mask=image).generate(text)
# wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud, interpolation="bilinear")
plt.title("华 为 用 户 评 价",fontsize=25)
plt.axis("off")
plt.figure(figsize=(8,8),dpi=80)
# plt.imshow(image,cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")

wordcloud.to_file("huaweiuser.png")
plt.show()






