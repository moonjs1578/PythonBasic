# 주석(comment):메모,실행x

print(test)  # 주석을 달아 주세요.
#1.출력함수
#소괄호 있으며 함수다/ 함수의 입력값을 전달/()값을 출력 


#pythondms "",''모두 문자열(string) 의미가 모두 동일하다
print("hello python") #그러나 습관은 쌍다음표로 

#참고:escape code(문자열과 함께 사용)
#-문법(\+@무언가)
# \n(한줄 개행)
# \n(탭,8칸 공백)

# 알트시프트 방향키는 복사
# 알트 방향키는 이동
# 클릭 알트 시프트 같은열 똑같은말
# 클릭 알트 다른열과 함께

print(hello\n python')
print(hello\n python')
print(hello\n python')
print('hello\n python')
print('hello\n python')

#2.자료형(type)
#-python의 모든 자료형은 객체(object)
#-정수형(int):3,4,5
# -실수형(float):3.12
# -문자열(string):"hi"
# -논리형(boolen):True,False

# if TRUE()

# 형변환 (type casting)
# int()안에 있는값을 정수
# float,str(무자열 모두 비슷)
a=3
b=3.14
c="5"
d="5.15"
print(float(a))
print(str(a))
print(str(b))
print(int(b))
print(int(c))
pirnt(int(d)) # error 발생, #str(실수)-> 정수 에러 발생


#non type
# -사용금지!, 그냥 평생 쓰지 말아라 시스템이 다운이 된다, 만약 써야한다면 "" 요걸로 대체하여 사용하라
# -null ==none
# nullpointer exception(크리티컬 오류->프로그램 종료)
#변수 생성 및 초기화
# num=5[5라는 값을 num에 대입하세요]
#pythondms 변수 선언시 type을 지정하지 않음(동적 타이핑 언어)
# =(대인연산자), 우측의 값을 좌측에 대입하세요
# -초기화:초기 변수를 생성하면 변수를 생성한 메모리 공간에
#        쓰레기 파일들이 존재,변수에 값을 대입하면
#         쓰래기 파일들이 삭제(초기화 돼고값만 저장)
#명명규칙
# 변수,함수,클래스 등의 사용자 정의 이름에 사용!
# 명확하고 알아보기 쉽게(막 짓는게 아니다)
#1.영어 대소문자,숫자,특수문자는" _,-"만 사용, 이름지을때 공백없이 사용금지
#2.숫자로 시작할 수없음:123
#3.영어 대소문자 구별:ABC!=ABC
# 4.예약어(이미 파이썬에서 지정해놓은언어)
# 7.네이밍 메서드
# 변수,함수,클래스 등의 사용자 정의 이름에 사용하는 기법
# 프로그래밍 언어 별로 naming method가 다음
# 1) PascalCase (앞쪽에 한개씩)
# 2) camelCase(낙타혹처럼 가운데)
# 3)snake_case(뱀처럼 아래 하이프)
# 4) kebav-case(캐밥처럼 중간 작대기)
#           변수    함수    클래스 
# java      카멜 카멜 파스칼
# pyhton    스네이크 스네이크  파스칼
#9.상수 
#-변하지 않는 수
# 상수는 반드시 선언 및 초기화를 함꼐
# 상수는 반드시 선언 및 초기화(고정)을 함께
# 전부디 대문자를 사용
MAX_VALUE=30 #상수

#9.동적 출력
#print() -->출력(변수)
print("조선대학교 24학번 김영안 입니다" ) #하드코딩(지양)
print("조선대학교 {}번{}입니다".format(student_num,name) ) #format()- 오랜된 코드 방식 가독성이 떨어짐
print(f"조선대학교 {student_num}학번 {name}입니다" ) #f-string -최신 방식
print("조선대학교 24학번 김영안 입니다" ) #하드코딩(지양)


# 10.간단하 사칙연산 
# -5/2 -> 2.5
# -5//2->몫(2)
# -5%2->나머지(1)

#  QUIZE
#num=9
#num=num-1
