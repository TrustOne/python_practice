from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id': 'tlsdlf5',
    'user_pw': 'tlsdlf11'
}

#세션 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    #HTML 소스 확인
    # print('login_req',login_req.text)
    #Header확인
    # print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://bbs.ruliweb.com/community/board/300143/read/48637251?cate=497')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        article = soup.select_one("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p:nth-child(6)")
        print(article)

        for i in article:
            if i.string is not None:
                print(i.string)
