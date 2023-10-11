#if + if

age=15
if age<=7:
    print('유아')
elif age<=19:
    if age<=13:
        print("초")    
    elif age<=16:
        print('중')    
    else:
        print('고')    
else:
    print('성인')

# for + if
n= 15       
for i in range(1,n+1):
    if i%3==0:
        print('홀수')
    else:
        print('짝수')        

#while + if
num1=0
num2=2       

while True:
    num1= num1+1
    print(num1)
    if num1==num2:
        break

#for + for
    for i in range(2,10):
        for l in range(1,10):
            print('{} x {} = {}'.format(i,l,i*l))