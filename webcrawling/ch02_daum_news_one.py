import requests
from bs4 import BeautifulSoup

# 1. URL 설정
# 2. → 수집하고 싶은 웹 사이트 주소
url="https://v.daum.net/v/20241028144248100"

# 2. URL 전체 소스코드 가져오기
result=requests.get(url)
# 200 : 성공
# 400~600 : 오류
#print(result)
#print(result.text)

# 3. BS에게 전체 소스코드 전달 및 파싱
# → BS가 수집할 수 있도록 소스코드를 변환
doc=BeautifulSoup(result.text, "html.parser")

# → HTML 태그로 구성됨
# <div>
# 안녕하세요
# <div>안녕</div>
# </div>
# <a>Hi</a>


# 4. 수집
# → 선택자
#   1. 태그 선택자(사용 금지)X
#   2. 아이디 선택자(#) → 1개(유니크)
#   3. 클래스 선택자(.) → 복수개 선택 가능
#   4. 자식 선택자() → 해당 태그의 하위 자식들 선택
#   5. 자손 선택자 → 해당 태그의 자손들(자식+하위)
# select() → LIST타입
title=doc.select("h3.tit_view")[0].get_text()
print(f"뉴스제목 : {title}")

# 본문 : 여러개의 p태그로 구성
contents=doc.select("section > p")
content=""
for text in contents:
    content += (text.get_text())
print(f"뉴스본문 : {content}")

#기자 : 

writer=doc.select("span.txt_info")[0].get_text()
print(f"기자 : {writer}")

#날짜 : 
reg_date=doc.select("span.num_date")[0].get_text()
#방법1 split구분자
#split_list=reg_date.split(". ") #['2024', '10', '28', '14:42']
#reg_date=split_list[0]+split_list[1]+split_list[2]
print(reg_date) #20241028

#방법2 strip():좌우여백제거
split_list=reg_date.split(".") # ['2024', ' 10', ' 28', ' 14:42']
#reg_date=split_list[0].strip()+split_list[1].strip()+split_list[2].strip()

# lamda식 : map(), reduce(), filter()
# → map() : 리스트의 모든 값에 내가 원하는 함수르 적용
# → reduce(): 덧셈, 곱셈 등오르 값을 줄임
# → filter() : 조건에 맞는 값만 추출
split_date=list(map(lambda x : x.strip(), split_list))
reg_date=split_date[0]+split_date[1]+split_date[2]
print(reg_date)
# contents → [<p>본1</p>, <p>본2</p>, <p>본3</p>]
# text → <p>본1</p>
# test.get_text() → 본1
# content += text → "본1 + 본2 +본3"
