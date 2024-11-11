##########
## 프로젝트:kisok_ice
## 작성자:food_del
## 최초 생성:2024년10월14일
## 마지막수정:2024년10월14일
## 내용:아이스크림을 판매하는 키오스크의 메인 프로그램
## +회사명
## +라이센스

from service_kiosk import print_sub_menu, input_menu_num

#########################
##1.메뉴와 가격표 생성##
###########################
#Didt 타입 생성-> 향후'데이터베이스'사용!
#-메인 메뉴
main_menu={
    1:'아이스크림',
    2:'음료',
    3:'디저트'
}
#-서브메뉴
icecream_menu={
    1:'엄마는 외계인',
    2:'민초가 최고',
    3:'베리베리 굿입니다'
}
icecream_prince={
    1:5000,
    2:3000,
    3:2000
}
drink_menu={
    1:'시원한 아아',
    2:'민초맛 아이스티',
    3:'차가운 핫초코'
}
drink_prince={
    1:3000,
    2:2000,
    3:1000
}
desert_menu={
    1:'3단케이크',
    2:'4단케이크',
    3:'5단케이크'
}
desert_prince={
    1:1000,
    2:2000,
    3:3000
}
#사용자가 주문한 메뉴 목록
order_list=[]



#############################
##2.메인 메뉴 출력##
##################################
while True:
    print(''*50)
    print('==베스킨 조선==')
    print('1.아이스크림')
    print('2.음료')
    print('3.디저트')
    print('>>MSG:메뉴를 선택해주세요.')

    order=input_menu_num(3)
        
    if order ==1:  #서브:아이스크림
        print_sub_menu(icecream_menu,icecream_prince,3)
        sub_order=input_menu_num(3)
        order_list.append([icecream_menu[sub_order],icecream_prince[sub_order]])
    elif order==2: #서브:음료
        print_sub_menu(drink_menu,drink_prince,3)
        sub_order=input_menu_num(3)
        order_list.append([drink_menu[sub_order],drink_prince[sub_order]])
    elif order==3: #서브:디저트
        print_sub_menu(desert_menu,desert_prince,3)
        sub_order=input_menu_num(3)
        order_list.append([desert_menu[sub_order],desert_prince[sub_order]])
    
    #추가 주문을 할거냐? 결제를 할거냐?
    #input() yes/no: yes or no 
    #y:추가 주문
    #n:결제하는 곳으로 가기!9(x)
    
    
    print('>>MSG:추가 주문하시겠습니까?')
    while True:
        yn=input('y=n:').lower()
        if yn=='y':
        elif yn=='n':
            break
        elif yn=='n':
            break
        else:
            print('>>WARNING:올바른 값을 입력해주세요.')
            
            
            
            
    if yn=='y':
        continue
    elif yn=='n':
        pass
    
    
        
        #주문 내역 출력
        print(''*50)
        print(f'==주문 메뉴==')
        total=0
        for i,item in enumerate(order_list):
            print(f'{i+1}.{item[0]}({item[1]}원)') 
            total+= item[1]
        print(f'고객님이 주문하신 메뉴는 총 {len(order_list)}건으로')
        print(f'결제금액은{total}원 입니다.')
        print(f'이용해주셔서 감사합니다.')    
    
    
    
    
    
    
    
    '''
    if 주문
    else:
    '''

    
    #사용자가 주문한 메뉴 출력
    for item in order_list:
        print(item)
        

