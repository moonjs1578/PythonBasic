# 다음 뉴스 수집기
import streamlit as st
from fnc_news import collect_news
import re  # 정규식

# README.md → md(Markdown) 문서
#  ㄴ emoiji(아이콘) → https://snskeyboard.com/emoji/
# Steamlit Doc → https://docs.streamlit.io/

# streamlit run project_collector/main.py


def main():
    st.set_page_config(
        page_title="뉴스 수집기",  # 웹사이트 제목
        page_icon="project_collector/img/favicon.png"                  
    )
    st.title("NEWS: :blue[Collector]")
    st.text("DAUM 뉴스를 수집합니다.")
           
    with st.form(key="form"):
        submitted = st.form_submit_button("수집")
        if submitted:
            collect_news()
    
               
if __name__ == "__main__":
    main()
   