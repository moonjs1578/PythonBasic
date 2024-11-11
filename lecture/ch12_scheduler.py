# 스케줄러(scheduler)
# 일정시간에 반복적으로 동작해야하는 작업
# ex) 12시간에 한번씩
    #   5분에 한번씩
# 
# python은 유명한 스케줄러 라이브러리2개 
# 1.scheduler
#  -매우 쉽고,매우 기능이 약해
# 2.apscheduler
# -메우쉽고,기능이 강해



#**apscheduler
#1.blockinfScheduler ->내가 메인이야,나만 동장할거야 #ex) 화면 가득 표시
# 2.BackgroundScheduler->난 서브야,뒤에서 동작하고 있을게 #ex) 핸드폰 기상 알람처럼 보이지는 않지만 작동은 하고있는


#APS ,scheduler사용법
# 1.스케줄러 생성
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.blocking import BackgroundScheduler

sched=BackgroundScheduler()

# %백그라운드 스케줄러는 반드시 메인 프로그램이 동작 중이러야만 동작함!
#2.job 생성(함수)
def print_hello():
    print('Hello')
          
          
          
#3.스케줄러에 job 등록
sched.add_job(print_hello,'cron',hour='12',minute='30',id='chosun')

#4.스케줄러 실행
sched.start()


while True:
    time.sleep(1)



