import time
import random
import math
import copy

#  0   1   2   3   4   5   6
Board = [['_', '_', '_', '_', '_', '_', '_'],  # 0
         ['_', '_', '_', '_', '_', '_', '_'],  # 1
         ['_', '_', '_', '_', '_', '_', '_'],  # 2
         ['_', '_', '_', '_', '_', '_', '_'],  # 3
         ['_', '_', '_', '_', '_', '_', '_'],  # 4
         ['_', '_', '_', '_', '_', '_', '_']  # 5
         ]
Ai_player = 'O'
opo = 'X'


######## board change ##########
def set_cell(grid, player, j):
    i = getFirstFreeRow(grid, j)
    grid[i][j] = player


def getAvailableColumns(grid):
    columns = []
    for j in range(0, 7):
        if grid[0][j] == '_':
            columns.append(j)
    return columns


def getFirstFreeRow(grid, j):
    i = 5
    while i >= 0:
        if grid[i][j] == '_':
            break
        i -= 1
    return i


def check_if_game_end(grid):
    if Win(grid, 'O'):
        return True
    if Win(grid, 'X'):
        return True
    columns = getAvailableColumns(grid)
    if columns == []:
        return True
    return False


######## board change ##########


########### WIN PART  ##################
def HorizontalWon(Board, i, j, Op):
    flag = True
    counter = 0
    while counter < 4:
        if Board[i][j] != Op:
            flag = False
            break
        counter += 1
        j += 1
    return flag


def VerticalWon(board, i, j, Op):
    flag = True
    counter = 0
    while counter < 4:
        if board[i][j] != Op:
            flag = False
            break
        counter += 1
        i += 1
    return flag


def MainDiagonalWon(board, i, j, Op):
    flag = True
    counter = 0
    while counter < 4:
        if board[i][j] != Op:
            flag = False
            break
        counter += 1
        j += 1
        i += 1
    return flag


def OtherDiagonalWon(board, i, j, Op):
    flag = True
    counter = 0
    while counter < 4:
        if board[i][j] != Op:
            flag = False
            break
        counter += 1
        j += 1
        i -= 1
    return flag


def Win(board, symbol):
    # checking for horizontal win
    for i in range(0, 6):
        for j in range(0, 4):
            if HorizontalWon(board, i, j, symbol):
                return True
    # checking for vertical win
    for i in range(0, 3):
        for j in range(0, 7):
            if VerticalWon(board, i, j, symbol):
                return True
    # checking for main diagonal win
    for i in range(0, 3):
        for j in range(0, 4):
            if MainDiagonalWon(board, i, j, symbol):
                return True

    # checking for other diagonal win
    i = 5
    while i > 2:
        for j in range(0, 4):
            if OtherDiagonalWon(board, i, j, symbol):
                return True
        i -= 1

    return False


def iWin(board):
    return Win(board, 'O')


def opWin(board):
    return Win(board, 'X')


#########    END OF Win Part    ##################


########## MINMAX Algorithm   #########
def do_move(board, player):
    best_column = makeMinimax(board)
    set_cell(board, player, best_column)


def makeMinimax(grid):

    scores = []
    columns = getAvailableColumns(grid)
    for i in range(7):
        if i in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, 'O', i)
            score = Minimax(boardCopy, 4, False)
            scores.append(score)
        else:
            scores.append(-math.inf)
    print(scores)
    bestc = max(range(len(scores)), key=lambda i: scores[i])
    return bestc


def Minimax(grid, currentDepth, maxim):
    columns = getAvailableColumns(grid)
    gameEnd = check_if_game_end(grid)
    if gameEnd or currentDepth == 0:
        if gameEnd:
            if Win(grid, 'O'):
                return 10000000000000
            elif Win(grid, 'X'):
                return -10000000000000
            else:
                return 0
        else:
            score = getScore(grid)
            return score

    # the maximizing
    if (maxim):
        curr = -math.inf
        #bestc=3
        for c in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, 'O', c)
            newScore = Minimax(boardCopy, currentDepth - 1, False)
            if newScore > curr:
                curr = newScore
                #bestc =c
        return curr
    # the minimizing
    else:
        curr = math.inf
        #bestc = 3
        for c in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, 'X', c)
            newScore = Minimax(boardCopy, currentDepth - 1, True)
            if newScore < curr:
                curr = newScore
                #bestc = c
        return curr


