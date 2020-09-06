from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

savename = "g:/python/section2/python_practice/files/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

#파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml,'html.parser')
# print(soup)
#지역확인
info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all('tmn')
    # print(weather)

    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
# print(info.keys())

with open('g:/python/section2/python_practice/files/forecast.txt','wt') as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print("-",n)
            f.write('\t'+str(n)+'\n')
