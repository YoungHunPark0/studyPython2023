# 파일 읽어오기
file = open('./Day05/sample05.txt', 'r', encoding='utf-8')

while True:
    text = file.read()

    if not text: break

    print(text)

file.close()    #파이썬은 파일을 open하면 반드시 close 해야됨!