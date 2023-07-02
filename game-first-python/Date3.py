import datetime

today=datetime.datetime.now()

if today.weekday() in [5,6]: #Saturday & Sunday
    print("주말이므로 학교에 가지 않습니다!")
    print("온종일 코딩하며 지낼 수 있어요!")
elif today.weekday()==4:
    print("금요일이므로 내일이면 코딩하며 시간을 보낼수 있어요!")
else:
    print("오늘은 학교 가는 날입니다")