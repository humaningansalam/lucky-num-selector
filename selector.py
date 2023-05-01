import random

def get_lucky_num(attemp):
    

    for y in range(attemp):
        lotto = []
        for x in range(6):
            lotto.append(random.randint(1,45))
        print(lotto)


if __name__ =="__main__":
    attemp = int(input("몇번 시도하시겠습니까?"))
    random_select(attemp)

