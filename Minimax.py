
import math
import copy

def makeMinimax (board, player):
    columns = board.getAvailableColumns()
    score = - math.inf
    bestc =0
    for c in columns:
        boardCopy = copy.deepcopy(board)
        boardCopy.set_cell(player, c)
        newscore = Minimax(boardCopy, 4, True)
        if newscore>score:
            score = newscore
            bestc = c
    return bestc

def Minimax(board, currentDepth, maxim):
    columns = board.getAvailableColumns()
    gameEnd = board._check_if_game_end(board.board)

    if(gameEnd or currentDepth ==0):
        if gameEnd:
            if board.iWin():
                return (10000000000000)
            elif board.opWin():
                return (-10000000000000)
            else:
                return (0)
        else:
            return ( board.getBoardScore()) #ha3melo now
        #return heuristic for the node

    # the maximizing agent
    if(maxim):
        curr = -math.inf
        column = 0
        for c in columns:
            boardCopy = copy.deepcopy(board)
            #boardCopy.board = board.getBoard()
            #boardCopy.set_cell('O',c)
            newScore = Minimax(boardCopy, currentDepth-1, False)
            if newScore > curr:
                curr = newScore
                column = c
        return curr
    # the minimizing agent
    else:
        curr = math.inf
        column = 0
        position = 0 # try to make it random
        for c in columns:
            # boardCopy = board.copy()
            boardCopy = copy.deepcopy(board)
            #boardCopy.board = board.getBoard()
            #boardCopy.set_cell('X',c)
            newScore = Minimax(boardCopy, currentDepth-1, True)
            if newScore < curr:
                curr = newScore
                column = c
        return curr
