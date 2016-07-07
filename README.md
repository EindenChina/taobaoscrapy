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
sudo pip3 install pymysql
sudo pip3 install xlsxwriter
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

```
run.bat
或者
python mtaobao.py
```

4.程序出错
有时候程序运行中途断网或者其他原因,如误点下载图片,而图片几万张不耐烦终止程序,导致程序
运行没完成。不必担心,只要原始数据在,一切好办。
将 data 中的原始数据移到 help 文件夹中

```
runhelp.bat
或者
python help.py
```

do not understand?contact me.
author:hunterhug
2015/11

--------------------------------------------------------------

# 补充
2016/7/7改bug
请查看JSON.json，淘宝json数据字段变更，导致程序出错<br/>

淘宝需要验证时，请往subcookie.txt填东西，参考pdf<br/>

 '手机折扣'字段失效
```
Traceback (most recent call last):
  File "mtaobao.py", line 322, in <module>
    itemlist.append(item['mobileDiscount'])
KeyError: 'mobileDiscount'
```

'URL地址'字段失效
```
Traceback (most recent call last):
  File "mtaobao.py", line 328, in <module>
    itemlist.append(item['auctionURL'])
KeyError: 'auctionURL'
```

已经更正