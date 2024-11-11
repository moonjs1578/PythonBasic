## 1.개발환경 구축

### 1-1.다운로드
-anaconda
-vscode

### 1-2. 아나콘다 세팅
-conda env list (가상환경 목록 확인)
-conda create -n developer python =3.11(가상환경 생성)
-conda activate developer(가상환경 접속)
-pip list (설치된 라이브러리 목록 확인)
-pip install[라이브러리](라이브러리 설처)
-cls(화면 clear)

### 1-3.VSCODE 세팅
1. Extension 설치
-python
-prettier
-python extention pack
-Atom Material  Icons
-Atom Material Thema
2. Settings 
-[Mouse Wheel Zoom] 켜기
3.Thema 설정
4.[ctrl]+[Shift]+[p] -> 'python select interpreter' 클릭후 deverloprer

### 1.4 명령어 단축키
-[ctrl]+[']: 터미널 켜기
-[ctrl]+[,]:setting 켜기
-[ctrl]+[/]: 주석(1line) 토글, 블록(+여러줄 가능)
-[ctrl]+[f11]:파이썬 코드실행 (터미널)
-코드 옆에 주석 달고 싶으면 스페이스바 2번 띄고,그다음에 #쓰기

1.기본 터미널 세팅 
2.터미널 폰트 사이즈 수정
3.python run 단축키 설정 


## 2.데이터베이스
    #데이터를 효율적으로 젖아하고 관리할 수 있?는 프로그램(DBMS)
## 2-1 DBMS(데이터베이스 관리 시스템)
     #관계형 데이터 베이스(RDB):표형태,보안이 중요하거나,영속성 데이터
     (개인정보,금융정보,...)
     ->Mariadb,Oracle,MySQL.PostgreSQL
     #NoSQL:자유 형태,대용량 수집 데이터
        ->MongoDB


## 2-2 sql(구조질의어)
- dbms에게 명령을 내릴때 사용
-예 SELECT*FROM:tbl_user;

## 2-3 DBMS 설치 방벙
1.로컬 설치(설치 파일 다운로드 직접설치)
2,클라우드(ams. gcp,azure ,기타등등)
3.도커 컨테이너


### 2-4.데이터베이스 구조
1. DBMS=->MariaDB,Oracle.MySQL.PostreSQL
    ㄴ data_base->chosun
        ㄴ table_tbl_news  (데이터 베이스,테이블 여러개 만들 수 있다) - sql 사용

 - 프로젝트별로 database 생성
 -   data baese(쇼핑몰)
 -     ㄴ table(회원)
 -     ㄴ table(상품)
 -     ㄴ table(구매)
-      ㄴ table(고객문의)

### 2-5 프로그래밍언어-DB 연결
 1. SQL Mapping: SQL을 작성->실행 (과거)
 2. ORM(object relation mapping) (최신)
 - SQL 복잡도 증가!->ORM 한계 

### 2-6. SQL매핑
1. connection 맺기(python-database)
   -IP,PORT,ID,PW
2.  일꾼 만들기(cursor 객체)
3.  job만들기(SQL작성)
4. 실행(일꾼-JOB)
5. 결과












## 3.도커(컨테이터)
-도커:컨테이너 가상화기술을 구현해주는 프로그램
-도커->도커엔제+도커 이미지
-도커 이미지:도커 컨테이너 실행을 위한 설계도면
-도커엔진:도커 이미지를 바탕으로 컨테이너를 실행

### 3-1 도커 명령어 
- docker ps : #현재 실행중인 컨테이너 확인
- docker images #현재 보유학고 있는 컨테이너 이미지 확인
-docker run #도커 컨테이너 이미지 확인
-docker logs [컨테이너 이름] #해당 컨테이너 로그 확인

 ```
 docker run --name mariadb -d  -p 3306:3306 -e MARIADB_ROOT_PASSWORD=mariadb mariadb     #누가 삭제하면 이 이코드를 윈도우 터미널에 넣으슈
- --name mariadb #컨테이너 이름
-d #데몬(백그라운드 실행)
-p 3306:3306 #포트(외부:내부)  ->외부 포트(호스트),내부포트(컨테이너)- 건물찾고 호수 찾고
-e ,MYSQL_ROOT_PASSWORD=mariadb #환경설정(ROOT 암호=mariadb)
-mariadb  #mariadb 컨테이너 실행! ->mariadb 이미지 필요!
-docker exec-it [컨테이너 이름]/bin/bash #해당 컨테이너 접속

```
## 참고:수업 전에 vs 코드키고/docker 들어가서 초록불 뜨게 하고 안되면 실행 버트/ 그다음 dbeaver들어가기 (이 순서 그대로 도커 다음 비버임)
## 숙제:docker 챝지피티 가서 공부해보기








# 전체 시스템 구조(학습용)-web/app
# client - server
# client(고객:웹 브라우저)

# ##구조
# client->네트워크->클라우드 컴퓨팅(aws)
#                 +server(리눅스 운영체제)
#                           도커 컨테이너
#                                데이터베이스(rdb,nosql)+sql
#                                프론트엔드
#                                백엔드 
#                                nginx
#                                database(데이터베이스)
# 프로그래밍 언어
# 디자인 패텀
# 자료구조
# github(버전 관리 도구)