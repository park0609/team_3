import requests as req
from bs4 import BeautifulSoup as bs
url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"}
web = req.get(url, headers = headers)
soup = bs(web.content,"html.parser")
number = soup.select("td:nth-child(3)")[5:]
tltle = soup.select(".tltle")
no = soup.select(".no")[:20]
for a, b, c in zip(no,tltle,number):
    print(a.text+" "+b.text+" "+c.text)