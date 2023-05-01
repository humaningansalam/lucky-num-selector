import random

def random_select():
    lotto = []
    for x in range(6):
        lotto.append(random.randint(1,45))
    print(lotto)


if __name__ =="__main__":
    
    random_select()

