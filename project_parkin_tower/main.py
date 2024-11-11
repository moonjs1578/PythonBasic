#주차타워(엘리베이터)
#1~5층(1층당 1대)
#차량번호:정수 숫자 4자리만 입력

#기능
#1.차량입고
#2.차량출고
#3.차량 조회
#4.프로그램 종료

#1.공통 설정
max_car=5 #최대 주차 5대
cnt_car=0 #현재 주차 대수(count)

#2.주차 타워 생성->list
#tower=['','','','',''] #방법 1:하드코딩(쓰지 마렴)
#방법2:for문 활용
#tower=[]
#for i in range(max_car):
   # tower.append('')
    
#방법3:List Comprehenshion 활용(방법 2를 압축해서 하는것)
tower=[''for i in range(max_car)]
#방법2와 방법3은 동일한 기능의 코드
#방법3을 사용하면 좀더 효율적으로 코드 개발 가능
#모든 for문을 'list comprehension'으로 변경 불가
#(시플한 for문만 가능)

#3.주차타워 메뉴 출력
while True:
    print('='*50)
    print('==주차 타워 시스템 ver1.1==')
    print('='*50)
    print('1.입고')
    print('2.출고')
    print('3.조회')
    print('4.종료')
    print('='*50)
    
    #사용자에게 1~4번까지 값을 입력 받는 코드 작성(+유효성 체크)
    # 올바른 값이 들어오지 않으면 경고 메시지 출력후 다시 입력
    #사용자에게 입력 받는 변수는 select_num에 담기

    while True:
        select_num=int(input('>>번호:'))
        if 4>=select_num>=1:
            break
        else:
            print('>>MSG:올바른 번호를 입력하세요.')
            
    if select_num==1: #입고
        #도메인 지식.->비즈니스 로직
        
        #1.주차타워 만차 여부 확인
        if cnt_cat<max_car:
        #2.주차번호(4자리)입력
        car_num=input('>>차량번호:')
        for i,car in enumerate(tower):
            if car=='':
                tower[i]=car_num
                cnt_car+=1
                break
            
            
        tower.insert(index,car_num)
        
        #4.현재 주차 차량 최신화->cnt_car+1
        else:
            print('>>MSG:만차입니다.다음에 이용해주세요.')
        #-만차y:죄송합니다
        #-만차n:다음단계 이동
        
    elif select_num==2: #출고
        #1.차량번로 입력(출고)
        #2.주차타워에 주차되어 있는 여부 확인
        # y:다음 단계
        # n:'주차되지 않은 차량입니다.'
        #3.차량 출고->tower에 있는 값을 '' 변경
        # 4.현재 차량수-1
        
    elif select_num==3: #조회
        print('■'*20)
        for i in range(len(tower))
        print(f'■{i+1}1층:{tower[i]}')
        
            print(f'■')
    elif select_num==4: #종료
        print(">>MSG:프로그램을 종료합니다.")
        exit()
    
    
    
    
    
    
    


