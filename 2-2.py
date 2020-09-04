from bs4 import BeautifulSoup
import requests
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = 'https://www.wishket.com/accounts/login'

ua = UserAgent()

with requests.Session() as s:
    s.get(URL)
    LOGIN_INFO = {
        'user_id': 'tlsdlf5',
        'user_pw': 'tlsdlf11',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome), 'Referer' : 'https://www.wishket.com/account/login/'})
    # print(response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)
        projectList = soup.select("body > div.gaia > div > div.mb60.container > div.content > div.right-side > div.mb16.user-info.user-info-partner > div.user-project")
        # print(projectList)
