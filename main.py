import pygame as pg
from random import randint as rd

pg.init()
pg.font.init()

# Screen configs.
SCREEN_WIDTH: int = 650
SCREEN_HEIGHT: int = 650

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Bomberman [BETA]")

running: bool = True

scenary: list = [
    [['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A']],
    [['A'], ['O'], ['O'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['O'], ['O'], ['A']],
    [['A'], ['O'], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], ['O'], ['A']],
    [['A'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['A']],
    [['A'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['A']],
    [['A'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['A']],
    [['A'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['A']],
    [['A'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['A']],
    [['A'], ['O'], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], [' '], ['X'], ['O'], ['A']],
    [['A'], ['O'], ['O'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' '], ['O'], ['O'], ['A']],
    [['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A']],
]

BRICK_BLOCKS_WIDTH: int = 50 # pixels
BRICK_BLOCKS_HEIGHT: int = 50 # pixels

def generateScenary():
    for x in range(len(scenary)):
        for y in range(len(scenary[x])):
            if scenary == [' ']:
                chance = rd(1, 20)
                if chance % 2 == 0:
                    scenary[x][y] = ["Y"]

generateScenary()

# Player configs.
x: int = int(SCREEN_WIDTH / 2)
y: int = int(SCREEN_HEIGHT / 2)

MOVEMENT_VALUE: int = 10

# Code
while running:
    pg.time.delay(75)
    screen.fill((0, 255, 0))

    for x in range(len(scenary)):
        for y in range(len(scenary[x])):
            # Generate wall bricks
            if scenary[x][y] == ['A']:
                pg.draw.rect(screen, (105, 105, 105), [((x + 1) * 50), ((y) * 50), 50, 50])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()