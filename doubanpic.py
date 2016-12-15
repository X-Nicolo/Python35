#python3.4 爬虫教程  
#爬取网站上的图片  
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)  
#可用程序
import urllib.request    
import socket    
import re    
import sys    
import os    
targetDir = r"E:\PythonWorkPlace\load"  #文件保存路径  
def destFile(path):    
    if not os.path.isdir(targetDir):    
        os.mkdir(targetDir)    
    pos = path.rindex('/')    
    t = os.path.join(targetDir, path[pos+1:])    
    return t    
if __name__ == "__main__":  #程序运行入口  
    weburl = "https://www.douban.com/"  #豆瓣使用了https 
    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}   
    req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头  
    webpage = urllib.request.urlopen(req)  #发送请求报头  
    contentBytes = webpage.read()    
    for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):  #正则表达式查找所有的图片  
        print(link)  
        try:   
            urllib.request.urlretrieve(link, destFile(link)) #下载图片  
        except:  
            print('失败') #异常抛出  