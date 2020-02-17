import requests
import time
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


def get_stock(stock_code):

    lists = []

    url = "https://finance.naver.com/item/board.nhn?code={}".format(stock_code)    # 에이치엔티 : 176440
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    top = bs.select("#content > div.section.inner_sub > table.type2 > tbody > tr:nth-child(3) > td.title > a")
    title = top[0]["title"]
    href = "https://finance.naver.com/" + top[0]["href"]
    lists.append([title, href])

    return lists


# print(get_stock("005930")) # 삼성전자

send_lists = []

def main():

    # zrookietestbot
    bot = telegram.Bot(token = "1087555363:AAHAOQxPvUCCOmARXKHUBiKO4-4ra7BmRyQ")


    while True:
        results = get_stock("176440")
        if results is not None:
            for r in results:
                title, href = r
                if title not in send_lists:
                    msg = "{} {}".format(title, href)
                    print(msg)

                    bot.sendMessage(chat_id=1005667850, text=msg)

                    send_lists.append(title)

main()

sched = BlockingScheduler()
sched.add_job(main, 'interval', seconds=10)
sched.start()