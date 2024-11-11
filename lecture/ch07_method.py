'''
기본 함수 문법
def  함수명 (parameter1,parameter2)


함수 사용법

1.함수 정의
def sum_two_value(x,y): #매개변수
    sum =x+y
    return sum  # 반환값
    
    
2. 함수 호출 
tota=sym_two_value(5,10)
print(total)


 def print_value(a,b)
    sum=x,y
    


3.인자(입력 매개 변수)
-함수에 전달되는 입력값
-함수 정의문과 호출문의 parameter 갯수가 동일해야함
-parameter값 2개 이상 사용시 정의된 순서대로 전달해야함



4.default parameter
-함수 호출시 parmeter 전달 받지 못한경우 기본값 사용
-다수의 인자중 끝에서부터 사용가능
#def test(a,b,c=5):         #(0)
#def test(a,b=2,c=5):       #(0)
#def test(a=1,b=2,c=5):     #(0)
#def test(a=1,b,c):         #(x)
#def test(a,b=2,c):         #(x)
#def test(a=1,b=1,c):       #(x)
------ 결국 즉 뒤에서 부터 체워져야됨



5.return 
-기본적으로 함수 종료의미
-return 반환값: 함수 호출문으로 값 전달(turtle type)
-return 만 사용하면 함수호출문으로  none 값 전달
- return이  없는 경우 들여쓰기가 종료되면 함수 종료로 간주
- return 문 다음에 오는 코드는 실행 안됨(error)


6.변수의 범위
-변수가 참조 가능한 코드상의 범위를 명시
-함수내의 변수는 자신이 속한 코드 블럭이 종료되면 소멸
-이렇게 특정 코드블록 내에서 선언된 변수를 지역변수
-반대로 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 전역 변수
-같은 이름의 지역변수와 전역변수 존재하는 경우
 가까운 (지역변수 )순서로 운선순위가 높음

num=10 #전역 변수
num1=20
def test(mum.num1):
    num1=30 #지역변수
    return num+num1
test(num,num1)

#함수 내에서 전역변수 값을 변경


num=10 #전역 변수
num1=20
def test(mum.num1):
    num1=30 #지역변수
    return num+num1
num1=test(num,num1)



#[global 은절때 쓰지 마쇼]
num=10 #전역 변수
num1=20
def test():
    global num1 #지역변수를 전역변수로[golbal전역변수 지칭 키우드 전대 사용하지 마쇼]
    num1=30
test()

#가변길이 인자(vaiable length parameter)
#-*args(): tupel type
#**kwargs():dict type

def test(*args)
    for item in args:
        print(item)
test(10,20,30)
test(1,2,3,4,5)


def test(**kwargs)
    for key,value in kwnargs.items():
        pirnt(key,value)

test(a=1,b=2,c=3)

#9.type hint
- 입력 매게 변수와 반화갑의 타입을 힌트로 미리 적어두기

 der sum(a:int,b:int)   int
    return a=b













'''