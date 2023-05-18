import time
import random
import math
import copy
import random
EMPTY = 0
RED = 1
BLUE = 2
#  0   1   2   3   4   5   6
# Grid = [[0, 0, 0, 0, 0, 0, 0],  # 0
#         [0, 0, 0, 0, 0, 0, 0],  # 1
#         [0, 2, 0, 0, 0, 0, 0],  # 2
#         [1, 1, 0, 2, 0, 0, 0],  # 3
#         [1, 1, 2, 2, 2, 0, 0],  # 4
#         [2, 1, 1, 1, 2, 0, 0]  # 5
#        ]

Grid = [[0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 0, 0, 0, 0, 0],  # 2
        [0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0]  # 5
       ]
Ai_player = RED
opo = BLUE


######## board change ##########
def set_cell(grid, player, j):
    i = getFirstFreeRow(grid, j)
    grid[i][j] = player


def getAvailableColumns(grid):
    columns = []
    for j in range(0, 7):
        if grid[0][j] == EMPTY:
            columns.append(j)
    return columns


def getFirstFreeRow(grid, j):
    i = 5
    while i >= 0:
        if grid[i][j] == EMPTY:
            break
        i -= 1
    return i


def check_if_game_end(grid):
    if Win(grid, 1):
        return True
    if Win(grid, 2):
        return True
    columns = getAvailableColumns(grid)
    if columns == []:
        return True
    return False


######## board change ##########


########### WIN PART  ##################
def HorizontalWon(board, i, j, Op):
    flag = True
    counter = 0
    while counter < 4:
        if board[i][j] != Op:
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


# def iWin(board,player,op):
#     return Win(board, player)
#
#
# def opWin(board):
#     return Win(board, op)


#########    END OF Win Part    ##################


########## MINMAX Algorithm   #########
## to be called when playing in board.py class
def chooseC (algorithm,depth,grid, Agent, Computer):
    if (algorithm ==1):
        best_column = makeAlphaBeta(depth, grid, Agent, Computer)
    else:
        best_column = makeMinimax(depth, grid, Agent, Computer)
    return best_column

## to be called when playing in GameGUI.py
def do_move(algorithm,depth,grid, Agent, Computer):
    if (algorithm ==1):
        best_column = makeAlphaBeta(depth, grid, Agent, Computer)
    else:
        best_column = makeMinimax(depth, grid, Agent, Computer)
    set_cell(grid, Agent, best_column)


def makeMinimax(depth,grid, Agent, Computer):

    #print_grid(grid)
    scores = []

    columns = getAvailableColumns(grid)
    #r = random.randint(0,len(columns))
    bestc = columns[0]
    bestscore = -math.inf
    for i in columns:
        boardCopy = copy.deepcopy(grid)
        set_cell(boardCopy, Agent, i)
        score = Minimax(Agent, Computer,boardCopy, depth,False)
        scores.append(score)
        if score>bestscore:
            bestscore = score
            bestc = i
    print(scores)
    return bestc


def Minimax(Agent, Computer, grid, currentDepth, maxim):
    columns = getAvailableColumns(grid)
    gameEnd = check_if_game_end(grid)
    if gameEnd or currentDepth == 0:
        # if gameEnd:
        #     if Win(grid, RED):
        #         return 10000000000000
        #     elif Win(grid, BLUE):
        #         return -10000000000000
        #     else:
        #         return 0
        #
        # else:
            score = getScore(grid, Agent, Computer)
            return score

    # the maximizing
    if (maxim):
        curr = -math.inf
        #bestc=3
        for c in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, Agent, c)
            newScore = Minimax(Agent, Computer, boardCopy, currentDepth - 1, False)
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
            set_cell(boardCopy, Computer, c)
            newScore = Minimax(Agent, Computer, boardCopy,currentDepth - 1, True)
            if newScore < curr:
                curr = newScore
                #bestc = c
        return curr


########## MINMAX Algorithm   #########



