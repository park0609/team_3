import requests as req
from bs4 import BeautifulSoup as bs
url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
web = req.get(url, headers = headers)
soup = bs(web.content, 'html.parser')

title = soup.select('a.tltle')[:20]
name = soup.select('td.number')[:20]
str = ''
for i, (t, n) in enumerate(zip(title, name),1):
    str += f'{i}위: {t.text.strip()} / {n.text}\n' 
print(str,end=' ')




=====================================================================

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stock_names = []
current_prices = []

table_rows = soup.select('.type_2 tbody tr')
for row in table_rows[:20]:
    stock_name_tag = row.select_one('td:nth-child(2) a')
    current_price_tag = row.select_one('td.number:nth-child(3)')
    
    if stock_name_tag and current_price_tag:
        stock_name = stock_name_tag.text.strip()
        current_price = current_price_tag.text.strip().replace(',', '')
        stock_names.append(stock_name)
        current_prices.append(current_price)

for name, price in zip(stock_names, current_prices):
    print(f"{name}: {price}")


