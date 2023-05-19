from Minimax import *
from tkinter import *
import numpy as np
import pygame
import sys
import random
import copy
Grid = [[0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 0, 0, 0, 0, 0],  # 2
        [0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0]  # 5
       ]
def terminate(window):
    window.destroy()
    sys.exit()
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

def ConnectFour(chosen_algorithm,chosen_level):

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
                if board[r][c] == 2:
                    pygame.draw.circle(screen, RED, (int(c * squareSize + squareSize / 2), height - int(r * squareSize + squareSize / 2)), radius)
                elif board[r][c] == 1:
                    pygame.draw.circle(screen, YELLOW, (int(c * squareSize + squareSize / 2), height - int(r * squareSize + squareSize / 2)), radius)
        pygame.display.update()


    def drawBoard(board):
        for c in range(column):
            for r in range(row):
                pygame.draw.rect(screen, BLUE, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
                pygame.draw.circle(screen, BLACK, ( int(c * squareSize + squareSize / 2), int(r * squareSize + squareSize + squareSize / 2)), radius)
    board = Grid
    #printBoard(board)
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

    algo_agent=1
    depth_agent=3
    if(chosen_algorithm=="Minimax"):
        algo_agent=2
        depth_agent=4
    else:
        algo_agent=1
        depth_agent=5

    computer_level = 1
    if(chosen_level=="Easy"):
        computer_level=1
    elif(chosen_level=="Intermediate"):
        computer_level=2
    elif(chosen_level=="Hard"):
        computer_level=3
    else :
        computer_level=4
    cnt = 0
    game_end = False

    #  print(getScore(board))
    while not game_end:
        print(board)
        ## shar7 el function :
        ##do_move(algorithm, depth, board, player1, player2)
        ## 1-> alpha beta, 2-> minimax
       # print("hour btswt ")
        do_move(algo_agent,depth_agent,board, 1,2)
        if Win(board,1):
            font = pygame.font.Font(None, 75)
            WinningAgent = font.render("Agent Wins !", True, YELLOW)
            text_rect = WinningAgent.get_rect(center=(width/2, height*1/10))
            screen.blit(WinningAgent, text_rect)
            game_end = True
            print_grid(board)
            new_board = reverseCopy(board)
            PlayTime_board(new_board)
            pygame.display.update()
            break
        if getAvailableColumns(board) == []:
            font = pygame.font.Font(None, 75)
            TieText = font.render("Tie Game!", True, BLUE)
            text_rect = TieText.get_rect(center=(width / 2, height * 1 / 10))
            screen.blit(TieText, text_rect)
            game_end = True
            print_grid(board)
            new_board = reverseCopy(board)
            PlayTime_board(new_board)
            pygame.display.update()
            break
        new_board = reverseCopy(board)
        PlayTime_board(new_board)
        pygame.display.update()
        if(computer_level==1):
            random_column = random.randint(0, 6)
            set_cell(board, 2, random_column)
        elif(computer_level==2):
            do_move(2,computer_level,board, 2, 1)
        else :
            do_move(algo_agent, depth_agent, board, 2, 1)


        if Win(board,2):
            font = pygame.font.Font(None, 75)
            WinningComputer = font.render("Computer wins !", True, RED)
            text_rect = WinningComputer.get_rect(center=(width / 2, height * 1 / 10))
            screen.blit(WinningComputer, text_rect)
            game_end = True
            print_grid(board)
            new_board = reverseCopy(board)
            PlayTime_board(new_board)
            pygame.display.update()
            break
        if getAvailableColumns(board) == []:
            font = pygame.font.Font(None, 75)
            TieText = font.render("Tie Game!", True, BLUE)
            text_rect = TieText.get_rect(center=(width / 2, height * 1 / 10))
            screen.blit(TieText, text_rect)
            game_end = True
            print_grid(board)
            new_board = reverseCopy(board)
            PlayTime_board(new_board)
            pygame.display.update()
            break
        new_board = reverseCopy(board)
        PlayTime_board(new_board)
        pygame.display.update()
        print_grid(board)
        #time.sleep(2)



def menu(board):
    window = Tk(className='Connect 4')
    window.geometry("400x400")
    header = Label(window, text="Connect 4")
    header.config(font=("Courier", 30))
    header.pack()

    Algorithm = {"Alphabeta": "1",
                 "Minimax": "2"}
    hardness = {"Easy": "1",
                "Intermediate": "2",
                "Advanced" : "4"
                }
    v = StringVar(window, Algorithm["Alphabeta"])
    u = StringVar(window, hardness["Easy"])
    algo = Label(window, text="Choose Algorithm")
    algo.config(font=("Courier", 15))
    algo.pack()

    for (i, value) in Algorithm.items():
        Radiobutton(window, text=i, variable=v, value=value).pack(side=TOP, ipady=5)
    level = Label(window, text="Choose Level")
    level.config(font=("Courier", 15))
    level.pack()
    for (j, value) in hardness.items():
        Radiobutton(window, text=j, variable=u, value=value).pack(side=TOP, ipady=5)

    Playbutton = Button(window, text='play', bd='7', command=lambda: ConnectFour(list(Algorithm.keys())[int(v.get()) - 1], list(hardness.keys())[int(u.get()) - 1]))
    Playbutton.pack()
    window.mainloop()
    window.protocol('WM_DELETE_WINDOW', terminate(window))



if __name__ == '__main__':
    menu(Grid)
    #play(Board)
