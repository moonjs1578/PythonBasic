''''
from datetime import datetime,timedelta
# 날짜 포맷팅
# now_date=datetime.now() #출력:2024-10-10 12:06:19.114959
now_date=datetime.now().strftime('%Y.%m.%d.%H:%M') 
print(now_date)  #2024.10.10.12:09
before_time = (now-timedelta(hours=13)).str
print(before_time)

# 실행시간 계산하는 코드
star_time=time.time()
#--실행코드
end_time = time.time()
except
....
'''