# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv

fileName = 'busanbus.csv'
dirName = 'C:/Source/GitHub/studyPython2023/'
fullPath = dirName + fileName

file = open(fullPath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')    # 구분자가 , 일 경우
next(reader)    # 헤더가 필요없을 때

for line in reader:
    print(line)

file.close()    # open하면 반드시 close!