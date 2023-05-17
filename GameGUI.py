from Minimax import *
from tkinter import *
import numpy as np
import pygame
import random
import copy
def reverseCopy(board):
    column = 7
    row = 6
    new_board = []
    temp = []
    for r in range(row):
        for c in range(column):
            temp.append(board[r][c])
        new_board.insert(0,temp)
        temp=[]
    return new_board

def ConnectFour():
    RED=(255 ,0,0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    column = 7
    row = 6
    def createBoard():
        board = np.zeros((row, column))
        return board


    def printBoard(board):
        print(np.flip(board, 0))



    def PlayTime_board(board):
        for c in range(column):
            for r in range(row):
                if board[r][c] == 'X':
                    pygame.draw.circle(screen, RED, (int(c * squareSize + squareSize / 2), height - int(r * squareSize + squareSize / 2)), radius)
                elif board[r][c] == 'O':
                    pygame.draw.circle(screen, YELLOW, (int(c * squareSize + squareSize / 2), height - int(r * squareSize + squareSize / 2)), radius)
        pygame.display.update()


    def drawBoard(board):
        for c in range(column):
            for r in range(row):
                pygame.draw.rect(screen, BLUE, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
                pygame.draw.circle(screen, BLACK, ( int(c * squareSize + squareSize / 2), int(r * squareSize + squareSize + squareSize / 2)), radius)
    board = Board
    printBoard(board)
    GameOver = False
    pygame.init()
    squareSize = 100
    width = column * squareSize
    height = (row + 1) * squareSize

    size = (width, height)
    radius = int(squareSize / 2 - 5)
    screen = pygame.display.set_mode(size)
    drawBoard(board)
    pygame.display.update()

    Computer = 0
    AI= 1

    cnt = 0
    game_end = False
    #  print(getScore(board))
    while not game_end:
        do_move(board, 'O')
        if iWin(board):
            font = pygame.font.Font(None, 75)
            WinningAgent = font.render("Agent Wins !", True, YELLOW)
            text_rect = WinningAgent.get_rect(center=(width/2, height*1/10))
            screen.blit(WinningAgent, text_rect)
            game_end = True
            print_grid(board)

        new_board = reverseCopy(board)
        PlayTime_board(new_board)
        pygame.display.update()
        random_column = random.randint(0, 6)
        set_cell(board, 'X', random_column)
        if opWin(board):
            font = pygame.font.Font(None, 75)
            WinningComputer = font.render("Computer Wins !", True, RED)
            text_rect = WinningComputer.get_rect(center=(width / 2, height * 1 / 10))
            screen.blit(WinningComputer, text_rect)
            game_end = True
            print_grid(board)
        print_grid(board)


def menu(board):
    window = Tk(className='Connect 4')
    window.geometry("400x400")
    header = Label(window, text="Connect 4")
    header.config(font=("Courier", 30))
    header.pack()
    v = StringVar(window, "1")
    u = StringVar(window, "1")
    Algorithm = {"Alphabeta": "1",
                 "Minimax": "2"}
    hardness = {"Easy": "1",
                "Hard": "2"}
    algo = Label(window, text="Choose Algorithm")
    algo.config(font=("Courier", 15))
    algo.pack()

    for (i, Algorithm) in Algorithm.items():
        Radiobutton(window, text=i, variable=v,value=Algorithm).pack(side=TOP, ipady=5)
    level = Label(window, text="Choose Level")
    level.config(font=("Courier", 15))
    level.pack()
    for (j, hardness) in hardness.items():
        Radiobutton(window, text=j, variable=u, value=hardness).pack(side=TOP, ipady=5)

    Playbutton = Button(window, text='play', bd='7', command=ConnectFour)
    Playbutton.pack()
    window.mainloop()


if __name__ == '__main__':
    menu(Board)
    #play(Board)
