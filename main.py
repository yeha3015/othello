import pygame
from pygame.locals import *
import sys

# FIXME: リストのインデックスがめちゃくちゃ。ちゃんと整理すべき。
# 


def main():
    global max
    max = 7
    pygame.init()
    scsize = 600
    screen = pygame.display.set_mode((scsize, scsize))
    global stones
    stones = [[9, 9, 9, 9, 9, 9, 9, 9],
              [9, 9, 9, 9, 9, 9, 9, 9],
              [9, 9, 9, 9, 9, 9, 9, 9],
              [9, 9, 9, 0, 1, 9, 9, 9],
              [9, 9, 9, 1, 0, 9, 9, 9],
              [9, 9, 9, 9, 9, 9, 9, 9],
              [9, 9, 9, 9, 9, 9, 9, 9],
              [9, 9, 9, 9, 9, 9, 9, 9]]
    turn = 0
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
                print(cx, cy)
                nsi, nsj = cx * 8 // scsize, cy * 8 // scsize
                if stones[nsj][nsi] != 9:
                    break
                flip_stones(stones, nsi, nsj, turn)
                stones[nsj][nsi] = int(turn)
                turn = not turn
                print_stones_for_debug(stones)


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
    cor = 1.5
    for i in range(max):
        for j in range(max):
            if stones[j][i] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (dsc + ctr*(2*i+1) + cor*i, dsc + ctr*(2*j+1) + cor*j), rnd)
            if stones[j][i] == 1:
                pygame.draw.circle(screen, (255, 255, 255), (dsc + ctr*(2*i+1) + cor*i, dsc + ctr*(2*j+1) + cor*j), rnd)


def flip_stones(stones, nsi, nsj, turn):
    find_opposite_stones_v(stones, nsi, nsj, turn)
    # print_stones_for_debug(stones)
    return 0


def find_opposite_stones_v(stones, i, j, turn, cnt=0):
    """
    fixme: 端に到達したときのコードが動かない。
    """
    flag = False
    flip_from = max
    # positive way
    for js in range(max, j, -1):
        print(flag)
        if flag:
            if stones[js][i] == turn:
                flip_from = js
            elif stones[js][i] == 9:
                flag = False
        else:
            if stones[js][i] == turn:
                flag = True
                flip_from = js
    if flag:
        print(i, flip_from)
        stones[i:flip_from][j] = [int(turn) for _ in range(flip_from - j)]
    return 0
        

def print_stones_for_debug(stones):
    for i in stones:
        print(i)        


if __name__ == "__main__":
    main()