

a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '

marked_list = []
game_end = False
xturn = True
oturn = False

def x_turn(m):
     global a1 
     m = input
     if m == 'a1':
          a1 = m


def o_turn(m):
     global a1 
     m = input
     if m == 'a1':
          a1 = m

def xchange_board(m):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,xturn,oturn,marked_list,board
    m = m.lower()
    if m in marked_list:
        print('Position taken')
        return False
    if m == 'a1':
        a1 = 'x'
        marked_list.append(m)
    elif m == 'a2':
        a2 = 'x'
        marked_list.append(m)
    elif m == 'a3':
        a3 = 'x'
        marked_list.append(m)
    elif m == 'b1':
        b1 = 'x'
        marked_list.append(m)
    elif m == 'b2':
        b2 = 'x'
        marked_list.append(m)
    elif m == 'b3':
        b3 = 'x'
        marked_list.append(m)
    elif m == 'c1':
        c1 = 'x'
        marked_list.append(m)
    elif m == 'c2':
        c2 = 'x'
        marked_list.append(m)
    elif m == 'c3':
        c3 = 'x'
        marked_list.append(m)
    else:
        print('Invalid move')
        return False
    xturn = False
    oturn = True
    return True




def ochange_board(m):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,xturn,oturn,marked_list,board
    m = m.lower()
    if m in marked_list:
        print('Position taken')
        return False
    if m == 'a1':
        a1 = 'o'
        marked_list.append(m)
    elif m == 'a2':
        a2 = 'o'
        marked_list.append(m)
    elif m == 'a3':
        a3 = 'o'
        marked_list.append(m)
    elif m == 'b1':
        b1 = 'o'
        marked_list.append(m)
    elif m == 'b2':
        b2 = 'o'
        marked_list.append(m)
    elif m == 'b3':
        b3 = 'o'
        marked_list.append(m)
    elif m == 'c1':
        c1 = 'o'
        marked_list.append(m)
    elif m == 'c2':
        c2 = 'o'
        marked_list.append(m)
    elif m == 'c3':
        c3 = 'o'
        marked_list.append(m)
    else:
        print('Invalid move')
        return False
    oturn = False
    xturn = True
    return True

board = f'a |{a1}|{a2}|{a3}|\nb |{b1}|{b2}|{b3}|\nc |{c1}|{c2}|{c3}|\n   1 2 3'


def check_winner():

    lines = [
        (a1, a2, a3),
        (b1, b2, b3),
        (c1, c2, c3),
        (a1, b1, c1),
        (a2, b2, c2),
        (a3, b3, c3),
        (a1, b2, c3),
        (c1, b2, a3),
    ]
    for wins in lines:
        if wins[0] == wins[1] == wins[2] and wins[0] in ('x', 'o'):
            return wins[0].upper()  
    return None




while game_end == False:
    
    while xturn == True and not game_end:
        print(board)
        m = input('X turn: ')
        if xchange_board(m):
            print(board)
            winner = check_winner()
            if winner:
                print(f'{winner} wins!')
                game_end = True
                break
            # check for draw
            if len(marked_list) >= 9:
                print('Draw!')
                game_end = True
                break
            break  # valid move made, exit to O's turn

    if game_end:
        break

    while oturn == True and not game_end:
        m = input('O turn: ')
        if ochange_board(m):
            print(board)
            winner = check_winner()
            if winner:
                print(f'{winner} wins!')
                game_end = True
                break
            # check for draw
            if len(marked_list) >= 9:
                print('Draw!')
                game_end = True
                break
            break  # valid move made, exit to X's turn


# print x at o turns
# print yung nilagyan ng user
# check winner at draw
