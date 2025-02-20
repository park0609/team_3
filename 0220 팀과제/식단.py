import requests as req
from bs4 import BeautifulSoup as bs
url = "https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"}
web = req.get(url, headers = headers)
soup = bs(web.content,"html5lib")
menu_card = soup.select(".menu-tbl")
dates = soup.select(".date") 
days = soup.select(".day") 
won = soup.select(".menu-tit01")
menu = soup.select(".menu-tit01+p")
for d, t, w, n in zip(dates, days, won,menu):
    print("="*20)
    print(d.text+" "+t.text+"\n"+"\n"+ w.text+"\n"+n.text)