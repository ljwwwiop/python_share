#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
需求：输入出生日月年，计算生命密码
备注：生命密码算法解说参考网址：https://tieba.baidu.com/p/2167628810
"""
import operator
import re
import requests
from bs4 import BeautifulSoup
from fontTools import unicode


class LifeCode():
    def insertBirthday(self):
        name = input('请输入您的中文姓名：')
        ischinese=self.is_chinese(name)
        if name and ischinese is True :
            tf=True
            while tf:
                birthday=input('请按格式2018-01-02输入您的阳历出生日期：')
                if birthday and len(birthday)==10:
                    bdinfo=birthday.split('-')
                    year=bdinfo[0]
                    month=bdinfo[1]
                    day=bdinfo[2]

                    if len(year)==4 and len(month)==2 and len(day)==2:
                        if int(month)<=12 and int(day)<=31:
                            print('您的出生年月日为：%s年%s月%s日'%(year,month,day))
                            yn=input('确认请输入Y，修正请输入N：')
                            if operator.eq('Y',str(yn)) or operator.eq('y',str(yn)):
                                tf = False  # 输入合法，终止死循环
                                A=int(day[0]) if len(day)>1 else 0
                                B=int(day[1]) if len(day)>1 else int(day)
                                C=int(month[0]) if len(month)>1 else 0
                                D = int(month[1]) if len(month) > 1 else int(month)
                                E = int(year[0])
                                F = int(year[1])
                                G = int(year[2])
                                H = int(year[3])

                                I = self.addRule(A, B)
                                J = self.addRule(C, D)
                                K = self.addRule(E, F)
                                L = self.addRule(G, H)

                                M = self.addRule(I, J)
                                N = self.addRule(K, L)

                                O = self.addRule(M, N)

                                P = self.addRule(M, O)
                                Q = self.addRule(N, O)
                                R = self.addRule(Q, P)

                                X = self.addRule(I, M)
                                W = self.addRule(J, M)
                                S = self.addRule(X, W)

                                V = self.addRule(K, N)
                                U = self.addRule(L, N)
                                T = self.addRule(V, U)

                                #幸运数字=年份 除以 (名字的笔画数（连名带姓）+月+日)得出的数，各个位数相加
                                number=int(int(year)/(int(self.countStrokes(name))+int(month)+int(day)))
                                if len(str(number))==1:
                                    luckyNum=number
                                elif len(str(number))==2:
                                    luckyNum = self.addRule(int(str(number)[0]),int(str(number)[1]))
                                elif len(str(number)) == 3:
                                    number=int(str(number)[0])+int(str(number)[1])+int(str(number)[2])
                                    luckyNum = number if len(str(number))<2 else int(str(number)[0])+int(str(number)[1])

                                talentNum=A+B+C+D+E+F+G+H
                                outTrend=S+R+T
                                outTrendType=self.outTrendType(outTrend)

                                print('''\n您的生命密码图为：
                                          %s               
                                         %s %s     
                                    --------------         
                                %s=%s%s    / %s \   %s%s=%s   
                                      / %s   %s \           
                                    / %s%s    %s%s \         
                                  /%s%s %s%s    %s%s %s%s\\\n'''%(R,Q,P,S,X,W,O,V,U,T,M,N,I,J,K,L,A,B,C,D,E,F,G,H))

                                print('您的主性格数字：%s，在五行中属：%s'%(O,self.wuxing(O)))
                                print('您的幸运数字：%s' % luckyNum)
                                print('您的天赋数字：%s' % talentNum)
                                print('您的生命数字：%s'%self.addRule(talentNum,0))
                                print('您的潜意识密码：%s%s%s' % (O,I,L))
                                print('您的内心密码：%s%s%s' % (O,M,N))
                                print('您的外心密码：%s%s%s' % (S,R,T))
                                print('您的外在动向等于：%s,您是【%s】'%(outTrend,outTrendType))
                                print("程序计算完毕，感谢使用！")
                            elif operator.eq('N',str(yn)) or operator.eq('n',str(yn)):
                                print("您选择重新输入：")
                        else:
                            print('请检查出生年月的格式！\n')
                    else:
                        print('请检查出生年月的格式！\n')
                else:
                    print('请检查出生年月的格式！\n')
        else:
            print('请输入合法的中文名！\n')
            self.insertBirthday()

    def countStrokes(self,chinese):
        '''利用爬虫得到输入汉字的笔画数'''
        url='https://bihua.911cha.com/'
        data={'q':chinese}
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
         }
        response=requests.post(url=url,headers=headers,data=data)
        status=response.status_code
        stroke=0
        if status==200:
            result=response.text
            soup=BeautifulSoup(result,'lxml')
            strokeSoup=soup.select('div span.pink')
            stroke=strokeSoup[1].text if len(strokeSoup)>1 else 0
        return stroke

    def is_chinese(self,char):
        """判断是否包含中文"""
        if not isinstance(char, unicode):
            char = char.decode('utf8')
        if re.search(r"[\u4e00-\u9fa5]+", char):
            return True
        else:
            return False

    def addRule(self,num1,num2):
        '''两数相加规则，结果始终是0-9的个位数'''
        value=num1+num2
        if value>9:
            value=int(str(value)[0])+int(str(value)[1])
        return value

    def wuxing(self,num):
        '''计算五行属性'''
        if int(num)==1 or int(num)==6:
            value = '金'
        elif int(num)==2 or int(num)==7:
            value = '水'
        elif int(num) == 3 or int(num) == 8:
            value = '火'
        elif int(num)==4 or int(num)==9:
            value = '木'
        elif int(num) == 5 :
            value = '土'
        return value

    def outTrendType(self,outTrend):
        '''计算外在动向属性'''
        if int(outTrend)>3:
            type ='理想主义者'
        if int(outTrend)>6:
            type = '现实主义者'
        if int(outTrend)>9:
            type = '远见主义者'
        return type

    #执行函数
    def run(self):
        while 1:
            print('\n欢迎使用生命密码计算程序！\n')
            self.insertBirthday()
            print()

if __name__ == '__main__':
    lfcode=LifeCode()
    lfcode.run()



