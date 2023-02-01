# while문
hit = 0 # hit 찍다, 'hit = 0 -> 변수초기화' 파이썬은 hit가 숫자인지 모르기에 숫자선언해줘야됨

while hit < 11: # 10번 찍으면, while True:무한반복(조심해서 쓸것) 끄는법: 컨트롤+c 2번
        hit += 1 # hit를 1씩 증가
    
    print(f'나무를 {hit}번 찍었습니다')
    if hit == 10:
        print('나무가 넘어갔습니다!!!')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다. 끈질긴 놈')

print('나무찍기 완료')