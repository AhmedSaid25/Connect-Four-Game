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


def Minimax(board, currentDepth, maxim):
    columns = board.getAvailableColumns()
    gameEnd = board._check_if_game_end(board.board)

    if(gameEnd or currentDepth ==0):
        if gameEnd:
            if board.iWin():
                return (None, 10000000000000)
            elif board.opWin():
                return (None, -10000000000000)
            else:
                return (None,0)
        else:
            return (None, board.getBoardScore()) #ha3melo now
        #return heuristic for the node

    # the maximizing agent
    if(maxim):
        curr = -math.inf
        column = 0
        for c in columns:
            boardCopy = board.copy()
            #boardCopy.board = board.getBoard()
            #boardCopy.set_cell('O',c)
            dummy, newScore = Minimax(boardCopy, currentDepth-1, False)
            if newScore > curr:
                curr = newScore
                column = c
        return column, curr
    # the minimizing agent
    else:
        curr = math.inf
        column = 0
        position = 0 # try to make it random
        for c in columns:
            boardCopy = board.copy()
            #boardCopy.board = board.getBoard()
            #boardCopy.set_cell('X',c)
            dummy, newScore = Minimax(boardCopy, currentDepth-1, True)
            if newScore < curr:
                curr = newScore
                column = c
        return column , curr





