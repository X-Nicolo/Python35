#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
url = 'http://jwxt.xidian.edu.cn/caslogin.jsp' #login网址

id = '1601120338'
password = '113411'
lt_value = 'LT-31860-Nr4DeRHVPUcMaNqcVrB5XxzLecI0ev1481623540759-wHmD-cas'
exe_value = 'e1s1'

datas = {'username': id, 'password': password,
          "submit": "", "lt": lt_value, "execution": exe_value,
          "_eventId": "submit", "rmShown": '1'
          }

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
           'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           # "Host": "ids.xidian.edu.cn",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept-Encoding": "gzip, deflate",
           "Referer": "http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp",
           # 'X-Requested-With': "XMLHttpRequest",
           "Content-Type": "application/x-www-form-urlencoded"
           }
sessions = requests.session()
response = sessions.post(url, headers=headers, data=datas)
print(response.status_code)