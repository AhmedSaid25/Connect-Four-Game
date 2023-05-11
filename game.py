from board import Board
import time
import random
from Minimax import *
# GAME LINK
# http://kevinshannon.com/connect4/

def main():
    board = Board()

    # board.set_cell('O',1)
    # board.set_cell('X',2)
    # board.set_cell('O', 3)
    # board.set_cell('O', 4)
    # board.set_cell('X', 1)
    # board.set_cell('X', 2)
    # board.set_cell('X', 3)
    # board.set_cell('O', 2)

    # available = [5,3,2,3,4,5,5]
    # new = board.giveAllScores(board, available)
    columns = board.getAvailableColumns()
    print(columns)
    board.print_grid()

    #testing some code
    #testboard = [[],[],[],[],[],[]]

    # normal code
    time.sleep(2)
    game_end = False
    board.print_grid()
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        #board.print_grid(game_board)
        # YOUR CODE GOES HERE
        bestColumn, score = Minimax(board,4,True)
        board.select_column(bestColumn)
        board.set_cell('O', bestColumn)
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column = random.randint(0, 6)
        board.select_column(random_column)
        board.set_cell('X', random_column)
        board.print_grid()

        time.sleep(2)



if __name__ == "__main__":
    main()
