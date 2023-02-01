# 구구단 프로그램
for x in range(2, 10):
    print(f'{x}단 시작 =======')
    for y in range(1, 10):
        #print(f'{x} X {y} = {x*y}')
        print(f'{x} X {y} = {x*y:>2}', end=' ') # :>2 이면 두자리로 만들어서 오른쪽정렬 
        #세로로 너무길어서 가로로 한줄로 만드는법 , end=' '
        # print(x,'*',y,'=',x*y)
    print()     # 2단~9단 나눠서 나오게됨
