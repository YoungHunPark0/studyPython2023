# 예외처리 - 예외를 잡는것
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b        

try:
    x, y = input('두 수를 입력하세요 > ').split() # split은 int를 한번에 못나눔
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요?') # 이거 실행 뒤 종료됨
                        #except하고 finally 안될 줄 알았는데 됨
# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x, y))
# except ZeroDivisionError as e:      #ZeroDivisionError의 부모가 exception
#     print('0으로 나누면 안되요!') # 굳이 없어도 됨
except Exception as e:  #Exception(예외)을 -> e로 표현 
    print(e)    # except exeption as e 무조건 제일마지막에 있어야함
                # 예외처리 할 때 많이 사용함
finally:       # finally는 try 구문에서 무조건 나옴
    print('계산은 계속됩니다!!') #예외가 나든안나든 무조건 출력되게함

print(add(x, y))
print(mul(x, y))