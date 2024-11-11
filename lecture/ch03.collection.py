#변수:하나의 값을 저장할 수 있는 메모리 공간,즉 하나의 값만 넣을 수있다
num=3
num=4
# 그러면 3은 지워지고 4만 됨

# 배열:(동일한 자료형의)여러 값을 저장 할 수 있음
#  그러나 단점으로 고정된 크기 사용(메모리를 비효율적으로 사용)
#  예시 내가 배열 100칸 생성+2개의 값만 저장,99개가 빈다
#  그럼에도 불구하고 100칸을 dbwl

# 컬렉션 프레임 워크라는 것을 사용한다
#  list,dictionary,set,tuple
#  순서가 있는 자료형(인덱스):list,tuple 예시:기차
#  순서가 없는 자료형:dict,set 예시:가방마댱 다 넣기

# 리스트(list)
#  시퀀스 자료형(연속 된 값 저장)
#  index 사용(스라이싱 가능) [],[:]
#  정렬가능
#  mutable(최초 생성된후 변경 가능),만들고 변경가능
#  packing과 upacking 가능
#  멤버함수:appednd extend insert/ remove pop index sorted 
#  2차원 리스트는 표 형태와 동일


list_a=[]
list_b=[1,2,3]
list_c=[1,0.1,'chosun',True] 

list_d= ['A','B','C'] #packing
a,b,c=list_d #unpacking
#a,b,c=['A','B','C']
a=[1,2,3]
a.append(4)

# 가 .append():맨 마지막에 값을 추가
# 나 .insert():원하는 인덱스에 값을 추가 하고 자기가 들어가서 뒤로 밀어버림
a.insert(1,9)
print(a)

# 다. extend():리스트와 리스트를 병합 합체!!
b=[1,2,3]
c=[3,4,5]
b.extend(c)
print(b)

# 라.remove():실제 값으로 삭제
d=[1,2,3,]
d.remove(2)
print(d)

# 마.pop():인덱스로 삭제
val=d.pop(0)
print(d)
print(val) 
# 바.index():원하는 값의 인덱스를 출력
e=['a','b','c']
print(e.index('a'))

# 사.sorted():정렬
# sort():정렬--원본 데이터를 건드리기에 절대 쓰지 마쇼
# sorted():복제한 후 값을 정렬(원본 값 유지)
# 정렬(기본:오름차순(ASC)),내림차순(DESC)
f=[99,50,30,10,40]
print(sorted(f)) #기본:오름차순(ASC)  
print(sorted(f,reverse=True)) #내림차순(desc)...... 게시판은 최근 순이니가 내림차순으로 정리


# 2.튜플(tuple)
#  시퀀즈 자료형
#  index 사용(슬라이싱 가능)
#  packing,updacking 가능
#  (),() 생략가능
#  immuatable(생성된후 수정불가)
#  멤버함수x, 정렬 불가
#  함수 return값으로 활용.... 값이 안변하게

a=(1,2,3) #튜플
b=1,2,3 #튜플   추가가 안되고 값변경이 안되기에 새로 만들어야됨, 값이 유동적이여야 되면 리스트,변화해야되면 튜플
c=(5)# 튜플
d=5 # int형(튜플x)
e=5, #튜블...튜블이라는것을 알리기 위해 ',' 같이 붙임 혼자 사용할때는


#딕트(dictionaty)
# {} 중괄호 사용
# 인덱스 없음(순서 없음)
# {key:value}- key value pair,,,, value값에  key를 대응시켜서 찾아낸다 
#value(실제값)- key 값으로 특정!
# value(중복 가능),key(중복 불가)-->유니크 해야한다(중복이 되면 안된다)
# value는 key로만 접근이 가능하다!
# JSON[제이슨] :값을 전달할때 포맷 기준!(왔다갔다 전달할때 사용하는것) == DICT 와 동일한것 파이썬에서 이렇게 부를뿐


intro={
    '이름':'김영안',
    '나이':'22',
    '전공':'인공지능'
}
print(intro['이름']) #key 값으로 찾는다
intro['성별'] ='남자' 
intro['전공']= '소프트웨어'
print(intro)

#update():두 딕셔너리 병합
a={'a':1,'b':2}
b={'b':5,'c':3,'d':4}
a.update(b)
print(a)
 
pop()
a.pop('b')
print(a)
 
 
 #in()
 #-key 값이 존재하는지 확인
print(2 in a) #true or false
# key 값이 존재하는지 확인
print(2 in a)
#value access(값 접근)

print(intro['이름'])
print(intro.get('이름'))

print(intro.keys())
print(intro.values())
print(intro.items())

#4.세트(set)
#수학의 집합과 동일한 개념
#{} 사용
# 인덱스 없음
# 중복값 허용 안함
# 중복값 제거시 많이 사용
a={1,2,3,4,5,} 
print(a)
list_f=[1,2,2,2,2,3]
print(list_f)
print(list(set(list_f))) # 중복값을 제거하고 다시 리스트로 바꾸기
print={} #dict 
print(type(a))


#숙제 :변수와 b변수의 값을 교환

a=10
b=20

# 코드 작성
print(a) #20
print(b) #10 

a,b=b,a #튜플 형식


