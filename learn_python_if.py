#if

num= int(input('숫자 입력'))

if num>0:
    print('{}는 0보다 큽니다'.format(num))


#if ~ else

num= int(input('숫자 입력'))

if num%2==0:
    print("{}는 짝수입니다.".format(num))
else:
    print("{}는 홀수입니다.".format(num))    

#if ~elif ~else
age= int(input('나이 입력'))

if age<=7:
    print("유아")
elif age<=19:
    print("청소년")    
else:
    print("성인")