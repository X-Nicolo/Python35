#! /usr/bin/env python3
import urllib.parse
import urllib.request

id = '1601120338'
password = '113411'
lt_value = 'LT-31860-Nr4DeRHVPUcMaNqcVrB5XxzLecI0ev1481623540759-wHmD-cas'
exe_value = 'e1s1'

url = 'http://jwxt.xidian.edu.cn/caslogin.jsp'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
values = {
'username': id, 'password': password,
          "submit": "", "lt": lt_value, "execution": exe_value,
          "_eventId": "submit", "rmShown": '1'
}
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))