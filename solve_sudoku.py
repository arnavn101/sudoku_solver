import random
from create_board import SudokuBoard
from check_sudoku import CheckSudoku

class SolveSudoku:
    def __init__(self, sudoku_board=SudokuBoard().board):
        self.sudoku_board = sudoku_board
        self.solveSudoku(self.sudoku_board)
        # print(self.printSudoku())

    def return_matrix(self):
        return self.sudoku_board

    def solveSudoku(self, sudoku_matrix):
        find_empty = self.find_empty(sudoku_matrix)
        if not find_empty:
            return True
        else:
            row, col = find_empty
        for num in range(1, 10):
            if self.valid(sudoku_matrix, num, (row, col)):
                sudoku_matrix[row][col] = num
                if self.solveSudoku(sudoku_matrix):
                    return True
                sudoku_matrix[row][col] = 0
        return False

    def valid(self, bo, num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False
        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False
        return True

    def find_empty(self, board_matrix, n_squares=9):
        for row in range(n_squares):
            for col in range(n_squares):
                if board_matrix[row][col] == 0:
                    return row, col
        return False

    def printSudoku(self, n_squares=9):
        for row in range(n_squares):
            for cols in range(n_squares):
                print(f"{self.sudoku_board[row][cols]}", end=" ")
            print("\n")

#SolveSudoku()
