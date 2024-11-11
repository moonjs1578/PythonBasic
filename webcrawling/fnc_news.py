import requests
from bs4 import BeautifulSoup

def get_news_info(url:str):

    result=requests.get(url)
    doc=BeautifulSoup(result.text,'html.parser')

    title= doc.select("h3.tit_view")[0].get_text() #문자섞여있는것중에 get text 를써서 텍스트만 가져감
    
    contents=doc.select('section > p')
    content=''
    for text in contents:
        content += text.get_text()

    #기자:
    writer_list=doc.select('span.txt_info')
    if len(writer_list)<2:
        writer=''
    else:
        writer=writer_list[0].get_text()
        
 

    reg_date=doc.select('span.num_date')[0].get_text()
    split_list=reg_date.split('. ') #결과['2024', ' 10', ' 28', ' 14:42'] #구분자를 '.'으로 두면 빈카이 생기니까 자르는 거를'.공백'으로 하면된다
    reg_date=split_list[0]+split_list[1]+split_list[2]



    print(f'뉴스제목:{title}')
    print(f'뉴스기자:{writer}')
    print(f'뉴스날짜:{reg_date}')
    print(f'뉴스본문:{content}')