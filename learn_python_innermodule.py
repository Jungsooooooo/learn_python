#내장 모듈

import math

print(math.ceil(2.1))   #올림
math.floor(2.1)         #내림
math.factorial(10)      #팩토리얼
math.sqrt(4)            #루트
math.pi                 #원주율 -> 함수가 아니라 값도 저장되어 있음.


import random

random.randint(1,5) #1~5 정수 랜덤값 생성
random.random() # 0<= <1 랜덤값 생성


li=['a','b','c']

random.choice(li)   #리스트 중 랜덤 
random.sample(li,2) #리스트 중 2개 선택
random.shuffle(li)  #리스트 순서 랜덤 섞기