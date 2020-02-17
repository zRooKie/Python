import requests
from bs4 import BeautifulSoup
import time


def get_stock(stock_code):
    title_list = []

    url = "https://finance.naver.com/item/board.nhn?code={}".format(stock_code)    # 에이치엔티 : 176440
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    titles = bs.select("td.title > a")

    for t in titles:
        try:
            # print(t["title"]) # a tag 내 title 속성
            title = t["title"]
            href = "https://finance.naver.com/" + t["href"]
            title_list.append([title, href])
        except:
            continue

    return title_list


# results = get_stock("176440")
# for result in results:
#     print(result[1])


send_lists = []

def main():

    while True:
        results = get_stock("027740")
        if results is not None:
            for r in results:
                title, href = r
                if title not in send_lists:
                    msg = "{} {}".format(title, href)
                    print(msg)
                    send_lists.append(title)
        time.sleep(5) # 5초에 한번

main()