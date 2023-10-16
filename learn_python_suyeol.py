# 등차 수열
# 앞 항에 일정한 수를 더해 만드는 수열
# 3, 8, 13, 18, 23, 28 n번째 항 구하기

# n=int(input('n:'))

# a= 3

# for i in range(n-1):
#     a=a+5

# print(a)    

# 등비 수열
# 앞 항에 일정한 수를 곱해 만드는 수열
# 3, 6, 12, 24, 48, 96 n번째 항 구하기

# n=int(input('n:'))

# a=3 #시작값

# for i in range(n-1):
#     a=a*2 # + 값

# print(a)    

# 피보나치 수열
# 바로 앞의 두 개의 항을 더해 만드는 수
# 1, 1, 2, 3, 5, 8, 13

n=int(input('n:'))

a=1
b=1

for i in range(n-2):
    c=a+b
    a=b
    b=c

print(b)    