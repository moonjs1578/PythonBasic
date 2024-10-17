#주차타워(엘리베이터)
# - 1~5(1층당 1대만 주차)
# - 차량번호 : 정수숫자 4자리만 입력

# 기능
# 1. 차량입고
# 2. 차량출고
# 3. 차량조회
# 4. 프로그램 종료

# 1. 공통 설정
max_car =5 # 최대 주차 5대
cnt_car=0 # 현재 주차 대수(count)
tower=[]

# 2. 주차 타워 생성 → List
# tower=["", "", "", "", ""] # 방법1 : 하드코딩(절대 지양)
# 방법2: for문 활용
#for i in range(max_car):
#    tower.apped("")
    
# 방법3: List Comprehension 활용
tower=[""for i in range(max_car)]

# 방법2와 방법3은 동일한 기능의 코드
# 방법3을 사용하면 좀 더 효율적으로 코드 개발 가능
# 모든 for문을 "List Comprehension"으로 변경 불가
# (심플한 for문만 가능)


# 3. 주차타워 메뉴 출력
while True:
    print("="*50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("="*50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    print("="*50)
    
    #사용자에게 1~4까지 입력받는 코드 작성(유효성쳌)
    # - 올바른 값이 들어오지 않으면 경고메
    while True:
        select_num=int(input(""))
        if(select_num==1):
            break
        elif(select_num==2):
            break
        elif(select_num==3):
            break
        elif(select_num==4):
            break
        else:
            print(">> MSG : 올바른 번호를 입력하세요.")
            
        if(select_num==1):
            # 도메인 지식 → 비지니스 로직
            
            # 1. 주차타워 만차 여부 확인
            if cnt_car<max_car:
            # 2. 주차번호(4자리) 입력
                car_num=input(">> 차량번호: ")
                for i, car in enumerate(tower):
                    if car=="":
            # 3. 주차타워 입고 → tower[]저장
                        tower[i]=car_num
            # 4. 현재 주차 차랑 최신화 → cnt_car + 1
                        cnt_car+=1
                        break
                tower.insert(index, car_num)
            else:
                print(">> MSG : 만차입니다. 다음에 이용해주세요.")
            #  - 만차y : 죄송합니다.
            #  - 만차n : 다음 단계 이동
        elif (select_num==2):
            # 1. 차량번호 입력(출고)
            # 2. 주차타워에 주차되어 있는 여부 확인
            #   y : 다음단계
            #   n : "주차되지 않은 차량입니다."
            # 3. 차량 출고 → tower → ""변경
            # 4. 현재 차량수 -1
            #
        elif(select_num==3):
            print("■"*20)
            for i in range(len(tower)):
                print(f"■{i+1}층 : {tower[i]}")
                print("■"*20)
        elif(select_num==4):
            print(">> MSG : 프로그램을 종료합니다.")
            exit()
            