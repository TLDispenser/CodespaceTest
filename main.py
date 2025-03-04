import subprocess as sub
import pygame as pyg
from button import Button
import snek_main 
import snow

pyg.init()

surface = pyg.display.set_mode((400, 300))
pyg.display.set_caption("The Hub?")

def load_snek():
    print("Loading Snek Game...")
    snek_main.run_snek_game()

def load_snow():
    print("Loading Snow Game...")
    snow.run_snow_game()


buttons = [
    Button("Load Snek", (50, 50), (300, 50), load_snek),
    Button("Load Snow", (50, 150), (300, 50), snow.run_snow_game),
]

running = True

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        for button in buttons:
            if button.is_clicked(event):
                button.callback()

    surface.fill((0, 0, 0))
    for button in buttons:
        button.draw(surface)
    pyg.display.flip()

pyg.quit()
quit()