# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자) for문 탈출 break
                        # break말고도 이스케이프 문자 있음
print('1.Hello.\r\nWorld') # 예전에는 /r/n
print('2.Hello.\nWorld') # 이걸 권장(편해서)
print('3.Hello.\n\tWorld') # t == 탭
print('4.Hello.\n\t\bWorld') # b == 백스페이스
print('5.Hello.\n\'World\'') # \' 문자열내 홑따옴표
print('6.Hello. "World"')
print('7.Hello. \"World\"')

print('7.Hello. \\ World') # \를 문자열에 표현(파이썬만) 
print('8.Hello\0') # \0 은 문자열 끝남을 의미함


# 문자열 포맷팅 - 예전것(구닥다리)
# %로 포맷코드를 시작
me = '저'
name = '박영훈'
age = 20
print('%s는 %s입니다. %d대입니다.'% (me, name, age)) #순서대로 들어감 순서바꾸기x %s는 문자. 숫자x

print(f'{254.112233:.2f}') # 최신식 :.2f소수점두번째에서 자름

print('%9.2f' %(254.112233)) # 구식 전체자리수.소수점 (.도 침)
