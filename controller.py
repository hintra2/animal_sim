import time
import threading

import pygame

from animal import Rabbit
from board import Board, Square


def controller_input_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        movement=[0,0]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            movement[0]=-1
        if keys[pygame.K_s]:
            movement[0]=movement[0]+1
        if keys[pygame.K_d]:
            movement[1]=movement[1]+1
        if keys[pygame.K_a]:
            movement[1]=movement[1]-1
        if movement != [0,0]:
            board.move(x=movement[1], y=movement[0])
            rabbit.draw()
        time.sleep(0.015)


def animal_loop():
    while running:
        rabbit.move(1,0)
        time.sleep(2)

running=True

if __name__ == '__main__':
    board = Board()

    rabbit = Rabbit(board=board)

    t1 = threading.Thread(target=controller_input_loop, args=())
    t2 = threading.Thread(target=animal_loop, args=())
    t1.start()
    t2.start()
    t1.join()
    running=False
    t2.join()