import numpy as np
import pandas as pd

user_info = pd.read_csv("userInfo.csv")
#数据清洗
user_info1 = user_info[(user_info["性别"] == "男") | (user_info["性别"] == "女")]#去除掉性别不为男女的部分
user_info1 = user_info1.reindex(range(0,103))#重置索引


user_index1 = user_info1[(user_info1["国家城市"].isnull() == True)&(user_info1["星座"].isnull() == False)
                         &(user_info1["星座"].map(lambda s:str(s).find("座")) == -1)].index
for index in user_index1:
    user_info1.iloc[index,3] = user_info1.iloc[index,2]

user_index2 = user_info1[((user_info1["国家城市"].isnull() == True)&(user_info1["星座"].isnull() == True)
                          &(user_info1["年龄"].isnull() == False)&(user_info1["年龄"].map(lambda s:str(s).find("岁")) == -1))].index
for index in user_index2:
    user_info1.iloc[index,3] = user_info1.iloc[index,1]

user_index3 = user_info1[((user_info1["星座"].map(lambda s:str(s).find("座")) == -1)&
                          (user_info1["年龄"].map(lambda s:str(s).find("座")) != -1))].index
for index in user_index3:
    user_info1.iloc[index,2] = user_info1.iloc[index,1]

user_index4 = user_info1[(user_info1["星座"].map(lambda s:str(s).find("座")) == -1)].index
for index in user_index4:
    user_info1.iloc[index,2] = "未知"

user_index5 = user_info1[(user_info1["年龄"].map(lambda s:str(s).find("岁")) == -1)].index
for index in user_index5:
    user_info1.iloc[index,1] = "999岁"#便于后续统一处理

user_index6 = user_info1[(user_info1["国家城市"].isnull() == True)].index
for index in user_index6:
    user_info1.iloc[index,3] = "其他"

user_info1.to_csv('ClearUserInfo.csv',index=False,mode='a+',encoding='utf-8_sig')

print(user_info)
print('---'*20)
print(user_info1)

