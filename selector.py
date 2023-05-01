import random

def get_lucky_nums(attemp):
    

    for y in range(attemp):
        lotto = []
        for x in range(6):
            a = random.randint(1,45)
            while a in lotto:
                a = random.randint(1,45)
            lotto.append(a)
        print(lotto)


if __name__ =="__main__":
    attemp = int(input("몇번 시도하시겠습니까?"))
    get_lucky_nums(attemp)

