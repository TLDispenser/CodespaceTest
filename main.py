import snek_main
import subprocess as sub
import pygame as pyg

pyg.init()

surface = pyg.display.get_surface((400, 300))
pyg.display.get_caption("The Hub?")

running = True
while running:
    for event in pyg.event.get():
        if event == pyg.QUIT:
            running = False

pyg.quit()

quit()