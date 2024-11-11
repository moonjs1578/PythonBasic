# 문자열의 이해


#문자열 인덱스(index)
#문자열릉 각 문자마다  순서(인덱스) 있음
#인덱스 시작은 0
#인덱스는 공백 포함

intro = "Hello Python"
#       "01234567891011"  :12개 //// 무자열 길이(12), 인덱스((0~11), 역인덱스(-12~-1)

# 2. 문자 추출
# 인덱스 범위 벗어난 경우(error:index out of range)
print(intro[0]) #H
print(intro[-2]) #o

#3. 문자열 슬라이싱(문장열 추출)
# -[시작:끝] , 이상 미만이기에 ,,, 예를 들어 [0:11]-> 0부터 10까지 
print(intro[:]) # 처음부터(0) 끝까지
print(intro[:6]) #처음부터 5까지
print(intro[3:]) #3번부터 끝까지
data='202140919 12:27'
data [0:4] #2021만 뽑히게 됨


#4.문자열 함수 
# -len():문자열 길이 계산
print(len(intro)) #12

#upper() and lower(): 대소문자 변경
print(intro.upper())
print(intro,lawer())

#replace():특정문자 치환
print(intro.replace("h","j"))


#split():구분자를 기준으로 문자열 분할(기본값:공백)
print(intro.split())
pirnt(intro.split(o))

#stript():문자열 좌우공백 제거
#'     dfdsf'--> 'dfdsf'

# in():특정 문자열 포함 하는지 확인(true or false 출력)
print('python' in intro) #대소문자 구별 명확히



#find() and rfind():문자열 내부의 특정 문자 인덱스 출력 
print (intro.find('H'))
print(intro.find('python')) #첫번째 글자의 인덱스
print(intro.find('o')) #좌측에서 찾기
print(intro,rfind)



# 문제 1.메일에서 추출기
# 힌트  이메일 받았을때 거기서 @뒤에 때고. 아아디 부분만 뽑아내기
# 맨처음은  [0:] 들어오는것이, @이의 인댁스   find (@) 함수를 쓰고 거기서 찾기 , find는 좌측에서 우측으로 이기에  rfind를 써서 찾기




# 문제2. 도메인 추출 
url='www.naver.com'
domain=url.split('.')[1]
print(domain)