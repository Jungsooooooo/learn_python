# 문자 체크
# 긴 문장과 한문자를 이별갑ㄷ아
# t가 text안에 포함되어 있는지 확인

text= input('text:')

check = False

for i in text:
    if i == 't':
        check= True

print(check)            

# 숫자 체크
# 5개의 숫자를 입력받아 리스트를 만들고
# n을 입력받아 리스트 값에 n이 있는지 확인

li = list(map(int,input('li:').split()))
n = int(input('n:'))

check1 = False

for i in li:
    if i == n:
        check1= True
print(check1)        