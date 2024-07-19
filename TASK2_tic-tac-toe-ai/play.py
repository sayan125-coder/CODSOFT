def insert(letter, position):
    if freeSpace(position):
        board[position] = letter
        printboard(board)
        if (draw()):
            print("DRAW!")
            exit()
        if botwins():
            print("BOT WINS!") 
            exit()
        if playerwins():
            print("PLAYER WINS")
            exit()
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insert(letter, position)
        return



def printboard(board):
    print(" |"+board[1]+"|"+board[2]+"|"+board[3]+"|")
    print("---------")
    print(" |"+board[4]+"|"+board[5]+"|"+board[6]+"|")
    print("---------")
    print(" |"+board[7]+"|"+board[8]+"|"+board[9]+"|")

def draw():
    for key in board.keys():
        if(key==''):
            return True
    return False

def playerwins():
    if (board[1] == board[2] and board[1] == board[3] and board[1] == 'X'):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == 'X'):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == 'X'):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == 'X'):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == 'X'):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == 'X'):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == 'X'):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == 'X'):
        return True
    else:
        return False
    

def botwins():
    if (board[1] == board[2] and board[1] == board[3] and board[1] == 'O'):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == 'O'):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == 'O'):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == 'O'):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == 'O'):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == 'O'):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == 'O'):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == 'O'):
        return True
    else:
        return False

def freeSpace(position):
    if board[position] == ' ':
        return True
    else:
        return False
    
def playerMove():
    position = int(input("Enter the position for 'X':  "))
    insert(user, position)
    return


def botMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insert(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    if (botwins()):
        return 1
    elif (playerwins()):
        return -1
    elif (draw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = user
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore
print("THE TIC-TAC-TOE GAME IS RUNNING")
board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}
print("BOT STARTS FIRST")
print("The Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
user='X'
bot='O'
print("------GAME HAS BEGAN------")
while (True):
    print('\n')
    botMove()
    playerMove()
    printboard(board)
