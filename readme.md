虎扑相册下载脚本
===

本脚会抓取虎扑某个相册的所有图片链接，并在脚本所在的文件夹中创建与下载相册同名的文件夹，抓取的所有图片url会写入这个文件夹中的urls文件中，然后通过wget（`wget -i urls`）批量下载下来。  
（为了功能的快速实现，下载的功能就交给wget处理了）

使用方法： 
--- 
把你要下载的某个虎扑相册的url作为脚本的参数运行即可。 
(注意：是个人主页中单个相册url)  
like this:  
`>>> python hupu_Album.py  http://my.hupu.com/jzgk/photo/a75782-1.html `   （也可直接修改脚本内的url为要下载的相册url，直接运行）

运行环境：
---
需要 python环境 。(linux 发行版都会带吧，mac下没有测试过)  
下载模块需要 wget  
（也可以打开urls文件，复制粘贴内容，用迅雷或者其他下载软件下载）  

version:0.1
---
* 批量下载一个虎扑相册的所有图片。

issues:
---
* 抓取时每页的封面图没有去除，总共有几页图就会多出几张图 
* 正则只匹配出jpg|gif|png|jpeg格式的图片，还有其他的格式么？

todo:
---
* 去除重复的图片url
* 下载功能的python实现
* gui或者更多～

 
欢迎提交BUG！