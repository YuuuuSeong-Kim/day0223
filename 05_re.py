import re

db = '''
3412 Bob 123
3834 Jonny 333
1248 Kate 634
1423 Tony 567
2567 Peter 435
3567 Alice 535
1234 Tiger 569
1548 Kerry 534
'''
# print(db)

#숫자만 출력
# result = re.findall("[0-9]+",db)
# print(result)
# print(type(result))

# 연습) 이름만 출력
# result = re.findall("[A-z]+",db)
# print(result)

# result = re.findall("[0-9]{4}",db)
# result = re.findall("\d{4}",db)
# result = re.findall("^\d+",db,re.MULTILINE)
# re.MULTILINE : 찾고자 하는 데이터가 줄 마다 있다
# print(result)

# 연습) id만 추출하여 출력
# result = re.findall("\d+$",db,re.MULTILINE)
# print(result)

# 연습) T로 시작하는 이름만 출력
# r = re.findall("T[A-z]+",db,re.MULTILINE)
# print(r)

# 연습) T로 시작하지 않는 이름만 출력
r = re.findall('[A-SU-Z][A-z]+',db)
print(r)