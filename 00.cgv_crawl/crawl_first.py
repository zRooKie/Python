import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=11&theatercode=0109&date=20200207"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
title_list = soup.select("div.info-movie")
for i in title_list:
    print(i.select_one("a > strong").text.strip())