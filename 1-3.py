from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io
import re
import time
from chrome import ChromeDriverObj
from naver_set import NaverImageCrwling
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="C:\\imagedown\\"
base = "https://www.naver.com/"
# quote = rep.quote_plus("추천-강좌")
quote = ""
url = base

class ImageGet:


    def __init__(self):

        self.config = NaverImageCrwling.get_information()
        self.chrome_driver = None
        self.cllct_time = time.strftime("%Y%m%d", time.localtime())

    def get_image_data(self):
        """
        :return:
        """
        if self.config["result"]:

            sess = req.Session()

            try:
                response = sess.get(url=self.config["data"]["hosts"])
            except req.exceptions.ConnectionError as err:
                print(err)
                sess.close()
            else:
                if response.status_code == 200 and response.ok:

                    self.chrome_driver = ChromeDriverObj.get_chrome_obj()
                    self.chrome_driver.get(url= self.config["data"]["hosts"])
                    self.chrome_driver.implicitly_wait(3)

                    ## iframe 처리 start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    """ 참고 블로그
                    https://dejavuqa.tistory.com/198
                    """
                    editor = self.chrome_driver.find_element_by_css_selector("iframe#da_iframe_time")
                    self.chrome_driver.switch_to.frame(editor)
                    response = self.chrome_driver.find_element_by_css_selector("div#addiv.ad > a#ac_banner_a > img")

                    try:
                        url = response.get_attribute("src")
                        print(url)
                    except:
                        pass
                    else:
                        self.image_download(url= url)

                    ## iframe 처리 end   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    self.chrome_driver.switch_to.default_content()

                    sess.close()
                    self.chrome_driver.close()

            finally:
                sess.close()

        else:
            print ("파일이 존재 하지 않는다.")

    def image_download(self, url):
        """
        참고 사이트 : https://www.it-swarm.dev/ko/python/python-url%EC%97%90%EC%84%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A0%80%EC%9E%A5/1053949951/
        :param url:
        :return:
        """
        # https ssl 처리
        context = ssl._create_unverified_context()

        try:

            html = urlopen(url, context=context)
        except:
            print ("request fail !!")
            pass
        else:

            with open("./result_image/naver_image_{}.jpg".format(self.cllct_time), "wb") as f:
                f.write(html.read())
                f.close()

            print ("image download success")


if __name__ == "__main__":
    image_object = ImageGet()
    image_object.get_image_data()

# res = req.urlopen(url).read()
#
# soup = BeautifulSoup(res,"html.parser")
#
# recommand = soup.select("iframe#da_iframe_time")
# print(recommand)

# for i,e in enumerate(recommand,1):
#     soup2 = BeautifulSoup(req.urlopen(e.get('data-iframe-src')).read(),"html.parser")
#     # print(soup2.find_all())
#     for link in soup2.find_all('script'):
#         pattern = re.compile(r'\/(\w+\.(?:jpg|png))')
#         mc = pattern.findall(str(link))
#         print(mc)

    # print(i,e.get('data-iframe-src'))



# try:
#     if not(os.path.isdir(savePath)):
#         os.makedirs(os.path.join(savePath))
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         print("Failed to create directory!!!!!")
#         raise


# for i,e in enumerate(recommand,1):
#     with open(savePath+"title_"+str(i)+".txt", "wt") as f:
#         f.write(e.select_one("h4.block_title > a ").string)
#     fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
#     req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)
