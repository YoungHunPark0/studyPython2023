# ramdom 모듈 사용
import random

#print(random.choice(range(1, 7)))

numbers = [i for i in range(1, 46)] # 1~45까지 리스트
lottery = []

for i in range(6): #0부터6 컴퓨터는 0부터(예외도 있음)
    lottery.append(random.choice(numbers))

print(lottery)