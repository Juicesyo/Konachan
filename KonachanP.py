import requests #为了请求网站
import time #耗时计算,延迟
from bs4 import BeautifulSoup #为了从网站中抓取需要的部分
import os #为了将图片写到本地
import socket

#url='https://konachan.net/post?page='
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
}
t=time.time()
page=1 #默认第一页
nP=1 #默认继续获取图片
late=5 #延迟
number=0 #重试次数
if socket.setdefaulttimeout(10):
    print('pass.')
    exit(-1)

path = r'C:\Users\Juice\Desktop\pic'

if not os.path.exists(path):
    os.makedirs(path)
    print(path,'创建目录成功。')
else:
    print('目录已经存在。')

def save_img(id,pixel,img_url,number): #保存图片函数
    try:
        img = requests.get(url=img_url,headers=headers)
        name = id +'('+pixel+')'+'.jpg'
        f = open(path+'\\'+name, 'ab')
        f.write(img.content)
        print(name, '图片保存成功。')
        f.close()
    except:
        number = number + 1
        if number>5:
            print('频繁操作。')
            exit(-1)
        print('try save.',number)
        save_img(id,pixel,img_url,number)


def konachan(page, number):
    global text
    global nP
    page=str(page)
    url = "https://konachan.net/post?page=" + page
    try:
        text = requests.get(url=url,headers=headers).text
        # print(soup)
    except:
        number = number + 1
        if number > 3:
            print('频繁操作。')
            exit(-1)
        #time.sleep(late)
        print('try again.',number)
        konachan(page,number)
    soup = BeautifulSoup(text, features="lxml")
    div = soup.find_all('li', style='width: 170px;')
    for i in div:
        img_url=i.contents[1].get('href') #图片链接
        id = i.get('id') #图片id
        pixel = i.contents[1].contents[1].string #分辨率
        #print(id,img_url,pixel)
        if id +'('+pixel+')'+'.jpg' in os.listdir(path): #判断图片是否存在
            print(id, '已存在。')
            nP=0
        else:
            number=0
            save_img(id, pixel, img_url,number)

if __name__ == "__main__":
    konachan(page,number)
    time.sleep(late)
    while nP == 1:
        print('自动从下一页获取。')
        page = page + 1
        konachan(page,number)

#time.sleep(late)
#socket.close()
print('time:',int(time.time()-t))