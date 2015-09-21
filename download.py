import os
import time
import random
import requests


Dir = '简单验证码'
gapTime = 0.05
url = 'http://drops.wooyun.org/wooyun/captcha.php?{0}'
header = {'User-Agent':
          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36', }

session = requests.Session()
session.headers.update(header)


def getImg(path, url):
    '''
    下载图片的函数
    给定网址及文件夹，下载指定图片至指定文件夹
    '''
    imgName = random.random()
    imgUrl = url.format(imgName)
    try:
        req = session.get(imgUrl, timeout=3)
        img = req.content
        with open('%s\%s.gif' % (path, imgName), 'wb') as f:
            f.write(img)
        print('图片下载成功，图片名： %s' % imgName)
    except Exception as e:
        print('图片下载失败！原因：')
        print(e)


def main(num):
    now = 0
    if not os.path.isdir(Dir):
        print('未找到文件夹“%s”，现在自动创建' % Dir)
        os.makedirs(Dir)
    print('开始下载验证图至文件夹“%s”' % Dir)
    print('现在开始下载，下载时间间隔默认为%s秒' % gapTime)
    path = r'%s\%s' % (os.getcwd(), Dir)

    while now < num:
        now += 1
        print('\n现在下载第%s张验证码中...' % now)
        getImg(path, url)
        time.sleep(gapTime)

if __name__ == "__main__":
    main(10)
