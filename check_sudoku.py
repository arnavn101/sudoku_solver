
class CheckSudoku:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.preDefined = []

    def check_board(self):
        if self.checkRows() and self.checkCols() and self.checkBoxes():
            return True
        return False

    def checkRows(self, n_squares=9):
        for col in range(n_squares):
            list_rows = []
            for row in range(n_squares):
                if not self.sudoku_board[row][col] == 0:
                    list_rows.append(self.sudoku_board[row][col])
            if len(list_rows) > len(set(list_rows)):
                return False
        return True

    def checkCols(self, n_squares=9):
        for row in range(n_squares):
            list_cols = []
            for col in range(n_squares):
                if not self.sudoku_board[row][col] == 0:
                    list_cols.append(self.sudoku_board[row][col])
            if len(list_cols) > len(set(list_cols)):
                return False
        return True

    def checkBoxes(self, n_squares=9):
        for row in range(0, n_squares, 3):
            for col in range(0, n_squares, 3):
                numbers_Box = []
                for rw in range(row, row+3):
                    for cl in range(col, col+3):
                        if self.sudoku_board[rw][cl] != 0:
                            numbers_Box.append(self.sudoku_board[rw][cl])
                if len(numbers_Box) > len(set(numbers_Box)):
                    return False
        return True