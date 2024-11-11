#조건문(condition):if~elif~else
#  특정 조건을 만족하는 경우 수행할 작업에 사용
# 모든 조건은 blooen으로 표현



'''
if 조건1: [처음]
    code [: 들여쓰기가 하나의 관계로 있기에 무조건 들여쓰기 해야됨]
elif 조건2:
    code
elif 조건3
    code
else :  [끝, 위에거 다 안되면 마지못해 이거]
    code
'''


# if문 조합식
# 1.if 
# 2.if~else
# 3.if~elif
# 4.if~elif~else


# 논리 연산자:AND,OR,NOT
'''
 AND:두조선 모두 참인 경우만 참 나머지 거짓
 OR:하나라도 참이면 참
 NOT :참이면 거짓,거짓이면 참
 '''
 
 
#  예제:태어나 년도를 입력하면 [성인,대학생,고등학생.중학생.초등학생 ,어린이 출력하는 코드작성]


#input()-키보드 값을 전달 받음
# input 은 싹다 문자혀응로 들어옴

born =input('태어난 년도:') #사용자의 출생년도 입력
if now <born:
    print('출생년도를 잘못입력하셨습니다')
    #다시 출생년도를 입력받게 함!
'''
from datetime import datetime
now=datetime.today().year #현재 날짜 정보

#print(type(now))
#print(type(born))

# 나이 계산
age = now-int(born)
print(age)
'''

#27~:성인
#20~26 :대학생
#17~19 :고등학생
#14~16 :중
#8~13:초
#7~ :어린이


#조건에 따라서 cotegory ='성인'

if age>= 27: #위에서부터 이 범위가 아닌것을 타고 내려가면서 하기에 아래있을때랑 범위가 겹치지 않는다
    category ='성인'
elif age >=20:
    category='대학생'
elif age >= 17:
     category='고등학생'
elif age>=0:
    category='어린이와 기타'
else:
    print('잘못된계산입니다')
    