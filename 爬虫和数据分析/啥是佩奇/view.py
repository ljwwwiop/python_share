'''
    Peiqi.py 可视化过程
'''
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
# 添加中文包
import jieba
import numpy as np
import pandas as pd

df = pd.read_csv('danmu.csv',header=None)
text = ''
for line in df[1]:
    text += ' '.join(jieba.cut(line, cut_all=False))
image = np.array(Image.open("timg (1).jpg"))
# 词云设置
wc = WordCloud(
    # background_color='white',
    # mask=image,
    # font_path=r'D:\python\pycharm\ziti\simhei.ttf',
    # max_words=2000,
    # max_font_size=80,
    # random_state=30,
    max_words=350,random_state=200,scale=5,collocations=False,max_font_size=70,background_color="white",font_path=r'D:\python\pycharm\ziti\simhei.ttf'
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
wc.to_file('peiqi.jpg')
print('词云运行成功!')





