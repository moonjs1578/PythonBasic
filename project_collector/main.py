# - 화면 : 뉴스 카테고리를 선택(
import streamlit as st
from fnc_news import collect_news

# README.md → md(Markdown) 문서
# ㄴ emoiji(아이콘) → https://snskeyboard.com/emoji/
# Streamlit Doc → https://docs.streamlit.io/

# streamlit run project_collector/main.py
category="digital" #IT
def main():
    st.set_page_config(
        page_title="뉴스 수집기",
        page_icon="project_collector/img/favicon.png"
    )
    st.title("NEWS: :blue[Collector]")
    st.text("DAUM 뉴스를 수집합니다.")
    
    category={
        "사회":"society",
        "정치":"politics",
        "경제":"economic",
        "국제":"foreign",
        "문화":"culture",
        "IT":"digital"
    }
    with st.expander(label="뉴스 카테고리", expanded=False):
        for key, value in category.items():
            st.text(f"{key}({value})")
    
    with st.form(key="form"):
        # 1. 정규식 → 문자만 추출(숫자, 특수문자 제거!)
        # 2. 수집 데이터를 엑셀로 다운로드
        # 3. README.md 작성! → 프로젝트 정리(Github)
        sel_category=st.text_input(label="수집하고 싶은 뉴스 카테고리").strip()
        st.write(sel_category)    
        st.form_submit_button("수집")
    
    
    
    
    
    
    #print(">> 뉴스를 수집합니다.")
    #collect_news(category)
    
if __name__ =="__main__":
    main()
