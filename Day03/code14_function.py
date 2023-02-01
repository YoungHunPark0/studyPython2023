# 함수
# 함수정의 - 이건 실행이 아님
def add(x, y): 
    result = x + y # x+y를 result에 담았음
    return result # return안하면 아무것도 안나옴

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result
    
# 함수호출
val = add(1024, 5) #val한테 뭔가 넘겨줘야함 = return
print(val)

val = sub(1024, 1000)
print(val)

val = mul(512, 2)
print(val)

val = div(108, 10)
print(val)