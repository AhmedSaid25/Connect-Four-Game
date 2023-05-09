from board import Board
import time
import random
from Alpha_Beta import *
# GAME LINK
# http://kevinshannon.com/connect4/

def main():
    board = Board()

    board.set_cell('O', 5, 1)
    board.set_cell('X',5,2)
    board.set_cell('O', 5,3)
    board.set_cell('O', 5,4)
    board.set_cell('X', 4, 1)
    board.set_cell('X', 4, 2)
    board.set_cell('X', 4, 3)
    board.set_cell('O', 3, 2)

    available = [5,3,2,3,4,5,5]
    new = giveAllScores(board.board, available)
    print(new)
    board.print_grid()

    #testing some code
    #testboard = [[],[],[],[],[],[]]

    ## normal code
    # time.sleep(2)
    # game_end = False
    # board.print_grid()
    # while not game_end:
    #     (game_board, game_end) = board.get_game_grid()
    #
    #     # FOR DEBUG PURPOSES
    #     board.print_grid(game_board)
    #
    #     # YOUR CODE GOES HERE
    #
    #     # Insert here the action you want to perform based on the output of the algorithm
    #     # You can use the following function to select a column
    #     random_column = random.randint(0, 6)
    #     board.select_column(random_column)
    #
    #     time.sleep(2)
    #


if __name__ == "__main__":
    main()
