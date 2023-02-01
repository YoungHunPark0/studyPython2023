# 라이프 스코프
a = 1   # a는 값을 받기위한 변수 - 함수에서 사용하는 변수-> 매개변수

def vartest(a): 
    global a # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다
    a = a + 1
    return a

a = vartest(a) # vartest를 호출한 순간 global a가 살아났다가 return을 만나면 사라짐
print(a)
  