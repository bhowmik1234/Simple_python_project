t = ['-', '-', '-',
     '-', '-', '-',
     '-', '-', '-'
     ]

first_player = input('enter the first player name : ')
second_player = input('enter the second player name : ')
name = first_player
print('first player always use X.')


def board():
    print(t[0], " | ", t[1], " | ", t[2], )
    print(t[3], " | ", t[4], " | ", t[5], )
    print(t[6], " | ", t[7], " | ", t[8], )


board()

current_player = 'X'
valid = False
while not valid:
    print()
    print()
    print(name, 'turns . ', 'Use', current_player)
    print('Enter the position from 1 to 9 ')
    position = input('enter the position : ')

    while position not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Invalid position')
        position = input('enter the position : ')
        print()

    position = int(position) - 1
    if t[position] == '-':
        t[position] = current_player
    else:
        while t[position] != '-':
            print('position is been used')
            position = input('enter the position : ')
            print()
            valid = False
            position = int(position) - 1
        if t[position] == '-':
            t[position] = current_player

    board()

    if t[0] == t[1] == t[2] == 'X' or t[0] == t[1] == t[2] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[3] == t[4] == t[5] == 'X' or t[3] == t[4] == t[5] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[6] == t[7] == t[8] == 'X' or t[6] == t[7] == t[8] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[0] == t[3] == t[6] == 'X' or t[0] == t[3] == t[6] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[1] == t[4] == t[7] == 'X' or t[1] == t[4] == t[7] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[2] == t[5] == t[8] == 'X' or t[2] == t[5] == t[8] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[0] == t[4] == t[8] == 'X' or t[0] == t[4] == t[8] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    elif t[2] == t[4] == t[6] == 'X' or t[2] == t[4] == t[6] == 'O':
        if(current_player == 'X'):
            print(f"{first_player} win.")
        else:
            print(f"{second_player} win.")
        valid = True
    else:
        if '-' in t:
            if current_player == 'X':
                current_player = 'O'
                name = second_player
                valid = False

            else:
                current_player = 'X'
                name = first_player
                valid = False

        else:
            print('match is tie .')
            break
