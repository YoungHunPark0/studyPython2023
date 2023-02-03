# urllib 패키지 불러오기
from urllib.request import Request, urlopen  # request,urlopen 2개만 원한다
                                             #노란색 = 함수
req = Request('https://www.naver.com') #https = http+security약자 보안강화
res = urlopen(req)
print(res.status)
