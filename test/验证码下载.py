import os
import time
import threading
import random
from urllib import request


end = 0
num = 0
Dir1 = '简单验证码1'
url1 = 'http://drops.wooyun.org/wooyun/captcha.php?{0}'
Dir2 = '简单验证码2'
url2 = 'https://account.bilibili.com/captcha?t={0}'
Dir3 = '数字验证码'
url3 = 'http://www.cepin.com/common/verifycode?width=72&amp;height=40&time={0}'
Dir4 = '数字字母验证码'
url4 = 'http://m.zhihu.com/captcha.gif?r={0}'


def getImg(Dir, url):
    '''
    下载图片的函数
    给定网址及文件夹，下载指定图片至指定文件夹
    '''
    if mode == '1' or mode == '2':
        imgName = random.random()
    else:
        imgName = str(int(time.time() * 1000))
    imgUrl = url.format(imgName)
    try:
        req = request.urlopen(imgUrl)
        img = req.read()
        with open(r'%s\%s\%s.gif' % (os.getcwd(), Dir, imgName), 'wb') as f:
            f.write(img)
        print('图片下载成功，图片名： %s' % imgName)
    except Exception as e:
        print('图片下载失败！原因：')
        print(e)


class GetInput(threading.Thread):

    """子线程获取用户输入，输入为特定值(q)时返回结束指令：end = 1"""

    def __init__(self):
        threading.Thread.__init__(self)
        # self.arg = arg

    def run(self):
        global end

        i = input()
        if i == 'q':
            end = 1
            print('发送结束指令...')


while True:
    print('用途：自动下载验证码图片')
    print('特别说明：下载开始后,可以通过按下“q”键+回车键结束下载\n')
    print('请输入“1”或“2”选择要下载的验证码，敲下回车键确认选择')
    mode = input('“1”和“2”的验证码均较为简单，分别来自“乌云”和“bilibili”，\n输入“3”下载纯数字验证码（来自“测聘网”），“4”下载数字+字母验证码（来自“知乎”）：\n')
    if mode == '1':
        Dir = Dir1
        url = url1
        break
    elif mode == '2':
        Dir = Dir2
        url = url2
        break
    elif mode == '3':
        Dir = Dir3
        url = url3
        break
    elif mode == '4':
        Dir = Dir4
        url = url4
        break
    else:
        print('你的输入是%s，请重新选择' % mode)

if not os.path.isdir(Dir):
    print('未找到文件夹“%s”，现在自动创建' % Dir)
    os.makedirs(Dir)
print('开始下载验证图至文件夹“%s”' % Dir)
print('现在开始下载，下载时间间隔默认为0.1秒')

GetInput().start()
while True:
    num += 1
    if end == 1:
        print('\n图片下载结束，共下载%s张，保存于 “%s” 中' % (num, Dir))
        break
    print('\n现在下载第%s张验证码中...' % num)
    getImg(Dir, url)
    time.sleep(0.1)
