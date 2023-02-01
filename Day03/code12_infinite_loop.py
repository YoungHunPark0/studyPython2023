# 무한반복 예제
num =0

while True:
    print('메뉴를 선택하세요.')
    print('  1. 회원입력')
    print('  2. 회원검색')
    print('  3. 회원수정')
    print('  4. 회원삭제')
    print('  5. 프로그램 종료')
    num = input('메뉴번호 입력 > ') # '1' 문자 1은 숫자1과 다름
    num = int(num) # 문자로 받은 '1'을 숫자 1로 변경

    if num == 1: # if '1' == 1:
        print('회원입력 시작!')
    elif num == 2:
        print('회원검색 시작!')
    elif num == 3:
        print('회원수정 시작!')
    elif num == 4:
        print('회원삭제 시작!')            
    elif num == 5:
        print('프로그램종료')
        break
    else:
        continue        