def Min_max(board,depth,alpha,beta, maximizer):
    available=board.getAvailableColumns()

    #check winning or game is over ( base case )
    #return board score

    if(maximizer):
        mx = -math.inf
        col = 4
        for i in available :
            # get first valid row in every column
            b_copy = board.copy()

            # set this place in b_copy and look at the score


            new_score = Min_max(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > mx:
                mx = new_score
                col = i
            alpha = max(alpha, mx)
            if alpha >= beta:
                break
        return col,mx

    else:
        mn = math.inf
        col = 4
        for i in available :
            # get first valid row in every column
            b_copy = board.copy()

            # set this place in b_copy and look at the score


            new_score = Min_max(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < mn:
                mx = new_score
                col = i
            alpha = min(alpha, mn)
            if alpha >= beta:
                break
        return col,mn