"""
  0 1 2 3 4 5 6
0
1
2
3
4
5

"""

import math

# GEEKS FOR GEEKS
# def minimax(curDepth, nodeIndex,maxTurn, scores,targetDepth):
#     # base case : targetDepth reached
#     if (curDepth == targetDepth):
#         return scores[nodeIndex]
#
#     if (maxTurn):
#         return max(minimax(curDepth + 1, nodeIndex * 2,
#                            False, scores, targetDepth),
#                    minimax(curDepth + 1, nodeIndex * 2 + 1,
#                            False, scores, targetDepth))
#
#     else:
#         return min(minimax(curDepth + 1, nodeIndex * 2,
#                            True, scores, targetDepth),
#                    minimax(curDepth + 1, nodeIndex * 2 + 1,
#                            True, scores, targetDepth))


def Minimax(board, currentDepth, max, maxDepth):
    columns = board.getAvailableColumns()
    gameEnd = board._check_if_game_end(board.board)

    if(gameEnd or currentDepth ==0):

    # the maximizing agent
    if(max):
        curr = -9999999
        position = 0
        for c in columns:
            boardCopy = board.copy
            board.set_cell(c)
            newScore = Minimax(boardCopy, currentDepth-1, False)
            if newScore > curr:
                curr = newScore
                position = c
        return position, curr

    # the minimizing agent
    else:
        curr = 999999999
        position = 0 # try to make it random
        for c in columns:
            boardCopy = board.copy
            board.set_cell(c)
            newScore = Minimax(boardCopy, currentDepth-1, True)
            if newScore < curr:
                curr = newScore
                position = c
        return position, curr









def giveAllScores(board, vector):
    for element in range(0,len(vector)):
        if vector[element] == -1:
            continue
        vector[element] = giveScore(board, vector[element], element)
    return vector
def countVertical(board, i,j):
    acc = 0
    i-=1
    while(i>0 and j>0 and i<6 and j<7 and board[i][j]=='O'):
        acc+=1
        i+=1
    return acc +1

def countHorizontal(board, i,j):
    acc = 0
    tmp = j
    j-=1
    while(i>=0 and j>=0 and i<6 and j<7 and board[i][j]=='O'):
        acc+=1
        j-=1
    j = tmp+1
    while ( i>=0 and j>=0 and i<6 and j<7 and board[i][j] == 'O'):
        acc += 1
        j += 1
    return acc+1
# this / diagonal
def mainDiagonal(board, i,j):
    acc = 0
    tmpj = j
    tmpi = i
    j+=1
    i-=1
    while(i>=0 and j>=0 and i<6 and j<7 and board[i][j]=='O'):
        acc+=1
        j+=1
        i-=1
    j = tmpi -1
    i = tmpj +1
    while (i>=0 and j>=0 and i<6 and j<7 and board[i][j] == 'O'):
        acc += 1
        j -= 1
        i +=1
    return acc+1

#this diagonal \
def otherDiagonal(board, i,j):
    acc = 0
    tmpj = j
    tmpi = i
    j-=1
    i-=1
    while( i>=0 and j>=0 and i<6 and j<7 and board[i][j]=='O'):
        acc+=1
        j-=1
        i-=1
    j = tmpi +1
    i = tmpj +1
    while (i>=0 and j>=0 and i<6 and j<7 and board[i][j] == 'O'):
        acc += 1
        j += 1
        i +=1
    return acc+1

def giveScore(board, i, j):
    fours=0
    threes=0
    twos=0
    ones=0
    freqArr = [0,0,0,0,0]
    hor = countHorizontal(board.board,i,j)
    ver = countVertical(board.board,i,j)
    d1 = mainDiagonal(board.board,i,j)
    d2 = otherDiagonal(board.board,i,j)
    freqArr[hor] += 1
    freqArr[ver] += 1
    freqArr[d1] += 1
    freqArr[d2] += 1
    # score = freqArr[4] + freqArr[3] + freqArr[2] + freqArr[1]
    score = freqArr[4]*9999999 + freqArr[3]*999 + freqArr[2]*99 + freqArr[1]*9
    if board.opWin():
        score = -999999999
    return score


