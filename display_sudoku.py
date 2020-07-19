# imports and initialization
import pygame
from create_board import SudokuBoard
from check_sudoku import CheckSudoku
from solve_sudoku import SolveSudoku
pygame.init()
pygame.font.init()


class InitializeGame:
    def __init__(self, screen_width=1000, screen_height=1000):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.initialize_screen()
        self.initialize_colors()
        self.sudoku_initializer = DrawSudoku(self.screen_object, self.blocks_color)
        self.start_game()

    def initialize_colors(self):
        self.background_color = (8, 182, 206)  # Turquoise Surf
        self.blocks_color = (255, 211, 1)  # Cyber Yellow
        self.title_color = (242, 243, 244)  # Anti-Flash White
        self.number_color = (140, 146, 172) # Cool Grey
        self.clicked_color = (255,53,94) # Radical Red
        self.button_color = (47,79,79) # Dark Slate Grey

    def initialize_screen(self):
        self.screen_object = pygame.display.set_mode((self.screen_width, self.screen_height))

    def start_game(self):
        while True:
            events_list = pygame.event.get()  # Handle any type of event
            keys = pygame.key.get_pressed()

            # Set background color
            self.screen_object.fill(self.background_color)

            # Draw Sudoku Squares
            self.sudoku_initializer.draw_sudoku()
            myfont = pygame.font.Font('freesansbold.ttf', 40)

            # Create Button
            rect_button = pygame.draw.rect(self.screen_object, self.button_color, [800, 900, 140, 80])
            rect_object = pygame.rect.Rect(800, 900, 140, 80)
            textsurface = myfont.render('Solve', False, self.blocks_color)
            self.screen_object.blit(textsurface, (810, 920))

            for event in events_list:
                if event.type == pygame.QUIT:
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.sudoku_initializer.reset_board()
                    if event.key == pygame.K_RETURN:
                        self.sudoku_initializer.update_board()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if rect_object.collidepoint(pos):
                        self.sudoku_initializer.solve_puzzle()
                    else:
                        clicked_box = [box for box in self.sudoku_initializer.return_list_rectangles()
                                       if box.collidepoint(pos)]
                        if len(clicked_box) > 0:
                            self.sudoku_initializer.color_box(self.clicked_color, clicked_box[0])

                if event.type == pygame.KEYDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked_box = [box for box in self.sudoku_initializer.return_list_rectangles()
                                   if box.collidepoint(pos)]
                    if len(clicked_box) > 0:
                            if event.key == pygame.K_1:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 1)
                            if event.key == pygame.K_2:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 2)
                            if event.key == pygame.K_3:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 3)
                            if event.key == pygame.K_4:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 4)
                            if event.key == pygame.K_5:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 5)
                            if event.key == pygame.K_6:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 6)
                            if event.key == pygame.K_7:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 7)
                            if event.key == pygame.K_8:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 8)
                            if event.key == pygame.K_9:
                              self.sudoku_initializer.type_box(self.number_color, clicked_box[0], 9)
            textsurface = myfont.render('Solve this Sudoku Puzzle', False, self.title_color)
            self.screen_object.blit(textsurface, (100, 30))

            # Display the game
            pygame.display.set_caption('Sudoku Puzzle')
            pygame.display.flip()
            pygame.display.update()
        pygame.quit()


