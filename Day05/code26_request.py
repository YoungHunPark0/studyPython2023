# 외부 패키지를 사용
import requests

res = requests.get('https://www.naver.com')
print(res.status_code)
print('=============')
print(res.content) 