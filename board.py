from PIL import ImageGrab
import pyautogui
from Minimax import *
# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 570
TOP = 200
RIGHT = 1350
BOTTOM = 875

EMPTY = '_'
RED = 1
BLUE = 2


class Board:

    def __init__(self) :
        self.board = [[EMPTY for i in range(7)] for j in range(6)]

    def getBoard(self):
        newBoard = []
        for i in range(0,7):
            for j in range (0,6):
                newBoard[i][j] = self.board[i][j]
    def valid_move(self,col):
            if(self.board[0][col]=='_'):return True
            else : return False

    def set_cell(self,player,j):
        i = self.getFirstFreeRow(j)
        self.board[i][j]=player



    def print_grid(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == EMPTY:
                    print("_", end=" \t")
                elif self.board[i][j] == 'O':
                    print("O", end=" \t")
                elif self.board[i][j] == 'X':
                    print("X", end=" \t")
            print("\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 115
                y = startCord[1] + j * 112
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage


    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        if self.opWin():
            return True
        if self.iWin():
            return True

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][0] + LEFT,
            self._get_grid_cordinates()[column][1] + TOP,
        )

    def getAvailableColumns(self):
        columns = []
        for j in range (0,7):
            if self.board[0][j] == EMPTY:
                columns.append(j)
        return columns

    def getFirstFreeRow(self, j):
        i = 5
        while i>=0 :
            if self.board[i][j] == EMPTY  :
                break
            i-=1
        return i


    # functions to see if opponent won
    def HorizontalWon(self, board, i, j, Op):
        flag = True
        counter = 0
        while counter < 4:
            if board[i][j] != Op:
                flag = False
                break
            counter += 1
            j += 1
        return flag

    def VerticalWon(self, board, i, j, Op):
        flag = True
        counter = 0
        while counter < 4:
            if board[i][j] != Op:
                flag = False
                break
            counter += 1
            i += 1
        return flag

    # this diagonal \
    def MainDiagonalWon(self, board, i, j, Op):
        flag = True
        counter = 0
        while counter < 4:
            if board[i][j] != Op:
                flag = False
                break
            counter += 1
            j += 1
            i += 1
        return flag

    def OtherDiagonalWon(self, board, i, j, Op):
        flag = True
        counter = 0
        while counter < 4:
            if board[i][j] != Op:
                flag = False
                break
            counter += 1
            j += 1
            i -= 1
        return flag

    def iWin(self):
        return self.Win('X')
    def opWin(self):
        return self.Win('O')


    def Win(self, symbol):
        i = 0
        j = 0
        # checking for horizontal win
        for i in range(0, 6):
            for j in range(0, 4):
                if (self.HorizontalWon(self.board, i, j, symbol)):
                    return True
        # checking for vertical win
        for j in range(0, 7):
            for i in range(0, 3):
                if (self.VerticalWon(self.board, i, j, symbol)):
                    return True
        # checking for main diagonal win
        for i in range(0, 3):
            for j in range(0, 4):
                if (self.MainDiagonalWon(self.board, i, j, symbol)):
                    return True

        # checking for other diagonal win
        for i in range(0, 3):
            for j in range(3, 7):
                if (self.OtherDiagonalWon(self.board, i, j, symbol)):
                    return True

        return False;

    def giveAllScores(self, vector):
        for element in range(0, len(vector)):
            if vector[element] == -1:
                continue
            vector[element] = self.giveScore(self.board, vector[element], element)
        return vector

    def countVertical(self, i, j):
        acc = 0
        i -= 1
        while (i > 0 and j > 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            i += 1
        return acc + 1

    def countHorizontal(self,i, j):
        acc = 0
        tmp = j
        j -= 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j -= 1
        j = tmp + 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j += 1
        return acc + 1

    # this / diagonal
    def mainDiagonal(self, i, j):
        acc = 0
        tmpj = j
        tmpi = i
        j += 1
        i -= 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j += 1
            i -= 1
        j = tmpi - 1
        i = tmpj + 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j -= 1
            i += 1
        return acc + 1

    # this diagonal \
    def otherDiagonal(self, i, j):
        acc = 0
        tmpj = j
        tmpi = i
        j -= 1
        i -= 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j -= 1
            i -= 1
        j = tmpi + 1
        i = tmpj + 1
        while (i >= 0 and j >= 0 and i < 6 and j < 7 and self.board[i][j] == 'O'):
            acc += 1
            j += 1
            i += 1
        return acc + 1

    def giveScore(self, i, j):
        fours = 0
        threes = 0
        twos = 0
        ones = 0
        freqArr = [0, 0, 0, 0, 0]
        hor = self.countHorizontal(i, j)
        ver = self.countVertical(i, j)
        d1 = self.mainDiagonal(i, j)
        d2 = self.otherDiagonal(i, j)
        freqArr[hor] += 1
        freqArr[ver] += 1
        freqArr[d1] += 1
        freqArr[d2] += 1
        # score = freqArr[4] + freqArr[3] + freqArr[2] + freqArr[1]
        score = freqArr[4] * 9999999 + freqArr[3] * 999 + freqArr[2] * 99 + freqArr[1] * 9
        if self.opWin():
            score = -999999999999
        return score


    def getBoardScore(self):
        if(self.opWin):
            return -9999999999999
        if(self.iWin):
            return 99999999999999
        else:
            sum = 0
            for i in range (0,7):
                for j in range (0,6):
                    if(self.board[i][j]=='X'):
                        sum += self.giveScore(i,j)

            return sum


