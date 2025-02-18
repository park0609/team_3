def birth():
    import datetime
    days = ["월","화","수","목","금","토","일"]
    month = input("생일의 월을 입력해주세요!")
    day = input("생일의 일을 입력해주세요!")
    day1 = datetime.date(2025,2,18)
    day2 = datetime.date(2025,int(month),int(day))
    diff = day2 - day1
    print(f"생일까지 {diff.days}일 남았고, 그 날은 {days[day2.weekday()]}요일 입니다!")
