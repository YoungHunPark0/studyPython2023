import os
import code

# 자동차 클래스
class Car:
    __number = '54라 9538'

    def get_number(self):
        return self.__number
    
    # 클래스 외부에선 변경불가x, 멤버함수로는 내부를 조작가능O
    def set_number(self, number):
        self.__number = number
    
    def __init__(self, number='54라 9538') -> None: #실행 2
        print('__init__')   # init을 보통 생성자라고함.
        self.__number = number

    # def __new__(cls):       # 실행 1. 
    #     print('__new__')    #new는 문법적으로만 사용하고 실무에선 사용안함
    #     return super().__new__(cls) 
    #     # super - 컴퓨터는 부모자식 상속개념. super는 부모클래스(상속)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car(number='88호 7645')
print(yourcar)
yourcar.__number = '54라 9999' # 외부에서는 멤버변수 조작x
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는요, 아이오닉이고, 번호가 {mycar.get_number()} 에요.')

yourcar.__number = '132거 8874'
print(yourcar.get_number())
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)
