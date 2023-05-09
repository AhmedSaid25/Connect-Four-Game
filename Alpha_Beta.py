"""
  0 1 2 3 4 5 6
0
1
2
3
4
5

"""
def minimax(board, available, turn):
    valid = 0
    for i in range(0, 7):
        if available[i] != -1:
            valid += 1
    if valid == 0:
        return 1e9
    score = [0, 0, 0, 0, 0, 0, 0]
    score = giveAllScores(board, score)
    if checkFour(board):
        if turn:
            return 1
        else:
            return 0
    if turn:
        mx = -1e9
        taken = -1
        for i in range(0, 7):
            if score[i] > mx:
                mx = score[i]
                taken = i
        board[taken][available[taken]] = 'O'
        available[taken] -= 1
        minimax(board, available, 1 - turn)
    else:
        # random a col for
        mx = 1e9
        taken = -1
        for i in range(0, 7):
            if score[i] < mx:
                mx = score[i]
                taken = i
        board[taken][available[taken]] = 'X'
        available[taken] -= 1
        minimax(board, available, 1 - turn)


def giveAllScores(board, vector):
    for element in range(0,7):
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
    hor = countHorizontal(board,i,j)
    ver = countVertical(board,i,j)
    d1 = mainDiagonal(board,i,j)
    d2 = otherDiagonal(board,i,j)
    freqArr[hor] += 1
    freqArr[ver] += 1
    freqArr[d1] += 1
    freqArr[d2] += 1
    # score = freqArr[4] + freqArr[3] + freqArr[2] + freqArr[1]
    score = freqArr[4]*99999 + freqArr[3]*999 + freqArr[2]*99 + freqArr[1]*9
    return score


