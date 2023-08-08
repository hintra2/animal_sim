from random import randint
import pygame

from square import Square

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
    object_board_height=100

    def get_square(self, x, y) -> Square:
        return self.object_board[x][y]

    def get_color(self, id:int):
        if id == 0:
            return "#1f7325"
        else:
            return "#5b85d4"

    def plot_board(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                square = self.get_square(self.current_x_pos+column, self.current_y_pos+row)
                color = self.get_color(square.id)
                if square.get_animals():
                    color = square.get_animals().get_color()

                rect = pygame.Rect(0+self.square_size*column, 0+self.square_size*row, self.square_size, self.square_size)
                pygame.draw.rect(surface=self.display, color=color, rect=rect)
        pygame.display.flip()

    def move(self, x:int, y:int):
        if not self.current_x_pos + x == -1 and x != 0 and not self.current_x_pos + x + self.columns + 2 >= self.object_board_width:
            self.current_x_pos += x
        if not self.current_y_pos + y == -1 and y != 0 and not self.current_y_pos + y + self.rows + 2 >= self.object_board_height:
            self.current_y_pos += y

    def __init__(self):
        #generate initial board
        self.object_board=[[Square(id=randint(0,101), value=0) for row in range(0, self.object_board_height)] for column in range(0, self.object_board_width)]
        #generate water
        for column in range(0, self.object_board_width):
            for row in range(0, self.object_board_height):
                if self.object_board[column][row].id == 1:
                    self.spread_water(column, row, 0)

        pygame.init()
        self.display = pygame.display.set_mode((self.screen_width,self.screen_height))

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