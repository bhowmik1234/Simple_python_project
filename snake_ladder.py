import random


def snake(position):
    snakes = {31: 14, 41:20, 58:37, 67: 49, 84: 62, 92: 76, 99:4}
    if(position in snakes):
        return snakes[position]
    return 0

def ladder(position):
    ladders = {2: 23, 8:12, 29:54,32: 51, 39: 80, 70:89, 75:96 }
    if(position in ladders):
        return ladders[position]
    return 0

def dice():
    number = random.randint(1,6)
    return number

def play():
    first_player = input("Enter first player name: ")
    second_player = input("Enter second player name: ")

    pp1=0
    pp2=0
    chance = 1
    ch = 'y'
    
    while((pp1 <= 100 or pp2 <= 100) and ch == 'y'):
        print("\n")
        if (chance == 1):
            DICE = dice()
            print(f"{first_player} turns.")
            print(f"Dice throw was: ", DICE)
            pp1 += DICE
            if(ladder(pp1) != 0):
                pp1 = ladder(pp1)
            if(snake(pp2) != 0):
                pp2 = snake(pp2)
            if(pp1 >= 100):
                print(f"\n{first_player} wins.")
                break;
            chance = 2
            print(f"{first_player} score.", pp1)
            print(f"{second_player} score.", pp2)
            ch = input("Want to continue..")


        elif (chance == 2):
            DICE = dice()
            print(f"{second_player} turns.")
            print(f"Dice throw was: ", DICE)
            pp2 += DICE
            if(ladder(pp2) != 0):
                pp2 = ladder(pp2)
            if(snake(pp2) != 0):
                pp2 = snake(pp2)
            if(pp2 >= 100):
                print(f"\n{second_player} wins.")
                break;
            chance = 1
            print(f"{first_player} score. ", pp1)
            print(f"{second_player} score. ", pp2)
            ch = input("Want to continue..")

        
        




play()
# ladder(2)
