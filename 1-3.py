from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="C:\\imagedown\\"
base = "https://www.naver.com/"
# quote = rep.quote_plus("추천-강좌")
quote = ""
url = base

res = req.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("iframe#da_iframe_time")
# print(recommand)

for i,e in enumerate(recommand,1):
    soup2 = BeautifulSoup(req.urlopen(e.get('data-iframe-src')).read(),"html.parser")
    # print(soup2.find_all())
    for link in soup2.find_all('script'):
        pattern = re.compile(r'\/(\w+\.(?:jpg|png))')
        mc = pattern.findall(str(link))
        print(mc)

    # print(i,e.get('data-iframe-src'))



try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


# for i,e in enumerate(recommand,1):
#     with open(savePath+"title_"+str(i)+".txt", "wt") as f:
#         f.write(e.select_one("h4.block_title > a ").string)
#     fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
#     req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)

print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")
