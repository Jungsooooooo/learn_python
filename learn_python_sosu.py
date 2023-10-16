# 소수 판별하기
# 숫자 하나 입력 받아 소수인지 아닌지 확인하기

# n = int(input('n:'))

# check=0

# for i in range(1, n+1):
#     if n%i ==0:
#         check=check+1

# if check==2:
#     print(True)        
# else:
#     print(False)    


# 범위 내의 소수 구하기
# a 값을 입력 받아 1~a 사이 모든 소수값 구하기 (a>0)

a=int(input('a:'))

li=[]

for n in range(2,a+1):
    check = True
    for i in range(2,n):
        if n%i==0:
            check= False
    if check:
        li.append(n)        
print(li)        