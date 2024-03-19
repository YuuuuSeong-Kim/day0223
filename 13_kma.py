import requests
import re

url = "http://devweather.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

text = requests.get(url).text
#
# title = re.findall('<title>(.+)</title>',text)
# print(title)
#
# for row in title:
#     print(row)


# re.DOTALL ==> 찾고자 하는 시작, 마지막 패턴이 여러줄에 걸쳐 있다.
#  .+   ==> 탐욕적
#  .+?  ==> 비탐욕적

# list = re.findall('<location wl_ver="3">(.+)</location>',text, re.DOTALL)
# print(len(list))  <== 1개 나옴

list = re.findall('<location wl_ver="3">(.+?)</location>',text, re.DOTALL)
# print(list)

# 연습) 모든 도시명 추출하여 출력
# city = re.findall("<city>(.+?)</city>", text , re.DOTALL)
# print(city)
'''
<tmEf>2024-02-26 00:00</tmEf>
<wf>맑음</wf>
<tmn>-1</tmn>
<tmx>8</tmx>
'''
f = open('./Data/hello.txt','w',encoding='utf-8')
for row in list:
    city = re.findall("<city>(.+)</city>", row)
    data = re.findall("<data>(.+?)</data>",row,re.DOTALL)
    print(city)
    f.write(city[0]+"\n")
    for d in data:
        tmEf = re.findall("<tmEf>(.+)</tmEf>",d)
        wf = re.findall("<wf>(.+)</wf>",d)
        tmn = re.findall("<tmn>(.+)</tmn>",d)
        tmx = re.findall("<tmx>(.+)</tmx>",d)
        print(tmEf,wf,tmn,tmx)
        f.write("tmEf : "+tmEf[0]+" wf : "+wf[0]+" tmn : "+tmn[0]+" tmx : "+tmx[0]+"\n")
    print("-"*50)
    f.write("-"*50+"\n")
f.close()
print("파일을 만들었습니다")