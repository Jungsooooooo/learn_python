#약수의 개수 구하기
#n을 입력받아 n의 약수의 개수 구하기

n= int(input('n:'))

check = 0
li=[]

for i in range(1, n+1):
    if n%i==0:
        check= check+1

for i in range(1,n+1):
    if n%i==0 :
        li.append(i)       

print(len(li))
print(check)        

#OX 개수 구하기

text= list(input("text"))

print(text.count('o'))
print(text.count('x'))

o_count = 0
x_count = 0

for i in text:
    if i == 'o':
        o_count= o_count+1
    elif i=='x':
        x_count=x_count+1    

#평균

num = list(map(int,input('num:').split()))

avg = sum(num)/len(num)

check = 0 

for i in num:
    if i>=avg:
        check= check+1

print(avg)        
print(check)