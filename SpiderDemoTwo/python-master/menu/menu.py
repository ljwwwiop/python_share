#!/usr/bin/env python
# -*- coding: utf-8 -*-

china ={
    '湖南': {
        '娄底':['新化县','冷水江市','涟源市','双峰县'],
        '长沙':['天心区','芙蓉区','岳麓区','开福区','雨花区']
    },
    '广东':{
        '广州':['天河区','白云区','黄埔区','萝岗区'],
        '深圳':['罗湖区','福田区','南山区','盐田区']
    }
}

provice_dict = {}
city_dict = {}
county_dict = []

pro_flag = 1
city_flag = 1
print('---------Welcom to China------------')

while pro_flag:
    pro_count = 0
    for pro in china:
        pro_count += 1
        provice_dict[str(pro_count)] = pro
        print(pro_count,pro)

    pro_choose = input('请选择省:').strip(" ")
    while True:
        if pro_choose in provice_dict:
            pro_key = provice_dict[pro_choose]
            citys = china[pro_key]
            city_count = 0
            for city in citys:
                city_count += 1
                city_dict[str(city_count)] = city
                print(city_count,city)
        elif pro_choose == 'b':
            break
        elif pro_choose == 'q':
            print("Bye bye....")
            exit(0)
        else:
            print("请重新输入")
            break

        city_choose = input('请选择市:').strip(" ")
        while True:
            if city_choose in city_dict:
                city_key = city_dict[city_choose]
                counties = china[pro_key][city_key]
                county_count = 0
                for county in counties:
                    county_count += 1
                    print(county_count,county)
                exit(0)
            elif city_choose == 'b':
                break
            elif city_choose == 'q':
                exit(0)
            else:
                print("请重新输入----")
                break

