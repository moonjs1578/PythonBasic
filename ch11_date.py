from datetime import datetime, timedelta
import time
#날짜 포맷팅
now_date=datetime.now().strftime("%Y.%m.%d. %H:%M")
#now_date=datetime.now()
print(now_date) #현재날짜 및 시간 출력

#날짜 계산
# ex) 현재 시간에서 13시간 빼기
now = datetime.now()
before_time = (now-timedelta(hours=13)).strptime("%Y%m%d %H:%M")
print(before_time)

#
start_time = time.time()
# > 실행코드
end_time=time.time()
execution_time=end_time-start_time
print(f"실행시간 : {execution_time}초")
