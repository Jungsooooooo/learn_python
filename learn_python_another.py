#continue 해당 단계만 건너 뜀
#break 조건 만족하면 끝나버림
#pass

for i in range(1,11):
    if i==5:
        continue
    print(i)  #5는 출력 안됨.

for i in range(1,11):
    if i==5:
        break
    print(i) # 1,2,3,4 나옴

for i in range(1,11):
    if i==5:
        pass
    print(i) 

#pass를 쓰는 이유 -> 파이썬은 가로로 영역을 표시하지 않고 들여쓰기로 하기 때문에 