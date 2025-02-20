import requests 
from bs4 import BeautifulSoup 
url = "https://www.melon.com/chart/index.htm"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")
    song_titles = soup.select("div.ellipsis.rank01 a")
    artists = soup.select("div.ellipsis.rank02 span.checkEllipsis")
    for idx, (title, artist) in enumerate(zip(song_titles,artists), start=1):
        print(f"{idx}위: {title.text.strip()} - {artist.text.strip()}")
else: 
    print(f"페이지를 불러오는 데 실패했습니다. 상태 코드: {response.status_code}")




