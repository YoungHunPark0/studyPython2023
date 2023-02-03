# 다중입력          잘알고, 이해야함. 코딩테스트에서도 나옴
# x, y = input('두 영단어를 입력하세요 > ').split() 
    # split 자름 ()생성 잘라서 공간만듬 
# print(x)
# print(y)

# 완전 다중입력(개수가 몇개든지 상관없음)
inputs = list(map(str, input('단어를 입력하세요(개수상관X) > ').split())) # split로 자르니 단어로 잘림

print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수상관X) > ').split())) # 숫자받을려면 int 문자받을려면 str

print(inputs)