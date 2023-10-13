#for문으로 list 추가

li=[]

for i in range(5):
    li.append(5)

print(li)

#for문으로 list 값 출력
for i in range(len(li)):
    print(li[i])

for i in li:
    print(i)


# 리스트 분리하기
li=['a','B','c','D']    
up=[]
low=[]

for i in li:
    if i.isupper():
        up.append(i)
    else :
        low.append(i)    

print(up)
print(low)