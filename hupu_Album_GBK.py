#!/usr/bin/env python
#coding: GBK
#author: xavierskip
#version: 0.13
#date: 10-13-2012

import os,sys,urllib2,re

def get_pages(home,homepage):
	match = re.match(r'http://my\.hupu\.com([\S]+?)(?:\-[\d]\.html|\.html)',home) 
	if match == None:
		print 'some thing wrong!\n说好了不要拿乱七八糟的url来调戏我的！'
		exit()
	path = match.group(1)    #Album path
	pat  = path+ r'-([\d]+).html(?:\'|\")>'
	P_nums = re.findall(pat,homepage)
	if P_nums==[]:
		page_list = [home]
		return page_list
	else:
		P_max = int(P_nums[-1])
		#生成所有相册页面，还好都是有规律的。汗|||
		page_list = [r'http://my.hupu.com%s-%d.html' %(path,i) for i in xrange(1,P_max+1)]
		return page_list

def get_content(url):
	content = urllib2.urlopen(url).read()
	return content

def get_urls(content):
	pat = r'http://i[\d]{1}\.hoopchina\.com\.cn/.+small\.(?:jpg|gif|png|jpeg)'
	url_list = re.findall(pat,content)    #parse img url
	print '得到%d张图片URL' %len(url_list)
	urls = '\n'.join(url_list)
	urls = re.sub(r'small\.',r'big.',urls)
	return urls

def dowm_img(urls):
	pass

def main():
	#脚本可带url参数
	if len(sys.argv)<=1:
		home = r'http://my.hupu.com/jackson817/photo/a82914-1.html'    #脚本内置虎扑相册地址
	else:
		home = sys.argv[1]
	homepage = urllib2.urlopen(home).read()    #字符编码真烦人
	title    = re.search(r'<title>(.+)</title>',homepage).group(1)
	print '正在抓取相册>>>%s>>>' %title
	page_list = get_pages(home,homepage)    #得到相册的所有页面
	P_num =  len(page_list)
	print '此相册有%d页！' %P_num
	content = ''
	current = 0
	for i in page_list:
		current +=1
		content +=get_content(i)     #得到所有页面内容
		print '%d/%d:page done:%s' %(current,P_num,i)
	urls = get_urls(content)
	os.system(r'mkdir "%s" ' %title)
	print '创建"%s"文件夹成功' %title
	url_file = open(r'%s/urls' %title,'w')    #追加:w+
	try:
		url_file.write(urls)
		print '图片url写入文件成功'
	finally:
		url_file.close()
	print '\n','='*10,'开始下载','='*10,'\n'
	end = os.system(r'wget -N -i "%s/urls" -P "%s" ' %(title,title) )
	if end == 1:
	    print '缺少wget！可以打开"%s"文件夹下的urls文件，复制其内容用其他下载工具下载，例如迅雷等~' %title
	else:
	    print 'success!'
		
if __name__ == '__main__':
    main()
