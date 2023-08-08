import abc
import typing

import pygame
from pygame import Color

from board import Board
from square import Square


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
    x:int
    y:int
    color:Color
    id:int

    def get_color(self):
        return self.color

    def move(self, board:Board, x:int = 0, y:int = 0):
        last_square=board.get_square(self.x,self.y)
        last_square.remove_animal_from_square(self)
        self.x += x
        self.y += y
        last_square=board.get_square(self.x,self.y)
        last_square.add_animal_to_square(self)

        print("moving to x:" + str(self.x) + "y: " + str(self.y))

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

class Rabbit(Animal):
    def __init__(self):
        self.speed = 1
        self.sight = 5
        self.food=[0]
        self.hunger_score = self.current_hunger = 100
        self.thirst_score = self.current_thirst = 50
        self.rest_score = self.current_rest = 300
        self.x=5
        self.y=5
        self.color = Color("#8a6e4b")
