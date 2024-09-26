# 반복문
# 1. for → 반복 횟수를 아는 경우
# 2. while  → 반복 횟수를 모르는 경우

 #켈렉션의 길이만큼 반복
for num in [1, 2, 3]:
    print(num)

#range(시작: 끝: 스텝)
#range(1: 5: 2) → 1, 3
#range(1:5) →1, 2, 3, 4(스텝 생략가능 :1)
#range(7) → 0, 1, 2, 3, 5, 6(시작 : 0)

# 1~10까지 출력 
for num in range(1, 11):
    print(num)

#반복 횟수 인덱스를 사용하고 싶은 경우
a=["A", "B", "C"]
for i, val in enumerate(a):
    print(i, val)
# 구구단 2단
# 2X1=2
# 2X2=4
# ...
# 2x9=18
for i in range(1, 10):
    print(f"2x{i}={2*i}")
    
# 숙제
# 1. 중첩 for문 사용해서 구구단 2단부터 9단까지 출력하는 코드 작성
# 2. 2단~9단 : 반복1
# 3. 단(1~9 곱셉) : 반복2
#for i in 범위:
#    for j in 범위:
#        for k in 범위:
            
