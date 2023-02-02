# 클래스 생성      클래스 : 변수와 함수의 집합
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'    # 명사 name 등 -> 속성변수(글로벌변수)

    # 1. 생성자 추가
    # def __init__(self) -> None:     # -> None 은 없어도됨
    #     self.name = '홍길동'        # 매개변수(글로벌변수x)
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None:   # 한번도 안쓰여져서 연한색상 써지면 진해짐
        self.name = name
        self.height = height 
        self.gender = gender

    def walk(self):     # 컴퓨터한테 걸어라고 명령. 동사 - > 함수
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):      # 클래스에만 self 사용
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')


    # 2. 생성자외 매직메서드 (펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}입니다.'

younghun = Person('박영훈', 175, 'male') # 이렇게 만든 객체생성 instance(하나의 예) 라고함
#younghun.name = '박영훈'
#younghun.height = '175'
#younghun.gender = 'male'
#younghun.blood_type = 'RH+ B'

print(f'{younghun.name}의 혈액형은 {younghun.blood_type}입니다.')

younghun.run('Fast')
print(younghun)

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)


print('==================')
# 파라미터를 받는 생성자를 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
