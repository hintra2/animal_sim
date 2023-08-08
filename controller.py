import time
import threading

import pygame

from animal import Rabbit
from board import Board


def controller_input_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        movement=[0,0]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            movement[1]=-1
        if keys[pygame.K_s]:
            movement[1]=movement[1]+1
        if keys[pygame.K_d]:
            movement[0]=movement[0]+1
        if keys[pygame.K_a]:
            movement[0]=movement[0]-1
        if movement != [0,0]:
            board.move(x=movement[0], y=movement[1])
        time.sleep(0.02)


def animal_loop():
    while running:
        rabbit.move(board=board, x=1, y=0)
        time.sleep(2)

running=True

def update_frame_loop():
    while running:
        board.plot_board()

if __name__ == '__main__':
    board = Board()
    rabbit = Rabbit()
    rabbit.move(board=board)

    t1 = threading.Thread(target=controller_input_loop, args=())
    t2 = threading.Thread(target=animal_loop, args=())
    t3 = threading.Thread(target=update_frame_loop, args=())
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    running=False
    t3.join()
    t2.join()