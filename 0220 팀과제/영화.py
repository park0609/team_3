import requests
import json

url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=86c5204088a51e4d9a9e26141ed5b4e5&targetDt=20250216"
res = requests.get(url)
text = res.text

d = json.loads(text)

for b in d['boxOfficeResult']['dailyBoxOfficeList']:
    print(b['rank'],b['movieNm'],b['audiCnt'])