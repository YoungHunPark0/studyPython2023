# 모듈 사용
import math as m # 앞으로 math라고 안쓰고 m이라고 하겠다. #math는 클래스로 안된 모듈
import code22_person as p # 우리가 만든 클래스
from code23_car import Car

print(m.pi)

print(m.tan(0))
print(m.ceil(3.1))
print(2 ** 10) # 정수
print(m.pow(2, 10)) # 실수(소수값나옴)

# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성') # ()는 생성, 생성했으면 변수공간 줘야함
print(me)

#
mycar = Car
print(mycar)