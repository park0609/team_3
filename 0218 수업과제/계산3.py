import datetime
day1 = datetime.date(2025,2,18)
day2 = datetime.date(2025,5,8)
diff = day2 - day1 
days=['월','화','수','목','금','토','일']
day = datetime.date(2025,5,8)

print("어버이날까지 남은 날은", diff.days,"일 이고,",days[day.weekday()]+'요일 입니다.')