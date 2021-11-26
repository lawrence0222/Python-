import os
import requests
from bs4 import BeautifulSoup
import time
for i in range(1,2):
    url = 'https://www.books.com.tw/web/sys_bbotm/books/020101/?loc=P_0001_3_00'+str(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    time.sleep(5)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #txt
    time.sleep(5)
    url2 = soup.find_all(class_= 'msg')[0].a['href']
    resp2 = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(resp2.text, 'html.parser')
    path = (soup.find_all(class_='cover')[0]['alt']+'.txt')
    i_text = soup2.find_all(class_ = 'mod_b type02_m057 clearfix')[0]
    a_text = soup2.find_all(class_ = 'mod_b type02_m057 clearfix')[1]
    c_text = soup2.find_all(class_ = 'mod_b type02_m057 clearfix')[2]
    try:
        with open('D:\\text\\I\\'+path, 'w',encoding = 'utf-8') as f:
            f.write(i_text.text)
            f.close()
            print("文件保存成功")
        with open('D:\\text\\A\\'+path, 'w',encoding = 'utf-8') as g:
            for k in a_text:
                g.write(k.text)
            g.close()
            print("文件保存成功")
        with open('D:\\text\\C\\'+path, 'w',encoding = 'utf-8') as h:
            for l in c_text:
                h.write(l.text)
            h.close()
            print("文件保存成功")
    except:
        print("爬取失敗")