class DrawSudoku:
    def __init__(self, screen_object, blocks_color):
        self.blocks_color = blocks_color
        self.screen_object = screen_object
        self.size_square = 80
        self.color_line = (255, 127, 80)  # Coral
        self.color_line2 = (250, 128, 114)  # Salmon
        self.untouchable_color = (219,112,147) # Palet Violet Red
        self.list_rectangles = []
        self.COLOR_BOX = False
        self.TYPE_BOX = False
        self.typed_boxes = []
        self.untouchables = []
        self.board_indices = {}
        self.reset_indices = True
        self.first_time = True
        self.initialized = False
        self.sudoku_board = SudokuBoard().board
        self.modified_sudokuBoard = self.sudoku_board
        self.title_color = (242, 243, 244)  # Anti-Flash White
        self.display_botText = None
        self.solved_board = False

    def color_box(self, color_block, block_object):
        self.color_block = color_block
        self.block_object = block_object
        self.COLOR_BOX = True

    def type_box(self, color_block, block_object, number_block=0):
        self.type_blockColor = color_block
        self.type_object = block_object
        self.number_block = number_block
        self.TYPE_BOX = True

    def solve_puzzle(self, n_squares=9, space_between=5):
        sudoku_solver = SolveSudoku(self.sudoku_board)
        self.sudoku_board = sudoku_solver.return_matrix()
        self.solved_board = True

        for row in range(1, n_squares + 1):
            for column in range(1, n_squares + 1):
                self.board_indices[
                    ((row * (self.size_square + space_between),
                      column * (self.size_square + space_between)))] \
                    = self.sudoku_board[column - 1][row - 1]
        self.initialized = False
        self.initialize_required()

    def return_list_rectangles(self, n_squares=9, space_between=5):
        self.list_rectangles = []
        for row in range(1, n_squares + 1):
            for column in range(1, n_squares + 1):
                self.list_rectangles.append(
                    pygame.rect.Rect(
                        (row * (self.size_square + space_between), column * (self.size_square + space_between),
                                      self.size_square, self.size_square)))
        return self.list_rectangles

    def create_board(self, n_squares=9, space_between=5):
        for row in range(1, n_squares + 1):
            for column in range(1, n_squares + 1):
                sudoku_square = [row * (self.size_square + space_between), column * (self.size_square + space_between),
                                 self.size_square, self.size_square]
                pygame.draw.rect(self.screen_object, self.blocks_color, sudoku_square)

                if self.reset_indices:
                    self.board_indices[
                        ((row * (self.size_square + space_between),
                          column * (self.size_square + space_between)))] \
                        = self.sudoku_board[column-1][row-1]
        self.reset_indices = False
        if self.first_time:
            self.initialize_required()
            self.first_time = False

    def reset_board(self):
        self.board_indices = {}
        self.sudoku_board = SudokuBoard().board
        self.display_botText = None
        self.reset_indices = True
        self.create_board()
        self.typed_boxes = []
        self.untouchables = []
        self.COLOR_BOX = False
        self.TYPE_BOX = False
        self.initialized = False
        self.initialize_required()

    def initialize_required(self):
        if not self.initialized:
            for individual_block in self.return_list_rectangles():
                if self.board_indices[(individual_block[0], individual_block[1])] != 0:
                    self.untouchables.append(individual_block)
                    self.initialized = True

    def update_board(self, n_squares=9, space_between=5):
        temp_boardIndices = self.board_indices
        for typed_box in self.typed_boxes:
            temp_boardIndices[(typed_box[0][0], typed_box[0][1])] = typed_box[1]

        for row in range(1, n_squares + 1):
            for column in range(1, n_squares + 1):
                self.modified_sudokuBoard[column-1][row-1] = temp_boardIndices[
                        ((row * (self.size_square + space_between),
                          column * (self.size_square + space_between)))]

        check_validity = CheckSudoku(self.modified_sudokuBoard)
        self.display_botText = check_validity.check_board()

    def displayBottomText(self, check_validity):
        myfont = pygame.font.Font('freesansbold.ttf', 40)
        if check_validity:
            textsurface = myfont.render('Everything is going well so far!', False, self.title_color)
            self.screen_object.blit(textsurface, (100, 900))
        else:
            textsurface = myfont.render('Something is incorrect here...', False, self.title_color)
            self.screen_object.blit(textsurface, (100, 900))

    def draw_sudoku(self, n_squares=9, space_between=5):
        if self.display_botText != None:
            self.displayBottomText(self.display_botText)

        self.create_board()

        # Borders
        pygame.draw.line(self.screen_object, self.color_line,
                         ((self.size_square + space_between), (self.size_square + space_between)),
                         ((self.size_square + space_between), (n_squares + 1) * (self.size_square + space_between)), 10)

        pygame.draw.line(self.screen_object, self.color_line,
                         ((self.size_square + space_between), (self.size_square + space_between)),
                         ((n_squares + 1) * (self.size_square + space_between), (self.size_square + space_between)), 10)

        pygame.draw.line(self.screen_object, self.color_line,
                         ((n_squares + 1) * (self.size_square + space_between), (self.size_square + space_between)),
                         ((n_squares + 1) * (self.size_square + space_between), (n_squares + 1) * (self.size_square
                                                                                                   + space_between)),
                         10)

        pygame.draw.line(self.screen_object, self.color_line,
                         ((self.size_square + space_between), (n_squares + 1) * (self.size_square + space_between)),
                         ((n_squares + 1) * (self.size_square + space_between), (n_squares + 1) * (self.size_square
                                                                                                   + space_between)),
                         10)

        # Seperate box of 3
        pygame.draw.line(self.screen_object, self.color_line2,
                         (4 * (self.size_square + space_between), (self.size_square + space_between)),
                         (4 * (self.size_square + space_between), (n_squares + 1) * (self.size_square
                                                                                     + space_between)),
                         12)

        pygame.draw.line(self.screen_object, self.color_line2,
                         (7 * (self.size_square + space_between), (self.size_square + space_between)),
                         (7 * (self.size_square + space_between), (n_squares + 1) * (self.size_square
                                                                                     + space_between)),
                         12)

        pygame.draw.line(self.screen_object, self.color_line2,
                         ((self.size_square + space_between), 4 * (self.size_square + space_between)),
                         ((n_squares + 1) * (self.size_square + space_between), 4 * (self.size_square + space_between)),
                         12)

        pygame.draw.line(self.screen_object, self.color_line2,
                         ((self.size_square + space_between), 7 * (self.size_square + space_between)),
                         ((n_squares + 1) * (self.size_square + space_between), 7 * (self.size_square + space_between), ),
                         12)

        if self.COLOR_BOX:
            pygame.draw.rect(self.screen_object, self.color_block, self.block_object, 10)

        myfont = pygame.font.Font('freesansbold.ttf', 40)
        current_index = 0

        for individual_box in self.typed_boxes:
            if self.type_object == self.typed_boxes[current_index][0]:
                self.typed_boxes.pop(current_index)
            else:
                textbox = myfont.render(str(individual_box[1]), False, self.type_blockColor)
                self.screen_object.blit(textbox, individual_box[0].center)
            current_index += 1

        for untouchable_block in self.untouchables:
            textbox = myfont.render(str(self.board_indices[(untouchable_block[0], untouchable_block[1])]),
                                    False, self.untouchable_color)
            self.screen_object.blit(textbox, (untouchable_block.center))

        if self.COLOR_BOX and self.TYPE_BOX and self.type_object not in self.untouchables:
            textbox = myfont.render(str(self.number_block), False, self.type_blockColor)
            self.screen_object.blit(textbox, (self.type_object.center))
            self.typed_boxes.append([self.type_object,self.number_block])

InitializeGame()
