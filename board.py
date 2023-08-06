from random import randint
import pygame

class Square(pygame.Rect):
    def __init__(self, id:int, value:int, left, top, width, height):
        pygame.Rect.__init__(self, left, top, width, height)
        self.id = 1 if id == 100 else 0
        self.value=value
    id:int
    value:int

class Board():
    screen_width=1500
    screen_height=800

    display:pygame.Surface
    square_size=20
    columns:int=round(screen_width/square_size)
    rows:int=round(screen_height/square_size)
    current_x_pos:int = 0
    current_y_pos:int = 0

    object_board: list[list[Square]]
    object_board_width=500
    object_board_height=500

    def get_color(self, id:int):
        if id == 0:
            return "#1f7325"
        else:
            return "#5b85d4"

    def plot_square(self, square:pygame.Rect):
        pygame.draw.rect(surface=self.display, color=self.get_color(square.id), rect=square)
        pygame.display.flip()

    def plot_board(self):
        for row in range(0, self.columns):
            for column in range(0, self.rows):
                rect = pygame.Rect(0+self.square_size*row, 0+self.square_size*column, self.square_size, self.square_size)
                pygame.draw.rect(surface=self.display, color=self.get_color(self.object_board[self.current_x_pos+row][self.current_y_pos+column].id), rect=rect)
        pygame.display.flip()

    def move(self, x:int, y:int):
        if not self.current_x_pos + x == -1 and not self.current_x_pos + x + self.columns + 1 == self.object_board_width:
            self.current_x_pos += x
        if not self.current_y_pos + y == -1 and not self.current_y_pos + y + self.rows + 1 == self.object_board_height:
            self.current_y_pos += y
        self.plot_board()

    def __init__(self):
        #generate initial board
        self.object_board=[[Square(id=randint(0,101), value=0, left=row*self.square_size, top=column*self.square_size, width=self.square_size, height=self.square_size) for column in range(0, self.object_board_width)] for row in range(0, self.object_board_height)]
        #generate water
        for row in range(0, self.object_board_width):
            for column in range(0, self.object_board_height):
                if self.object_board[row][column].id == 1:
                    self.spread_water(row, column, 0)

        pygame.init()
        self.display = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.plot_board()

    def spread_water(self, x_pos:int, y_pos:int, water_rate:int):
        if randint(0, water_rate) == 0:
            self.object_board[x_pos][y_pos].id = 1
            try:
                self.spread_water(x_pos-1, y_pos, water_rate+3)
            except:
                pass
            try:
                self.spread_water(x_pos+1, y_pos, water_rate+3)
            except:
                pass
            try:
                self.spread_water(x_pos, y_pos-1, water_rate+3)
            except:
                pass
            try:
                self.spread_water(x_pos, y_pos+1, water_rate+3)
            except:
                pass