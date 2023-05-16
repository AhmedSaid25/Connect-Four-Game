from board import *
import time
import random
from Minimax import *
# GAME LINK
# http://kevinshannon.com/connect4/

def main():
    board = Board()

    #testing some code
    #testboard = [[],[],[],[],[],[]]

    # normal code
    time.sleep(2)
    game_end = False
    #board.print_grid(board.board)
    while not game_end:
        # FOR DEBUG PURPOSES
        #board.print_grid(game_board)
        # YOUR CODE GOES HERE
        #board.print_grid(game_board)


        (game_board, game_end) = board.get_game_grid()
        bestColumn = makeMinimax(game_board)
        board.print_grid (game_board)
        print("answer: ", bestColumn)
        board.select_column(bestColumn)


        #set_cell(myBoard,RED, bestColumn)
        #board.board=copy.deepcopy(myBoard)
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)
        # board.select_column(random_column)
        # set_cell(myBoard,'X', random_column)
        # board.board = copy.deepcopy(Board)
        #board.print_grid(board.board)

        time.sleep(2)




if __name__ == "__main__":
    main()