import datetime
def child():
    cd = datetime.date(2025,5,5)
    today = datetime.datetime.now().date()
    diff = cd - today
    days = ['월','화','수','목','금','토','일']
    return f"오늘부터 어린이날까지는 {diff.days}일 남았으며, 어린이날은 {days[cd.weekday()]}요일 입니다."
child()