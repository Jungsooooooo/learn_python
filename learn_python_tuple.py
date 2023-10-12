#tuple

#tuple -> 값을 변경할 수 없는 열거형 집합.

tu=()
tu=tuple()

tu=('a','b','c')

tu.index('a')       #위치 찾기
'b' in tu           #b 존재유무 확인
len(tu)             #전체 개수
tu.count('a')       #a개수

num=(5,7,9)
n1,n2,n3 = num      #num을 각각 변수 할당.


a='one'
b='two'

(a,b)=(b,a)         # 값 교환하기

print(a,b)

li=['a','b','c']
tuple(li)           # list->tuple

tu=('a','b','c')
list(tu)            # tuple->list