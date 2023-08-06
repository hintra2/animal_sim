import abc
import typing

from pygame import Color
import pygame

from board import Board, Square

class Animal():

    speed:int
    sight:int
    age:int = 0
    memory: typing.List[typing.List[typing.List[int]]]
    food:typing.List[int]

    hunger_score:int
    thirst_score:int
    rest_score:int

    current_hunger:int
    current_thirst:int
    current_rest:int

    vision:typing.List[typing.List[int]]
    position:typing.List[int]
    color:Color
    id:int

    board:Board

    def move(self, x:int = 0, y:int = 0):
        #when moving decrease food_score and thirst_score and rest_score.
        #Decrease exponentially in when you run. Windup?
        self.board.plot_square(self.board.object_board[self.position[0]][self.position[1]])
        self.position[0] += x
        self.position[1] += y
        self.current_hunger -= 2
        self.current_thirst -= 2
        self.current_rest -= 2
        print("moving to x:" + str(self.position[0]) + "y: " + str(self.position[1]))
        self.draw()

    def eat(self, food_id:int):
        #If value you are standing on is the value of things you eat, eat.
        if self.current_hunger >= self.hunger_score:
            print("rabbit not hungry. hunger: " + str(self.current_hunger))
            return
        if food_id in self.food:
            print("rabbit ate. hunger: " + str(self.current_hunger))
            self.current_hunger += 5
        else:
            print("No food")

    def drink(self, water_id:int):
        #If value you are standing on is the value of water, drink
        if self.current_thirst >= self.thirst_score:
            print("rabbit not thirsty. thirst: " + str(self.current_thirst))
            return
        if water_id == 1:
            self.current_thirst += 5
            print("rabbit drank. thirst: " + str(self.current_thirst))
        else:
            print("No water")

    def sleep(self):
        #Can do anywhere
        #Worse vision?
        #More sleep the more you sleep exponentially better
        #Reset when stop sleeping
        if self.current_rest >= self.rest_score:
            print("rabbit not tired. sleep: " + str(self.current_rest))
            return
        self.current_rest += 5
        print("rabbit sleept. sleep: " + str(self.current_rest))

    def age(self):
        self.age = self.age + 1

    def die(self):
        self.id = 1

    def check_stats(self):
        self.current_hunger -= 1
        self.current_thirst -= 1
        self.current_rest -= 1

        if self.current_hunger == 0 or self.current_thirst == 0:
            self.die()

        if self.current_rest == 0:
            self.sleep

    def draw(self):
        #print("Draw rabbit")
        x_pos = self.position[0] - self.board.current_x_pos
        y_pos = self.position[1] - self.board.current_y_pos
        if y_pos < 0 or x_pos < 0:
            return
        pygame.draw.rect(surface=self.board.display, color=self.color, rect=pygame.Rect(0+self.board.square_size*x_pos, 0+self.board.square_size*y_pos, self.board.square_size, self.board.square_size))
        pygame.display.flip()


class Rabbit(Animal):
    def __init__(self, board:Board):
        self.speed = 1
        self.sight = 5
        self.food=[0]
        self.hunger_score = self.current_hunger = 100
        self.thirst_score = self.current_thirst = 50
        self.rest_score = self.current_rest = 300
        self.position=[5,5]
        self.color = Color("#8a6e4b")
        self.board = board
        self.draw()