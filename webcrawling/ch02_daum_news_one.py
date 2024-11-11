import requests
from bs4 import BeautifulSoup

#1. url  설정
#-> 수집하고 싶은 웹 사이트 주소
url="https://v.daum.net/v/20241028144248100"

#2.URL 전체 소스 코드 가져오기

result=requests.get(url)
'''
print(result)
print(result.text)
'''
# 3.bs에게 전체 소스코드 전달 및 파싱
#-->bs가 수집할 수 있도록 소스 코드를 변환
doc=BeautifulSoup(result.text,'html.parser')

#%#html 태그로 구성 됨
#<div>
# 안녕하세요
# <div>안녕</div>
# </div>
#<a>hi</a>



#4.수집
#->선택자 
# 1.태그 선택자(사용금지 , 존나큰 주차장에서 검은색차 찾아줘랑 비슷함, 쓸게 못됨)
# 2.아이디 선택자-->1개(유니크)
# 3.클래스 선택자-->복수개 선택 가능
# 4.자식 선택자-->해당 태그의 하위 자식들 선택
# 4.자손 선택자--> 해당 태그의 자손들(자식+하위)
#select() -list 타입

title= doc.select("h3.tit_view")[0].get_text() #문자섞여있는것중에 get text 를써서 텍스트만 가져감
print(f'제목:{title}')

contents=doc.select('section > p')
content=''
for text in contents:
    content += text.get_text()
print(f'뉴스본문:{content}')


#content->[<p>본1</p>,<p>본2</p>,<p>본3</p>]
#text-><p>본1</p>
#text.get_text()0->본1
#content +=text->'본1'



#기자:
writer=doc.select('span.txt_info')[0].get_text()
print(f'기자:{writer}')



#날짜:
reg_date=doc.select('span.num_date')[0].get_text()
split_list=reg_date.split('. ') #결과['2024', ' 10', ' 28', ' 14:42']
reg_date=split_list[0]+split_list[1]+split_list[2]
print(reg_date)
