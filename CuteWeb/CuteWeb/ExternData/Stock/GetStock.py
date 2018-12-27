# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 14:05
# @Author  : ZouJunLin
"""
-----获取所有股票信息------
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

r=requests.get("http://quote.eastmoney.com/stocklist.html",timeout=300)
r.encoding=r.apparent_encoding
print r.status_code
content=r.text
soup=BeautifulSoup(content,"html.parser")
soup.declared_html_encoding="utf-8"
quote_div=soup.find("div",class_="quotebody")
quote_a=quote_div.findAll("a",target=True)
quote={}
typecontent={}
file=open("quote.txt","wb")
templist=[]
for i in quote_a:
    name=i.get_text().strip().encode("utf-8")
    href=i['href'].strip().encode("utf-8")
    temphref=re.findall(r"[s][hz]\d{6}",str(href))[0]
    if str(temphref).strip().startswith('sz'):
        typecontent[name]='sz'
    elif  str(temphref).strip().startswith('sh'):
        typecontent[name]='sh'
    # href="https://gupiao.baidu.com/stock/"+href[0]+".html"
    quote[name]=href
for key in quote:
    Type=typecontent[key]
    quote_name=key[0:key.index('(')]
    quote_num=key[key.index('(')+1:key.index(')')]
    # print  quote_name+"\t"+quote_num+"\t"+quote[key]+"\t"+Type+"\n"
    templist.append(tuple([quote_name,quote_num,quote[key],Type]))
    # file.write(quote_name+"\t"+quote_num+"\t"+quote[key]+"\t"+Type+"\n")
for i in templist:
    print i[0],i[1],i[2],i[3]