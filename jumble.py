# import random

# def r_word():
#     word = ["computer", "Notebook", "condition", "license", "chutar", "keyboard", "iomanip", "umbrella", "Micky"]
#     n = random.choice(word)
#     return n

# def jumble(word):
#     a = "".join(random.sample(word, len(word)))
#     return a

# def play():
#     player1 = input("Enter your Name. ")
#     player2 = input("Enter your Name. ")
#     pp1=0
#     pp2=0
#     turn=0
#     while(1):
#         w = r_word()
#         pick = jumble(w)
#         print(pick)

#         if(turn%2==0):
#             print("Player 1 turn.")
#             ans = input("What you think word will be. ")
#             if(ans==w):
#                 print("You gussed the correst word")
#                 pp1 += 1
#                 print(f"{player1} score", pp1)
#                 c = int(input("To play enter (1) or 0: "))
#                 if(c==0):
#                     break;

#             else:
#                 print("Better luck next time.")
#         else:
#             print("Player 2 turn.")
#             ans = input("What you think word will be. ")
#             if(ans==w):
#                 print("You gussed the correst word")
#                 pp2 += 1
#                 print(f"{player2} score", pp1)
#                 c = int(input("To play enter (1) or 0: "))
#                 if(c==0):
#                     break;
#             else:
#                 print("Better luck next time.")

#         turn += 1


# play()


# gussing the letter

import random

def r_word():
    word = ["computer", "notebook", "condition", "license", "keyboard", "iomanip", "umbrella", "micky"]
    n = random.choice(word)
    return n

def jumble(word):
    a = "".join(random.sample(word, len(word)))
    return a



def display_word(word, pos, wrd):
    w = ""
    for i in range(len(word)):
        if (i == pos):
            w = w + word[pos]
            print(word[pos], end="");
        else:
            w = w + wrd[i]
            print(wrd[i], end="");

    return w
    


def play():
    player1 = input("Enter your Name. ")
    player2 = input("Enter your Name. ")
    pp1=0
    pp2=0
    turn=0
    w = r_word()
    pos = -1
    wrd = ""
    for i in range(len(w)):
        wrd = wrd + "*"

    wrd = display_word(w, pos, wrd)
    while(1):
        if(turn%2==0):
            print(f"\n{player1} turn.")
            ans = input("What you think letter will be. ")
            if(ans in w):
                print("You gussed the correct letter.")
                pos = w.find(ans)
                if(ans in wrd):
                    for i in range(len(w)):
                        if(w[i] == ans and wrd[i] != ans):
                            pos = i
                            break
                wrd = display_word(w, pos, wrd)
                pos = 0
                pp1 += 1
                print(f"\n{player1} score", pp1)
                if('*' not in wrd):
                    print(f"{player1} score is {pp1}.\n")
                    print(f"{player2} score is {pp2}.\n")
                    break
                print("\n")
                c = int(input("To play enter (1) or (0): "))
                if(c==0):
                    break;
                else:
                    turn += 2
            
            else:
                turn += 1
                print("Better luck next time.")
        else:
            print(f"\n{player2} turn.")
            ans = input("What you think letter will be. ")
            if(ans in w):
                print("You gussed the correct letter")
                pos = w.find(ans)
                if(ans in wrd):
                    for i in range(len(w)):
                        if(w[i] == ans and wrd[i] != ans):
                            pos = i
                            break
                wrd = display_word(w, pos, wrd)
                pos = 0
                pp2 += 1
                print(f"\n{player2} score", pp2)
                if('*' not in wrd):
                    print("\n")
                    print(f"{player1} score is {pp1}.")
                    print(f"{player2} score is {pp2}.")
                    break
                print("\n")
                c = int(input("To play enter (1) or (0): "))
                if(c==0):
                    break;
                else:
                    turn += 2
            else:
                turn += 1
                print("Better luck next time.")

        

play()


