import requests
import telegram
from bs4 import BeautifulSoup
import time
# pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    now = time.localtime()
    now_date = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

    # zrookietestbot
    bot = telegram.Bot(token = "1087555363:AAHAOQxPvUCCOmARXKHUBiKO4-4ra7BmRyQ")

    # url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=11&theatercode=0109&date=20200207" # cgv현대 (대구)
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date={}".format(now_date)  # cgv용산아이파크
    # url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200207"  # cgv용산아이파크
    
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    imax = soup.select_one("span.imax")

    if(imax):
        imax = imax.find_parent("div", class_="col-times")
        title = imax.select_one("div.info-movie > a > strong").text.strip()
        # print(title + " IMAX가 열렸습니다.")
        # print("{} IMAX가 열렸습니다.".format(title))
        bot.sendMessage(chat_id=1005667850, text=title + " IMAX가 열렸습니다.")
        sched.pause()   # IMAX가 열리면 스케쥴러 중단
#    else:
#        # print("IMAX가 열리지 않았습니다.")
#        bot.sendMessage(chat_id=1005667850, text="IMAX가 아직 열리지 않았습니다.")


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)     # 30초 마다 알람
sched.start()