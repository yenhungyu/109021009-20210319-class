import requests
from bs4 import BeautifulSoup

req=requests.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
req.encoding = "big5"
if req.status_code == 200:
    soup = BeautifulSoup(req.text,"lxml")
    result1 = soup.find_all(["ul","ol"])
    fp = open("out3.txt","w",encoding="utf8")
    for val in result1:
        text2 = val.text.replace("\n","")
        text3 = text2.replace("","")
        print(text3)
        fp.write(text3+"\n")
    fp.close()
    print(result1)
else:
    print("no page")
