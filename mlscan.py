#!/usr/bin/env python
# coding=utf-8
# code by CyzCc
# Date 2020/06/01
import requests
import sys
import requests.packages.urllib3
import threading
import queue
import time

q=queue.Queue()

print('''
 _ __ ___ | |___  ___ __ _ _ __  
| '_ ` _ \| / __|/ __/ _` | '_ \ 
| | | | | | \__ \ (_| (_| | | | |
|_| |_| |_|_|___/\___\__,_|_| |_|
''')#图形由figlet生成
print("Dictionary： DIR.txt、dict.txt、beifenwenjian.txt、PHP.txt")
print("python mlscan.py url 字典  线程数")
print("Example： python mlscan.py http://xxxxxx/ PHP.txt 2")


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}

def print_result(a):
    print('==========================\n扫描到可访问路径:')
    for j in a:
        print(j)
    print('==========================')
    print("耗时："+time.asctime(time.localtime(time.time()-d)))

a = []
def scan(url):
    while not q.empty():
        data = q.get()
        urls = url+'/'+data
        urls = urls.replace('\n','')
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url = urls,headers = headers, verify=False).status_code
        print('[' + str(response) + ']==>' + data.replace('\n',''))
        if response == 200 and response == 301 and response == 302:
            #print('-----------------------'+data.replace('\n',''))
            a.append(data)


if __name__ == '__main__':
    d = time.time()
    url = sys.argv[1]
    dic = sys.argv[2]
    xc = sys.argv[3]
    for data in open(dic):
        q.put(data)         #传递data
    #scan(url)
    lock = threading.Lock()
    for i in range(int(xc)):  # 加入多线程
        t = threading.Thread(target=scan, args=(url,))
        t.start()
