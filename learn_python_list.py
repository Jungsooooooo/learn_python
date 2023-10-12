#list
li = []
li=list()

#리스트 인덱스
li=['a','b','c']
print(li[0])

li.index('c') #위치 찾기

li.append('f')              # 추가 -> 맨 끝에 추가 됨.
li.insert(0,'aa')           # 추가 -> 특정 자리에 추가 됨.

li.remove('aa')             #삭제 1
del li[0]                   #삭제 2

print('aa' in li)           #확인하기

len(li)                     #전체 개수
li.count('a')               #개수 세기

number=[1,2,3]
sum(number)                 #더하기
min(number)                 #최소
max(number)                 #최대

number.reverse()            #숫자 뒤집기

number.sort()               # 오름차순 정렬
number.sort(reverse=True)   # 내림차순 정렬