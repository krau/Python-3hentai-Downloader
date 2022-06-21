# Python-3hentai-Downloader

这是一个python程序，用来下载3hentai上的漫画

## 使用
1. 下载Python-3hentai-Downloader.py
2. 在Python-3hentai-Downloader.py所在文件夹中，打开终端，执行`python .\Python-3hentai-Downloader.py`(powershell)或`python Python-3hentai-Downloader.py`(cmd)
3. 根据提示输入3hentai的漫画id，等待下载完成


注：3hentai的漫画id 指下图红框所框出的数字

![](WhatIsId.png)

### 参数
- `-z` or `--zip`
    下载并打包压缩漫画

示例：
`python Python-3hentai-Downloader.py -z`

## bug
~~由于某些漫画名字过长，超过了系统或python的限制，导致无法下载。正尝试通过判断文件名长度，将过长的文件名改为以id创建文件夹的方法解决，ToDo。~~

更正：并非由于漫画名过长，而是因为某些漫画名中带有"|"字符，现已通过将其转化为下划线修复。感谢 @AHCorn
