################################################
## 프로젝트     : kiosk_ice
## 작성자       : 문정수
## 최초생성     : 2024년 10월 14일
## 마지막수정   : 2024년 10월 14일
## 내용 : 아이스크림을 판매하는 키오스크의 메인 프로그램
## +회사명
## +라이센스

from service_kisok import print_sub_menu, input_menu_num
##########################
## 1. 메뉴와 가격표 생성 ##
##########################
# Dict타입생성 > 향후 데이터베이스 사용!
# - 메인 메뉴
main_menu={
    1:"아이스크림", 
    2:"음료",
    3:"디저트"
}
# - 서브 메뉴
icecream_menu={
    1:"메로나",
    2:"누가바",
    3:"바밤바"
}
icecream_price={
    1:3500,
    2:4000,
    3:4500
}
drink_menu={
    1:"콜라",
    2:"사이다",
    3:"환타"
}
drink_pirce={
    1:5500,
    2:5000,
    3:4000
}
desert_menu={
    1:"아이스 모찌",
    2:"아이스 샌드",
    3:"아이스크림 롤"
}
desert_price={
    1:1000,
    2:2000,
    3:3000
}
# 사용자가 주문한 메뉴 목록
order_list=[]


#####################
## 2. 매인메뉴 출력 ##
#####################
while True:
    print("*"*50)
    print("** == 베스킨 조선 ==")
    print("** 1. 아이스크림")
    print("** 2. 음료")
    print("** 3. 디저트")
    print(">> MSG : 메뉴를 선택해주세요");
    
    order=input_menu_num(3)
    if order ==1:   # 서브 : 아이스크림
        print_sub_menu(icecream_menu, icecream_price,3)
        sub_order=input_menu_num(3)
        #["아몬드봉봉", 4500]
        order_list.append([icecream_menu[sub_order], icecream_price[sub_order]])
    elif order ==2: # 서브 : 음료
        print_sub_menu(drink_menu, drink_pirce,3)
        sub_order=input_menu_num(3)
        order_list.append([drink_menu[sub_order], drink_pirce[sub_order]])
    elif order ==3: # 서브 : 디저트
        print_sub_menu(desert_menu, desert_price,3)
        sub_order=input_menu_num(3)
        order_list.append([desert_menu[sub_order], desert_price[sub_order]])
    ans=input("추가주문하시겠습니까?")
    if(ans=='yes'):
        pass
    elif(ans=='no'):
        break
    for item in order_list:
        print(item)
