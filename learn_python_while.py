# while

a=int(input('a:'))

while a>=0:
    print('실행')
    a=int(input('a:'))


# 무한루프
# a=10
# while a>0:
#     print('실행')

#n번 반복하기

#n=int(input('n:'))

#while n:
#    print(n)
    n=n-1 #-> 0이 되기까지 반복됨.

# e 또는 E가 입력될 때 까지 반복하기.
text=input('문자입력')    

while text!='e' and text!='E':
    text = input('e 또는 E 입력시 종료')
print('종료')    