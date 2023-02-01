# for문
arr = [1,2,3,4,5]
sum = 0

for item in arr:    # i == item 줄임말. arr이라는 리스트[1,2,3,4,5]가 in들어와서 item하나씩 for문 적용
    #print(f'{item:2.2f}')       # arr는 정수, 2.2실수 - 실행시 소수점 표시
    print(item)
    sum += item  # == 'sum = sum + item'


print('합계는 ', sum)

# 리스트를 편하게 만드는 방법
vals = [i for i in range(1, 11)] # 범위가 1부터 11전까지 만듬 
#== [1,2,3,4,5,6,7,8,9,10]이상 쓰기엔 너무많아 사용함.
print(vals)

num = 0
for item in vals:
    num += 1
    if num % 2 == 0: # (% 나눈 나머지값)num을 2로 나눈값이 0이면, 
                     # 1을 2로 나누면 0이아니기에 홀수면 else로감
        #continue # 이후의 것을 수행하지 않고 다시 for문으로 감.
        break # break를 만나면 for문을 완전히 탈출. 2넣으면 0이나와서 끝나니 탈출.
        # if, break는 if문 안에 있어야만 사용가능
    else:
        print(num, '번 수는', item, '입니다')
       