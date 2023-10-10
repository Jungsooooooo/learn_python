# a=int(input('a 입력:'))
# b=int(input('b 입력:'))
# c=int(input('c 입력:'))

#print(a,b,c,a+b+c)

# split 특정 기준으로 문자열 분리.
#text=input('날짜 입력 yyyy.mm.dd')
#y,m,d=text.split('.')

#map 한 줄에 여러개 숫자를 받기.
#y,m,d=map(int,text.split('.'))
#print(text,y,m,d)

#숫자 출력하기

# 숫자와 문자 함꼐 출력하기 (1) 콤마 & 형변환
x=3
y=5
print(x,'과',y,'의 합은',x+y)

# 숫자와 문자 함꼐 출력하기 (2) end='' 좋은 방법 x
print(x,end='')
print('과 ',end='')
print(y,end='')
print('의 합은 ',end='')
print(x+y,end='')
print('이다.')

# 숫자와 문자 함꼐 출력하기 (3) format() 좋은 방법 o
print('{}과 {}의 합은 {}이다'.format(x,y,x+y) )

#산술 연사자 > 관계 연산자 > 논리 연산자로 우선순위.

#반올림
print(round(3.33))
print(round(3.66,1)) # -> 뒤에 숫자는 소수점 몇 자리까지 나타냄을 의미. 1은 소수 첫째자리

# 절대값
print(abs(-3))

#제곱
print(pow(3,2))
print(3**2)

#나눗셈
x,y = divmod(7,2) #7을 2로 나눈 몫과 나머지가 x,y에 들어감
print(x) # 몫
print(y) # 나머지

#최댓값
max([7,5,1,3])

#최소값
min([7,5,1,3])

#합 
sum(7,5,1,3)