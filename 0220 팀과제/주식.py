import requests as req
from bs4 import BeautifulSoup as bs

def finance():
    url="https://finance.naver.com/sise/sise_market_sum.naver"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    web = req.get(url,headers = headers)
    soup = bs(web.content, 'html.parser')
    
    title = soup.select('.tltle')
    marketprice = soup.select('td.number:nth-child(3)')
    
    for i,(t,m) in enumerate(zip(title, marketprice),1):
        print(f'{i}:', t.text.strip()+" : ",  m.text.strip()+"원")