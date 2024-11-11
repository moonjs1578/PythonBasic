#라이브러리(library),패키지(package),모듈(module)
#라이브러리>=패키지>=모듈

# 라이브러리:외부 개발자가 개발해 놓은 코드 묶음
#     패키지1
        #  모듈1
        #  모듈2
        
    #   패키지2
        #  도듈1
        # 모듈2
        
        
        
'''
사용방법
외부에서 개발해씩 때문에 프로그래밍 언어 설치하면 존재x
1.다운로드 (아나콘다 pip install)
2.불러오기(import 라이브러리)
3.사용하기(라이브러리.math())
*가정:'request' 라이브러리 내에 모듈 1000개 존재

import requests
-- 1000개 모두 불러오기
--requests.get()


2.from request import,post 
-- get(),post() 2개만 불러오기
--get()
--post()

*AS(Alias:'별명')
import requests as req
--req.get()

'''

