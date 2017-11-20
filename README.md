# 天猫淘宝关键字商品搜索说明

已经太久远了，不再维护了。

本人开了新库，使用Golang语言, 更多精彩请移动到[https://github.com/hunterhug/GoTaoBao](https://github.com/hunterhug/GoTaoBao), 更多参考：[一只尼玛博客园](http://www.cnblogs.com/nima/p/5324490.html)

![](doc/seeme0.jpg)

仍然能跑，2017/6。

```
一个抓取淘宝的Python爬虫
---------------------------------------------------------

一个抓取淘宝天猫关键字搜索商品的爬虫使用python3.4，爬虫程序已经封装好
支持抓取商品标题/商品价格/商品销量/商品图片等
使用请直接点击exe文件夹中后缀为exe的文件或者run.bat

------------------------------------------------------------
```

>更多说明参考pdf

# 一.项目结构

```
-----taobaocomment
	-------source	源代码
	-------data 原始数据
	-------image 你要的图片
	-------excel	你要的结果
	-------exe.rar	请解压变成exe
	-------exehelp.rar	请解压变成exehelp
	-------run.bat	你要跑的脚本
	-------runhelp.bat 
```

# 二.本地环境准备

安装[python3](https://www.python.org/downloads/)。然后设置环境变量。

## 1.安装依赖模块

```
pip3 install -r requirement.txt
```

如果安装模块失败, 那么可能是`cx_Freeze`下载失败, 从[万能仓库](http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze) 下载对应版本的打包库,然后:

```
pip3 install cx_Freeze-4.3.4-cp35-none-win_amd64.whl
```

## 2.打包exe

转到源代码文件夹`source`, 执行打包命令！

```
python setup.py build
```

把`exe.win32-3.4`文件夹移到根目录，改名为exe, 同样`python setuphelp.py build`打包辅助工具.

# 三.开始使用

正常执行

```
cd source
python mtaobao.py

或者

run.bat
```

有时候程序运行中途断网或者其他原因,如误点下载图片,而图片几万张不耐烦终止程序,导致程序<br/>
运行没完成。不必担心,只要原始数据在,一切好办。<br/>
将 data 中的原始数据移到 help 文件夹中

继续！

```
cd source
python help.py

或者

runhelp.bat
```

# 四.演示
![](doc/seeme1.jpg)
![](doc/seeme2.jpg)
![](doc/seeme3.jpg)
![](doc/seeme4.jpg)


Do not understand?contact me.<br/>
author:hunterhug<br/>
2015/11


如果你觉得项目帮助到你,欢迎请我喝杯咖啡

微信
![微信](https://raw.githubusercontent.com/hunterhug/hunterhug.github.io/master/static/jpg/wei.png)

支付宝
![支付宝](https://raw.githubusercontent.com/hunterhug/hunterhug.github.io/master/static/jpg/ali.png)


--------------------------------------------------------------

# 补充
1.2016/7/7改bug

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

参考JSON可以加更多字段，请自行增加修改
