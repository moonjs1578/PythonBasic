# 프론트엔드 - Controller - Service - DAO - DB
# streamlist - main.py - Service       - DB

# 서비스층 : 실제 비지니스로직의 기능을 담당
# NVC, NVT 패턴 
# -> 시스템 개발시 사용하는 패턴
# 웹브라우저 요청(request) : http://www.naver.com/cafe
#
# 웹서버(네이버 서버)
# 1. Controller : 요청을 받아서 해당 로직을 처리할 수 있는 Service로 전달하는 역할
#   -> Cafe 관련 Service로 전달
# 2. Service : 실제 비지니스 로직을 처리하는 곳
#   -> Cafe 글쓰기 관련 함수(cafe_insert)()로 처리
#   -> def cafe_insert() 처리하는 도중에 DB가 필요한 경우 DAO로 전달
# 3. DAO(Data Access Object) : DB관련 로직을 처리
#   -> CafeDAO를 사용해서 SQL(INSERT INTO~) 실행
#   -> DB로부터 처리받은 결과를 Service로 전달
# 4. Service
#   -> DAO로부터 처리받은 결과를 Controller로 전달
# 5. Controller
#   -> Service로부터 처리받은 결과를 웹브라우저에게 전달(Response)

# 겨울방학때 추천 코스
# 1. SQLD 자격증 취득
#   -> 요즘은 ORM으로 개발하는데 SQL 필요한가?
#   -> ORM을 할려고해도 SQL을 이해하고 있어야 훨씬 좋음
#   -> 복잡한 SQL구조는 ORM으로 구현 불가능(그때는 SQL 직접 사용)
# 2. 웹 개발 공부
#   -> 웹 개발 -> 모든 IT의 정수
#   -> Python 웹 프레임워크 : Django(대부분 장고), Flask(비추), FastAPI(점유율 오르는 추세긴 함(쉬움))-> 추천
#   * Python 웹 개발자 취업? 매우 어렵, 잘 안써(점유율 매우 낮음)
#       1 등 : SprintBoot(JAVA)
#       2 등 : Node, js(JavaScript)
#       3 등 : Django(Python)
#   * 나는 졸언 전에 취업하고 싶다. SprintBoot(취업 매우 잘됨)
#   * HTML, CSS, JS(기본) : 1달 공부
#   * 토이프로젝트, 사이드프로젝트, 펫프로젝트
#       -> 개인 웹 사이트
# 
from common.connection import connection
import pandas as pd


# 도서목록 조회(ALL)
def get_books():
    conn=connection()
    try:
        curs=conn.cursor()
        sql="""
            SELECT * FROM tbl_book;
        """
        curs.execute(sql) # 실행문 
        # 전체결과 -> Dict -> 2차원데이터
        rows=curs.fetchall()   # 실행결과 받기(전체) 받기
        # 2차원 Dict 데이터 -> 표 형태로 변환
        rows=pd.DataFrame(rows) # Python의 DataFrame형태로 변환
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 도서검색
def search_books(keyword: str):
    conn=connection()
    
    try:
        curs=conn.cursor()
        sql="""
        SELECT *
        FROM tbl_book
        WHERE book_name LIKE %(keyword)s
        OR book_writer LIKE %(keyword)s
        OR book_publisher LIKE %(keyword)s;
        """
        curs.execute(sql, {"keyword" : "%"+keyword+"%"})
        rows=curs.fetchall()
        print(rows)
        rows=pd.DataFrame(rows)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 도서등록
def insert_book(book: dict):
    conn=connection()
    try:
        curs=conn.cursor()
        sql="""
            INSERT INTO tbl_book(book_name, book_writer, book_publisher, book_price) 
            VALUES(%(book_name)s, %(book_writer)s, %(book_publisher)s, %(book_price)s);
        """
        curs.execute(sql,book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

# * UPDATE문과 DELETE문은 반드시 WHERE 절과 함께 사용할 것!!!!!

# 도서수정
def update_book(book: dict):
    conn=connection()
    try:
        curs=conn.cursor()
        sql="""
            UPDATE tbl_book 
            SET book_name=%(book_name)s,
                book_writer=%(book_writer)s,
                book_publisher=%(book_publisher)s,
                register_at=%(register_at)s,
                useyn=%(useyn)s
            WHERE book_isbn=%(book_isbn)s;
        """
        curs.execute(sql,book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

# 도서삭제
def delete_book(book_isbn: dict):
    conn=connection()
    try:
        curs=conn.cursor()
        sql="""
            DELETE FROM tbl_book
            WHERE book_isbn=%(book_isbn)s;
        """
        curs.execute(sql,{"book_isbn" : book_isbn})
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()