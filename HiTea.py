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
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
           'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           # "Host": "ids.xidian.edu.cn",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding": "gzip, deflate",
           "Referer": "http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp",
           # 'X-Requested-With': "XMLHttpRequest",
           "Content-Type": "application/x-www-form-urlencoded"
}
 
url = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fyjsxt.xidian.edu.cn%2Flogin.jsp'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
# data = ungzip(data)     # 解压
It = 'LT-31860-Nr4DeRHVPUcMaNqcVrB5XxzLecI0ev1481623540759-wHmD-cas'
 
url = 'http://jwxt.xidian.edu.cn/caslogin.jsp'

id = '1601120338'
password = '113411'

postDict = {
        'It':It,
        'username': id, 
        'password': password,
        "submit": "",
        "execution": 'e1s1',
        "_eventId": "submit",
        "rmShown": '1'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
# data = ungzip(data)
 
print(data.decode())