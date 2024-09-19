# 문자열의 이해(String)
#   - 활용 예 : 데이터 분석, 자연어 처리 응용
#               사용자로부터 값 입력받고 처리(유효성 체크)

# 1. 문자열 인덱스(index)
#   - 문자열은 각 문자마다 순서(인덱스) 있음
#   - 인덱스 시작은 0
#   - 인덱스는 공백 포함
intro = "Hello Python" # 문자열길이(12), 인덱스(0~11), 역인덱스(-12 ~ -1)

# 2. 문자 추출
# - 인덱스 범위 벗어난 경우(Error : index out of range)
print(intro[0]) #H
print(intro[-2]) #o

# 3. 문자열 슬라이싱(문자열 추출) 
# - 슬라이싱 시험문제
#   -[시작:끝] 끝-1
#   -[0:11] → 0~10
print(intro[:]) # 처음부터 끝까지
print(intro[:6]) #처음부터 5까지 → 0 ~ 5
print(intro[3:]) #3부터 끝까지(-1)

date ="20240919 12:27"
date[0:4]

# 4. 문자열 함수
# -len() : 문자열 길이 계산
print(len(intro)) # 12

# -upper() and lower() : 대소문자 변경
print(intro.upper())
print(intro.lower())

# - replace() : 특정 문자 치환
print(intro.replace("H", "J"))

# - split() : 구분자를기준으로 문자열 분할(기본값 : 공백)
print(intro.split())
print(intro.split("o"))

# - strip() : 문자열의 좌우공백 제거
# - "       ccw     " → "ccw"
print(intro.strip())

# - in() : 특정 문자열 포함하는지 확인(True or False 출력)
print("python" in intro) # 대소문자 구별(정확히)

# - find() and rfind() : 문자열 내부 특정 문자 인덱스 출력
print(intro.find("H"))
print(intro.find("Python"))







