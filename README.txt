# 说明
由于Github 打包的exe某些文件上传被.gitignore了，所以不提供windows二进制包
更多参考：[一只尼玛博客园](http://www.cnblogs.com/nima/p/5324490.html)

---------------------------------------------------------
一个抓取淘宝天猫关键字搜索商品的爬虫使用python3.4，爬虫程序已经封装好<br />
支持抓取商品标题/商品价格/商品销量/商品图片等<br />
使用请直接点击exe文件夹中后缀为exe的文件或者run.bat<br />

#更多说明参考pdf

一个抓取淘宝的Python爬虫
------------------------------------------------------------
A scarpy for catch taobao item info<br />
using python3<br />
run just click exe/*.exe</br>

more please watch the pdf

# 使用
1.安装模块请使用
```
pip3 install *
```

2.打包windows二进制
从万能仓库 http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze 下载对应版本的打包库,然后:
```
pip3 install cx_Freeze-4.3.4-cp35-none-win_amd64.whl
```

转到源代码文件夹
```
python setup.py build
```

3.运行
把exe.win32-3.4移到根目录taobaoscrapy，任意改名，以下改为exe，文件目录如下：
```
taobaoscrapy
-------source
-------exe
-------exehelp
-------help
```

运行
```
run.bat
```


do not understand?contact me.

author:hunterhug
2015/11

# 补充
