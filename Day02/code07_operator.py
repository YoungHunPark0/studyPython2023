# 연산자
# 할당연산 assignment
# 2 = 1 (x)
#1 = val (x)
val = 1 # 변수(공간)에 넣을 수 있음

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 //2) # 정수나누기
print(6 // 3)
print(9 % 3) # 나머지 3->0 6->0 9->0 12->0 3으로 나눠서 0이면 3의배수

#print(6 / 0) #컴퓨터는 6으로 0을 못나눠서 zero division에러나옴- 이렇게 하지말기 
#print(6 // 0)

print(2 ** 10) # 2의 10승

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)
print(first + ' ' + second) #연산자 + ' ' 하면 띄어쓰기가 가능함
print(first, second)
print(first * 4)
#print(first - second) # 문자열연산에는 +, * 만 지원함

# 문자열 길이
print(len(first))
#print(first[0])
#print(first[1])
#print(first[2])
#print(first[3])
#print(first[4])
#print(first[5]) #인덱스에러 5는 x

# 파이썬에 인덱스 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
#print(first[-6] # 뒤에서 부터 -5가 H

# 리스트 자르기
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])  # 2023 2부터 0,1,2... 네번째로 끊으면 2023
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일' 
+ current[11:13] + '시' + current[14:16]+ '분' + (current[17:]) + '초')

print(current[-19:-15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)

#que[5] = 10 # 길이가 5까지라서
#print(que)

que.append(10) # 맨 마지막에 추가
print(que)


que.insert(3, 99) # 3번째에 99를 넣겠다 insert - 내가원하는위치에 특정인덱스 넣음
print(que)

que.remove(99) # 어떠한 값을 삭제
print(que)

# 이런거안됨
#tup = (1, 2, 3, 4, 5)
#tup[1] = 9
#print(tup)

# 문자열 == 문자 리스트
title = 'python'
print(title[0])

#title[0] = 'P' # 문자열에서는 값변경X
print('P' + title[1:])

# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} to you, {1}!!".format(2, 'Hey'))
# 최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} to you, {sayHello}!!")  

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.02f}입니다.')
print(f'파이는 {pi:10.3f}입니다.') #.3은 소수점 3자리, 10은 앞 10자리 표시

# 문자열을 특정문자로 자르기(많이쓰임!)
full_name = 'Young Hun. Park'
vals = full_name.split() #split 자르다. 스페이스로 자르기
print(type(vals))
print(vals)

vals = full_name.split('.') # .으로 지정
print(vals)

print(full_name.replace('Young Hun.', 'Ashely')) #replace 자리대체함

# 문자열 공백 없애기
hi = '          Hello~ Bye          '
print(hi.lstrip() + '|') # left 왼쪽의 공백 없애다
print(hi.rstrip() + '|') # right 오른쪽공백  '|' 파이프키 라고부름
print(hi.strip() + '|')

# 문자열에서 값을 찾기
print(full_name.index('g')) # index 리스트에 몇번째에 있는지 young hun. park에서 g는 5번째(0,1,2,3,4) 
#print(full_name.index('Z'))

print(full_name.find('Z')) # 찾는 게 없으면 -1
print(full_name.find('g')) 

# 찾는 단어의 개수
print(full_name.count('u'))

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper()) #upper 위로 올리다. 전부 대문자 출력. 영어검색 한정으로 대문자소문자 구분없애기 위해
print(full_name.lower()) # lower 전부 소문자 출력

## 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)