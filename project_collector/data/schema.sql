#테이블 생성 SQL(대문자는 원래있는거고 소문자는 내가 만들어낸것)
#-CHAR(문자열)
#-VARCHAR(가변문자)
#-VARCHAR(500)-> byte 크기

#(-영어는 한글자가 2바이트 한글은 한자가 3바이트)
                  title
#-CHAR(10)      |a|b|c| | | (뒤에 없어도 무조건 칸을 다 확보)- 문자열의 길이가 고정일때
#-VARCHAR(10)   |a|b|c|(뒤에 안만들고 필요한 만큼만 저장)     - 문자열의 길이가 변동일때
         
#-datetime ->날짜("년월일시분"   이거를 무조건)        
#-AUTO_INCREMENT:1~5까지하고 3개 더 추가하고 싶을때 자동으로 6~8로 뒤에 숫자세서 보내주는것
#Primary Key(PK키)
  ㄴ테이블안의 모든 데이터를 유일하게 식별할 수 있는 값    
USE chosun; #CHOSUN DB를 사용
  
#테이블 삭제(만약 존재하면)
#-CASECADE:연쇄반응 (게시판에 같이 있는 댓글까지 같이 묶어서 지워버려)
#예) 게시판 테이블
#	  ㄴ댓글 테이블
DROP TABLE IF EXISTS tbl_news CASCADE;
CREATE TABLE IF NOT EXISTS tbl_news(
	id		 INT  AUTO_INCREMENT PRIMARY KEY,
	title	 VARCHAR(200),	
	writer   VARCHAR(50),
	content  VARCHAR(10000),
	regdate  VARCHAR(50)
	
);
#테이블 조회(실행은 ctrl f5)
SELECT*FROM tbl_news;

