import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()
    scsize = 600
    dsc = scsize // 40
    screen = pygame.display.set_mode((scsize, scsize))
    stones = [[1, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 2, 0, 0, 0],
              [0, 0, 0, 2, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1],]
    while True:
        make_bg(screen, scsize)
        draw_stones(screen, stones, scsize)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                cx, cy = event.pos


def make_bg(screen, sc):
    screen.fill((0, 100, 0))
    dsc = sc // 40
    for i in range(dsc, sc - dsc, int((sc - dsc*2) // 8)):
        pygame.draw.line(screen, (0, 0, 0), (i, dsc), (i, sc - dsc - 2), 2)
        pygame.draw.line(screen, (0, 0, 0), (dsc, i), (sc - dsc - 2, i), 2)


def draw_stones(screen, stones, sc):
    dsc = sc // 40
    ctr = (sc - 2 * dsc) // 16
    rnd = ctr - dsc // 2
    cor = 2
    for i in range(len(stones)):
        for j in range(len(stones[i])):
            if stones[i][j] == 1:
                pygame.draw.circle(screen, (0, 0, 0), (dsc + ctr*(2*i+1) + cor, dsc + ctr*(2*j+1) + cor), rnd)
            if stones[i][j] == 2:
                pygame.draw.circle(screen, (255, 255, 255), (dsc + ctr*(2*i+1) + cor, dsc + ctr*(2*j+1) + cor), rnd)



if __name__ == "__main__":
    main()