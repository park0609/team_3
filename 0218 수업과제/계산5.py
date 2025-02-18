def chuseck():
    import datetime
    days = ["월","화","수","목","금","토","일"]
    day1 = datetime.date(2025,7,25)
    day2 = datetime.date(2025,10,6)
    diff = day2 - day1
    print(f"수료 후 추석까지 {diff.days}일 남았고, 그 날은 {days[day2.weekday()]}요일 입니다!")