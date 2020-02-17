import requests
from bs4 import BeautifulSoup
import re   # 정규식
import json
import random
import os

def get_news():
    url = "https://www.usatoday.com"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("div.gnt_m_th > a")

    for li in lists:
        href = url + li["href"]
        # print(href)

        r = requests.get(href)
        bs = BeautifulSoup(r.text, "lxml")
        texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")

        # # print(texts)
        # contents = []
        # for p in texts:
        #     contents.append(p.text)

        contents = [p.text for p in texts]
        contents = " ".join(contents)
        # print(contents)
        return contents.lower()
    return None

def naver_traslate(word):
    try:
        url = "https://ac.dict.naver.com/enkodict/ac?st=11001&q={}".format(word)
        r = requests.get(url)
        j = json.loads(r.text)
        # print(j["items"][0][0][1][0])
        return (j["items"][0][0][1][0])
    except:
        return None


def make_quiz(news):
    match_pattern = re.findall(r'\b[a-z]{4,15}\b', news) # a-z 까지 4자리 ~ 15자리 경계가 되는 단어를 news 에서 찾아내라
    # print(match_pattern)

    frequency = {}
    quize_list = []
    for word in match_pattern:
        # print(word)
        # print(word, frequency.get(word, 0))
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        # print(frequency[word])

    for word, count in frequency.items():
        # print(word, count)
        if count > 1:
            kor = naver_traslate(word)
            if kor is not None:
                quize_list.append({kor: word})

    return quize_list

def quize():
    quize_list = make_quiz(get_news())
    random.shuffle(quize_list)

    chance = 5
    count = 0

    for q in quize_list:
        os.system("cls")
        count += 1
        kor = list(q.keys())[0]
        english = q.get(kor)

        # print(kor, english)
        print("*" * 90)
        print("문제 : {}".format(kor))
        print("*" * 90)

        for j in range(chance):
            user_input = str(input("위의 뜻이 의미하는 단어를 입력하세요 > ")).strip().lower()

            if user_input == english:
                print("정답입니다!!! {} 문제 남음".format(len(quize_list) - count))
                os.system("pause")
                break
            else:
                n = chance - (j + 1)
                if j == 0:
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다.".format(user_input, n))
                elif j == 1:
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {} 로 시작".format(user_input, n, english[0]))
                elif j == 2:
                    hint = " _ " * int(len(english) - 2)
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {} {} {} 로 시작".format(user_input, n, english[0], english[1], hint))
                elif j == 3:
                    hint = " _ " * int(len(english) - 3)
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {} {} {} {} 로 시작".format(user_input, n, english[0], english[1], english[2], hint))
                else:
                    print("틀렸습니다. 정답은 {} 입니다.".format(english))
                    os.system("pause")

        print("더이상 문제가 없습니다.")

quize()