# - 화면 : 뉴스 카테고리를 선택(
from fnc_news import collect_news
category="digital" #IT
def main():
    print(">> 뉴스를 수집합니다.")
    collect_news(category)
    
if __name__ =="__main__":
    main()
