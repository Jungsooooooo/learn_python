#문자열 인덱스
text='abc'

text[0],  text[-3] #동일
text[1],  text[-2] 
text[2],  text[-1]

#문자열 슬라이스

textslice='abcde fgh ijk'
print(textslice[2:5]) #c~e까지 출력

print(textslice[5:]) #f부터 끝까지 출력
print(textslice[:5]) #처음부터 5까지.

print(textslice[0:8:2]) #첨부터 8까지 2칸 간격으로 출력
print(textslice[8:0:-1]) # 반대로 출력 

print(textslice[::-1]) #문자열 뒤집기

# 출력 지정
text = 'abcde {} {}'
print(text.format('ABC',123))

# 대체하기
textreple = 'abcde ABC ABC'
print(textreple.replace('ABC',"KKK"))

# 합치기
textj = 'abcde'
print('/'.join(textj)) #문자 사이사이에 /가 들어감 -> a/b/c/d/e

# 개수 확인하기
textc = 'abcde'
print(text.count('a')) #1 -> 문자열 'a' 갯수를 셈

# 제거하기 *중간값은 제거 못함
textd='  abcde  '
textd.strip()   #앞, 뒤 공백 제거
textd.lstrip()  #왼쪽 제거
textd.rstrip ()  #오른쪽 제거

#인덱스 찾기
textf = 'ABC ABC'
text.find('A')    # 0 -> 왼쪽이 기준이고 처음에 찾은 자릿수 추출 
text.rfind('A')   # 4 -> 오른쪽이 기준이고 처음에 찾은 자릿수 추출
textf.index('A')  # 0 -> 왼쪽이 기준이고 처음에 찾은 자릿수 추출
textf.rindex('A') # 4 -> 오른쪽이 기준이고 처음에 찾은 자릿수 추출

#확인 boolean 값
textc = 'abc'

textc.isalpha() # 알파벳
textc.isdigit() # 숫자
textc.isalnum() # 숫자와 알파벳
textc.isupper() # 대문자
textc.islower() # 소문자

#대/소문자 만들기

textCr = 'AbCabc'
print(textCr.upper()) #대문자로
print(textCr.lower()) #소문자로

#0 채우기
y="2023"
m='8'
d='1'

print(m.zfill(2))