#딕셔너리 특징
#키와 값으로 이루어짐

dic= dict()
dic={}


dic={'kor':82,'eng':83}
print(dic['kor'])

dic['sci']=100

print(dic)  #없는 키값을 선언 하면 dic에 알아서 추가가 됨.

#dic.clear() -> 전체삭제
'eng' in dic          #유무 확인
len(dic)              #개수 확인

dic.keys()            # 모든 키 얻기
dic.values()          # 모든 값 얻기
print(dic.items())    # 모든 순서쌍 얻기

list(dic.keys())

li=['ab','cd']
li2=[['chicken','치킨'],['pizza','피자']]
print(dict(li))     #->{'a': 'b', 'c': 'd'}
print(dict(li2))