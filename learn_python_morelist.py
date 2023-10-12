#문자 입력받아 공백 기준 자르기

"""
li1=input('문자입력').split() 
print(li1) #띄어 쓰기 기준으로 list 생성
"""

#문자 입력받아 전체 자르기
"""
li2=list(input('문자입력'))
print(li2) #문자 하나하나 리스트로(공백도 1개로 침)
"""

#숫자 하나씩 입력
"""
li3=[]

li3.append(int(input('입력1')))
li3.append(int(input('입력2')))
print(li3)
"""

#숫자 여러개 입력받기

li4=list(map(int,input('숫자 한꺼번에 입력').split()))
print(li4)