import datetime
day1 = datetime.date(2025,2,3)
day2 = datetime.date(2025,12,25)
print(day1,day2)
diff = day2 - datetime.datetime.now().date()
print("남은 기간:" , diff.days,"일")
days = ['월', '화', '수', '목', '금', '토', '일']
print("그날은 " + days[day2.weekday()] + "요일 입니다.")