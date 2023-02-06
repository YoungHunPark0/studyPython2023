# 차 부모클래스
class Car:
    # Mother class 특징과 동작
    __name = '자동차'
    __color = 'white'
    __plate_number = '없음'
    __product_year = 1900  
    
    def __str__(self) -> str:
        return f'부모클래스'

    def get__name(self):
        return self.__name

    def run(self):
        return f'차가 달립니다.'

    def stop(self):
        return f'차가 멈춥니다'