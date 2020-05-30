#!/usr/bin/env python
# coding=utf-8
# code by CyzCc
# Date 2020/06/01
import requests
import time
import os
print('''
 _ __ ___ | |___  ___ __ _ _ __  
| '_ ` _ \| / __|/ __/ _` | '_ \ 
| | | | | | \__ \ (_| (_| | | | |
|_| |_| |_|_|___/\___\__,_|_| |_|   by CyzCc
''')#图形由figlet生成
url = input("请输入url:")
dic = input("DIR.txt、dict.txt、beifenwenjian.txt、PHP.txt\n请输入需要的字典文件:")
def scan():
    i = 0
    for data in open(dic):
        #print(data)
        urls = url+data
        urls = urls.replace('\n','')
        response = requests.get(url = urls).status_code
        print('['+str(response)+']==>'+data)
        if str(response) != '404':
            print('-----------------------'+data)
            with open('result.txt', "a") as f:
                f.write('['+str(response)+']==>'+data)
    with open('result.txt', "r") as a:
        res = a.read()
        print('==========================\n扫描到可访问路径:\n')
        print(res)
        print('==========================')
    os.remove('result.txt')
if __name__ == '__main__':
    scan()