###### ALPHA BETA PRUNING ######
def makeAlphaBeta(depth,grid, Agent, Computer):
    #print_grid(grid)
    scores = []

    columns = getAvailableColumns(grid)
    #r = random.randint(0,len(columns))
    bestc = columns[0]
    bestscore = -math.inf
    for i in columns:
        boardCopy = copy.deepcopy(grid)
        set_cell(boardCopy, Agent, i)
        score = AlphaBeta(Agent, Computer,boardCopy, depth,False, -math.inf, math.inf)
        scores.append(score)
        if score>bestscore:
            bestscore = score
            bestc = i
    print(scores)
    return bestc


def AlphaBeta(Agent, Computer, grid, currentDepth, maxim, alpha, beta):
    columns = getAvailableColumns(grid)
    gameEnd = check_if_game_end(grid)
    if gameEnd or currentDepth == 0:
        score = getScore(grid, Agent, Computer)
        return score

    if maxim:
        curr = -math.inf
        for c in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, Agent, c)
            newScore = AlphaBeta(Agent, Computer, boardCopy, currentDepth - 1, False, alpha, beta)
            curr = max(curr, newScore)
            alpha = max(alpha, curr)
            if beta <= alpha:
                break
        return curr
    else:
        curr = math.inf
        for c in columns:
            boardCopy = copy.deepcopy(grid)
            set_cell(boardCopy, Computer, c)
            newScore = AlphaBeta(Agent, Computer, boardCopy, currentDepth - 1, True, alpha, beta)
            curr = min(curr, newScore)
            beta = min(beta, curr)
            if beta <= alpha:
                break
        return curr

######### get Score #########


def getScore(grid, player, op):
    myScore = getPlayerScore(grid, player, op)
    opScore = getPlayerScore(grid, op, player)
    score = 0
    if Win(grid, player):
        return math.inf  # Player wins
    elif Win(grid, op):
        return -math.inf # Oponent wins

    return myScore - opScore


def giveScore(player, op, grid, i, j):
    freqArr = [0, 0, 0, 0, 0]
    score = 0
    if (j == 3):
        score += 10
    hor = countHorizontal(grid, i, j, player)
    ver = countVertical(grid, i, j, player)
    d1 = mainDiagonal(grid, i, j, player)
    d2 = otherDiagonal(grid, i, j, player)
    freqArr[hor] += 1
    freqArr[ver] += 1
    freqArr[d1] += 1
    freqArr[d2] += 1
    #### same for oponent ####

    freqArrO = [0, 0, 0, 0, 0]
    horO = countHorizontal(grid, i, j, op)
    verO = countVertical(grid, i, j, op)
    d1O = mainDiagonal(grid, i, j, op)
    d2O = otherDiagonal(grid, i, j, op)
    freqArrO[horO] += 1
    freqArrO[verO] += 1
    freqArrO[d1O] += 1
    freqArrO[d2O] += 1
    score += freqArr[4] * 999999 + freqArr[3] * 5 + freqArr[2] * 2
    if freqArrO[4]>=1:
        score += 99999
    # el fo2 da kan tmm
    score += freqArrO[3] * 5 + freqArrO[2] * 2
    return score


def getPlayerScore(grid, player, op):
    score = 0
    if Win(grid, player):
        score -=10000
    if Win(grid,op):
        score += 1000000
    for i in range(0, 6):
        for j in range(0, 7):
            if (grid[i][j] == player):
                score += giveScore(player, op ,grid, i, j)
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





######### get Score #########


######## print grid #############
def print_grid(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            print(board[i][j], end=" ")
        print("\n")
    print("\n")


####### print grid #########

# Agent = 1
# Computer = 2
# def play(board):
#     cnt = 0
#     game_end = False
#
#     print_grid(board)
#     while not game_end:
#         ## first player
#         print("player 1 turn")
#         bestC = makeMinimax(board,1,2)
#         set_cell(board, 1, bestC)
#         if Win(board,1):
#             print("player 1 won")
#             game_end = True
#             print_grid(board)
#             break
#         print_grid(board)
#
#         ##second player
#         print("player 2 turn")
#         bestC = makeMinimax(board, 2, 1)
#         set_cell(board, 2, bestC)
#         if Win(board,2):
#             print("player 2 won")
#             game_end = True
#             print_grid(board)
#             break
#         print_grid(board)
#
# if __name__ == "__main__":
#     play(Grid)
