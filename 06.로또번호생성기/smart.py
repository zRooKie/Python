'''
1. 특정 숫자를 포함해서 로또 번호를 생성해 주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해 주는 기능
3. 정해진 자릿수만큼 연속 숫자를 포함하는 번호를 생성해 주는 기능
'''

# pip install numpy
import numpy

def make_lotto_number(**kwargs): # 사용자의 옵션을 받는다.
    rand_number = numpy.random.choice(range(1, 46), 6, replace=False) # 1부터 46사이에 6자리 숫자를 중복되지 않게 만들어라.
    rand_number.sort()

    # 최종 로또 번호가 완성될 변수
    lotto = []

    if kwargs.get("include"):   # include라는 키워드가 넘어오면...
        include = kwargs.get("include")
        lotto.extend(include)

        cnt_make = 6 - len(lotto)
        for i in range(cnt_make):
            for j in rand_number:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)

    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude)) # lotto를 집합화 하고 exclude를 집합화 해서 차집합을 구해 리스트에 담는다.

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1, 46), 6, replace=False) 
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break

    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1)

        seq_num = []
        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []
        lotto.extend(seq_num)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1, 46), 6, replace=False) 
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break

                lotto = list(set(lotto))

    lotto.sort()
    return lotto

# print(make_lotto_number(include=[1, 2]))
# print(make_lotto_number(exclude=[11, 21]))
# print(make_lotto_number(continuty= 3))

count = int(input("로또 번호를 몇개 생성할까요? > "))

for j in range(count):
    print(make_lotto_number())



