#set 순서가 없고 중복 허용이 안됨.

se=set()
#se={} 사용 불가능 -> 비어있는 값을 만드려면 함수 써야 함.

#세트 특징
a={2,4,6,8,2}
b={2,3,4}
print(a)        #순서 변경됨 넣는 순서 의미 없음. 그리고 중복값은 알아서 제거

a.add(5)        #추가
a.remove(5)     #삭제

1 in a          # 값 확인
len(a)          # 길이 확인
#sum,min,max,list,tuple 함수들은 동일함

print(a&b)  #교집합
a|b         #합집합 -> 중복 없어짐.
print(a-b)  #차집합
print(a^b)  #대칭차집합 -> a-b의 값과 b-a의 값을 더한것. 서로의 차집합을 더한 것.