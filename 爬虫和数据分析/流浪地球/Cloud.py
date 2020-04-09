'''
    豆瓣上  流浪地球  差评词云
'''
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
import numpy as np
import pandas as pd

text = open('Aliencom.txt','r',encoding='utf-8',errors='ignore').read()

wc = WordCloud(
    background_color='white',
    # mask=image,
    font_path=r'D:\python\pycharm\ziti\simhei.ttf',
    max_words=2000,
    max_font_size=80,
    random_state=30,
    # max_words=350,random_state=200,scale=5,collocations=False,max_font_size=50,background_color="white",font_path=r'D:\python\pycharm\ziti\simhei.ttf'
)
wc.generate_from_text(text)

# 查看高频词汇细节
a = 1
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
# print(sort[:50])
for i in sort[:50]:
    print(a,' ',i)
    a+=1


plt.imshow(wc, interpolation='bilinear')
plt.axis('off',)
plt.show()
wc.to_file('Aliencomment.jpg')
print('词云运行成功!')



