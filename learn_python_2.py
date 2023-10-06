# 자료형 타입 확인 type()으로 확인 가능.
# 필요에 따라 자료형을 변경할 수 있다.
# int float

# a //b a를 b로 나눈 몫     - 정수형 a/b -> 실수형
# a % b a를 b로 나눈 나머지
# a **b a의 b 제곱  
# int 와 float 몇 결과는 무조건 float

a = 10
b = 5
c = 2.0
d = 0.5
print(a//b)

# 논리형 
# bool
# != 같지 않다 == 같다.
# not x -> x가 참이면 거짓, x가 거짓이면 참.

x = 10
y = 5
print(x != 7)

# 문자열형
# 다른 언어와 달리 문자와 문자열을 따로 구분하지 않는다.
# 연산 불가능
# 문자열 다루는 메소드 split join,upper,lower,replace 등


#print(3+'3')  # 동작 안함
print('3'+'3') # 33
print('3'*5)   # 33333

# 군집 자료형(집합의 형태)
# list tuple set dictionary
# 좀 더 자세히 다룰 예정


# 자료형 변환 방법
str(10)     #10을 문자열로
int('10')   #문자열을 숫자로
int(12.5)   #실수를 정수로
print(list('hello'))

a=int(input('숫자를 입력하세요'))

print(a+a)