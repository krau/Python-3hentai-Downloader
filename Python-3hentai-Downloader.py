import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys
import getopt
import shutil

opts, args = getopt.getopt(sys.argv[1:], '-z', ['zip'])

id = int(input("请输入3hentai本子id："))
bzurl = os.path.join('https://3hentai.net/d',
                     '{id}/1'.format(id=id))
bzurl = bzurl.replace('\\', '/')  # 把os.path.join产生的反斜杠转换为正斜杠,麻了

#请求并获取本子总页数
ua = UserAgent()
head = {"User-Agent": ua.random}
reqbz = requests.get(bzurl, headers=head)
soup = BeautifulSoup(reqbz.text, 'lxml')
maxnum = soup.select(
    'div.reader-nav:nth-child(1) > div:nth-child(2) > a:nth-child(3) > span:nth-child(3)')[0].string # 本子总页数

#在脚本同路径下创建以本子名为名的文件夹
bzname = soup.select('html body div#reader div.reader-nav.d-flex.flex-row div.reader-back span.reader-title')[0].string #获取本子名
path0 = os.path.dirname(__file__) # 获取脚本当前路径
createdir = os.path.join('{path0}'.format(path0=path0),'{bzname}'.format(bzname=bzname))
createdir = createdir.replace('\\','/')
createdir = createdir.replace(' ','_')
createdir = createdir.replace('|','_') #特殊字符转换
os.mkdir(createdir)

# 开始逐页下载
print('开始下载啦~共{maxnum}页！'.format(maxnum=maxnum))
dlnum = 1
while dlnum <= int(maxnum):
    imgurl = os.path.join('https://s7.3hentai.net/',
                          'd{id}'.format(id=id), '{dlnum}.jpg'.format(dlnum=dlnum))
    imgurl = imgurl.replace('\\', '/')
    getimg = requests.get(imgurl,headers=head)
    file = os.path.join('{path0}'.format(path0=path0),'{bzname}'.format(bzname=bzname),'{dlnum}.jpg'.format(dlnum=dlnum))
    file = file.replace('\\','/')
    file = file.replace(' ','_')
    file = file.replace('|','_')
    with open(file,'wb') as f:
        f.write(getimg.content)
    print('第 {dlnum} 页下载完成'.format(dlnum=dlnum))
    dlnum += 1
else:
    print('{bzname} 下载完成！'.format(bzname=bzname))


#若传入了-z或--zip则打包，并删除原文件
for opt_name, opt_value in opts:
    if opt_name in ('-z', '--zip'):
        print('正在打包...')
        shutil.make_archive('{bzname}'.format(bzname=bzname),'zip','{createdir}'.format(createdir=createdir))
        shutil.rmtree('{createdir}'.format(createdir=createdir))
        print('打包完成！')