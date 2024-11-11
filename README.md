## 1. 개발환경 구축

### 1-1. 다운로드
- anaconda
- vscode

### i-2. 아나콘다 세팅
-실행하면 (base) 가상환경 자동 접속 됨
-conda env list                       (가상환경 목록 확인)
-conda create -n developer python=3.11(가상환경 생성)
-conda activate developer             (가상환경 접속)
-pip list                             (설치 된 라이브러리 목록 확인)
-pip install [라이브러리]              (라이브러리 설치)
-cls                                  (화면 clear)

### 1-3. VSCODE 세팅
1. Extensions 설치
-python
-prettier
-python extension pack
-Atom Material Icons
-Atom Material theme

2. Settings
-[Mouse Whell Zoom] 켜기
3. Theme 설정
4. [ctrl] + [shift] + [p] > "Python : Select Interpreter" 클릭 후 "developer" 가상환경 선택

### 1-4. 명령어 단축키
- [ctrl] + ['] : 터미널 켜기
- [ctrl] + [,] : Settings 켜기

### 2-5. 프로그래밍언어 - DB 연결
 1. SQL Mapping : SQL을 작성 → 실행 (과거))
 2. ORM(Object Relation Mapping) (최신))
 - SQL 복잡도 증가! → ORM 한계

### 2-6. SQL 매핑
 1. Connection 맺기(Python - Database)
    - IP, PORT, ID, PW
 2. 일꾼 만들기(cursor 객체)
 3. JOB 만들기(SQL 작성)
 4. 실행(일꾼-JOB)
 5. 결과 
 
 ## 3. 도커(컨테이너))
1. 기본 터미널 세팅
2. 터미널 폰트 사이즈 수정
3. python run 단축키 설정
