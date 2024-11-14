# Python ---------------- Database(MaraiDB)
# - IP
# - PORT
# - ID
# - PW

import pymysql 

# 집(통신사) → IP주소(고정, 유동)
# 127.0.0.1 → 루프백IP(DB 내컴퓨터 설치된 경우)
# Connet to MaraiDB
def connection():
    try:
        connection = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user = "root",
            password="mariadb",
            database="chosun",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
            
        )
        return connection
    # DB 연결
    # - ID, PW 틀림
    # - IP 주소 잘못
    # - DB 서버 작동 X
    # - 인터넷 X
    except pymysql.Error as e:
        print("fMARIDB 연결실패: {e}")