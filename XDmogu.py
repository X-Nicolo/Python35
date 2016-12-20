#python3.5 从西电小蘑菇爬取课表
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
# import cStringIO,Image,re  
 
# def ungzip(data):
#     try:        # 尝试解压
#         print('正在解压.....')
#         data = gzip.decompress(data)
#         print('解压完毕!')
#     except:
#         print('未经压缩, 无需解压')
#     return data
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
 
header = {


           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
           'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

           # "Host": "ids.xidian.edu.cn",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding": "gzip, deflate",
           "Referer": "http://115.159.48.227:8080/XDxiaoMogu/queryMasterTimeTable.htm?winzoom=1",
           "Content-Type": "application/x-www-form-urlencoded"
}
 
url  = 'http://115.159.48.227:8080/XDxiaoMogu/queryMasterTimeTable.htm?winzoom=1'
url2 ='http://115.159.48.227:8080/XDxiaoMogu/masterTimetableResult'
opener = getOpener(header)
op = opener.open(url)
data = op.read()


username = '1601120338'
password = '113411'

postDict = {
      
        'username': username, 
        'password': password,
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url2, postData)
data = op.read()
# data = ungzip(data)
 
print(data.decode())