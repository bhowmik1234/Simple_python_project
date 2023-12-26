import random

def play():
    global ACCOUNT
    bet_number = random.randint(1, 10)
    lucky_number = random.randint(1, 10)

    print("Ber Number: ", bet_number)
    print("Lottey Number: ", lucky_number)
    if(bet_number == lucky_number):
        ACCOUNT = ACCOUNT + 900 - 100
    else:
        ACCOUNT = ACCOUNT - 100

    print("Amount you won ", ACCOUNT)
    print("\n")


ACCOUNT = 0
for i in range(10):
    play()