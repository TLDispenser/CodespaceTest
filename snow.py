import pygame as pyg
import random

pyg.init()

def run_snow_game():
    white = (255, 255, 255)
    green = (0, 255, 0)

    size = (400, 300)
    screen = pyg.display.set_mode(size)
    pyg.display.set_caption("Snow")

    snowfall = []

    for i in range(50):
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        snowfall.append([x, y])

    clock = pyg.time.Clock()

    running = True

    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False

        screen.fill(white)

        for i in range(len(snowfall)):
            snowfall[i][1] += 1
            if snowfall[i][1] > size[1]:
                snowfall[i][0] = random.randint(0, size[0])
                snowfall[i][1] = random.randint(-50, -10)
            pyg.draw.circle(screen, green, snowfall[i], 2)

        pyg.display.flip()
        clock.tick(30)

    pyg.quit()
    quit()