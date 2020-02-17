import requests
from bs4 import BeautifulSoup
import time
# pip install lxml

# 함수의 동작시간 확인
def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper

@time_function
def r_find_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li", {"class": "ah_item"})

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles

@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.select("li.ah_item")
    
    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles

url = "https://www.naver.com"
r_find_all(url, "html.parser")
r_select(url, "html.parser")

r_find_all(url, "lxml")
r_select(url, "lxml")


# r = requests.get("https://www.naver.com") 
# # bs = BeautifulSoup(r.text, "html.parser")
# bs = BeautifulSoup(r.text, "html.lxml") # 일반적으로 parser 보다 lxml 속도가 빠르다.

# # 1. find
# # lists = bs.find_all("li", {"class": "ah_item"})

# # for li in lists:
# #     title = li.find("span", {"class": "ah_k"}).text
# #     print(title)

# # 2. select
# # select 는 항상 list를 리턴한다.
# # li.클래스명, li#아이디 // li.a, li#b
# lists = bs.select("li.ah_item") 
# for li in lists:
#     title = li.select("span.ah_k")[0].text  # list 리턴하므로 [0]째 호출
#     print(title)

    