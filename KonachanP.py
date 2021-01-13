import requests #为了请求网站
import time #耗时计算
from bs4 import BeautifulSoup #为了从网站中抓取需要的部分
import os #为了将图片写到本地
#user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75
t=time.time()
page = '1' #页数
url = "https://konachan.net/post?page=" + page + '&tags='
text = requests.get(url).text
soup = BeautifulSoup(text)
#print(soup)
#div = soup.find_all('a', class_ = 'directlink')
div = soup.find_all('li',style = 'width: 170px;')
#print(div,div2)
#div = soup.find_all('span', class_ = 'directlink')
#str_a = BeautifulSoup(str(div[0]))
#a = str_a.find_all('a')
path = r'C:\Users\Juice\Desktop\pic'

if not os.path.exists(path):
    os.makedirs(path)
    print(path,'创建目录成功。')
else:
    print('目录已经存在。')

def save_img(id,pixel,img_url):  #保存图片
    img = requests.get(img_url)
    name = id +'('+pixel+')'+'.jpg'
    f = open(path+'\\'+name, 'ab')
    f.write(img.content)
    print(name, '图片保存成功。')
    f.close()
#number=0
for i in div:
    #skip = 0
    # number=number+1
    img_url=i.contents[1].get('href')
    id = i.get('id')
    pixel = i.contents[1].contents[1].string
    #print(id,img_url,pixel)
    #for n in os.listdir(path):
    if id +'('+pixel+')'+'.jpg' in os.listdir(path):
        #print(id +'('+pixel+')'+'.jpg' in os.listdir(path))
        print(id,'已存在。')
    else:
        save_img(id, pixel, img_url)
print('time:',time.time()-t)
