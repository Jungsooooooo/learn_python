#함수 정의

def aa():
    print('hi')


def bb(x):
    for i in range(x):
        print('hello')

def cc()        :
    n=int(input('n:'))
    return n*2

def dd(x,y):
    print(x*y)
    return x*y

print(cc())
print(aa()) # 리턴 값 없으면 None