########## MINMAX Algorithm   #########


######### get Score #########
def getScore(grid):
    if opWin(grid):
        return -99999999999999999
    elif iWin(grid):
        return 99999999999999999
    else:
        score = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if (grid[i][j] == 'O'):
                    score += giveScore(grid, i, j)


    return score


def countVertical(grid, i, j, player):
    acc = 0
    # if(grid[i][j]==player):
    #     acc+=1
    tmp=i-1
    i+=1
    while i >= 0 and j >= 0 and i < 6 and j < 7 and acc < 4 and grid[i][j] == player:
        acc += 1
        i += 1
    i=tmp
    while i >= 0 and j >= 0 and i < 6 and j < 7 and acc < 4 and grid[i][j] == player:
        acc += 1
        i -= 1
    if (acc >= 3):
        acc = 3
    return acc+1


def countHorizontal(grid, i, j,player):
    acc = 0
    tmp=j
    j-=1
    while i >= 0 and j >= 0 and i < 6 and j < 7 and grid[i][j] == player:
        acc += 1
        j -= 1
    j=tmp + 1
    while i >= 0 and j >= 0 and i < 6 and j < 7 and grid[i][j] == player:
        acc += 1
        j += 1
    if(acc>=3):
        acc=3
    return acc+1


def mainDiagonal(grid, i, j, player):
    acc = 0
    tmpj = j
    tmpi =i
    j+=1
    i-=1
    while(i>=0 and j>=0 and i<6 and j<7 and grid[i][j]==player):
        acc+=1
        j +=1
        i-=1
    j = tmpj -1
    i = tmpi + 1
    while (i >= 0 and j >= 0 and i < 6 and j < 7 and grid[i][j]==player):
        acc += 1
        j -= 1
        i += 1
    if (acc>=3):
        acc = 3
    return acc+1




def otherDiagonal(grid, i, j, player):
    acc = 0
    tmpj = j
    tmpi = i
    j -= 1
    i -= 1
    while (i >= 0 and j >= 0 and i < 6 and j < 7 and grid[i][j]==player):
        acc += 1
        j -= 1
        i -= 1
    j = tmpj + 1
    i = tmpi + 1
    while (i >= 0 and j >= 0 and i < 6 and j < 7 and grid[i][j]==player):
        acc += 1
        j += 1
        i += 1
    if (acc >= 3):
        acc = 3
    return acc + 1


def giveScore(grid, i, j):
    freqArr = [0, 0, 0, 0, 0]
    score=0
    if(j==3):
        score += 10
    hor = countHorizontal(grid, i, j, 'O')
    ver = countVertical(grid, i, j,'O')
    d1 = mainDiagonal(grid, i, j,'O')
    d2 = otherDiagonal(grid, i, j, 'O')
    freqArr[hor] += 1
    freqArr[ver] += 1
    freqArr[d1] += 1
    freqArr[d2] += 1
    #### same for oponent ####
    freqArrO = [0, 0, 0, 0, 0]
    horO = countHorizontal(grid, i, j, 'X')
    verO = countVertical(grid, i, j, 'X')
    d1O = mainDiagonal(grid, i, j, 'X')
    d2O = otherDiagonal(grid, i, j, 'X')
    freqArrO[horO] += 1
    freqArrO[verO] += 1
    freqArrO[d1O] += 1
    freqArrO[d2O] += 1
    #score = freqArr[4] + freqArr[3] + freqArr[2] + freqArr[1]
    score += freqArr[4] * 9999999 + freqArr[3] * 999 + freqArr[2] * 99 + freqArr[1] * 9
    if freqArrO[4]>=1:
        score += 9999999999999
    # score -= freqArrO[4] * 9999999 + freqArrO[3] * 999 + freqArrO[2] * 99 + freqArrO[1] * 9
    return score


######### get Score #########


######## print grid #############
def print_grid(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")


####### print grid #########


def play(board):
    cnt = 0
    game_end = False
  #  print(getScore(board))
    while not game_end:
        do_move(board, 'O')
        if iWin(board):
            print("agent win")
            game_end = True
            print_grid(board)
            break
        print_grid(board)

        random_column = random.randint(0, 6)
        set_cell(board, 'X', random_column)
        if opWin(board):
            print("computer win")
            game_end = True
            print_grid(board)
            break
        print_grid(board)


if __name__ == '__main__':
    play(Board)
