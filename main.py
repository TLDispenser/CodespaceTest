import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame as pyg
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pyg.Color(0,0,0)
white = pyg.Color(255,255,255)
red = pyg.Color(255,0,0)
green = pyg.Color(0,255,0)
blue = pyg.Color(0,0,255)

pyg.init()

pyg.display.set_caption('SNAAAAKE')
game_window = pyg.display.set_mode((window_x,window_y))

fps = pyg.time.Clock()

snake_position = [100, 50]

snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
  score_font = pyg.font.SysFont(font, size)
  
  score_surface = score_font.render('Score: ' + str(score), True, color)
  
  score_rect = score_surface.get_rect()
  
  game_window.blit(score_surface, score_rect)

def game_over():
  my_font = pyg.font.SysFont('helvetica', 50)
  
  game_over_surface = my_font.render('Your Score is: ' + str(score), True, red)

  game_over_rect = game_over_surface.get_rect()
  
  game_over_rect.midtop = (window_x/2, window_y/4)
  
  game_window.blit(game_over_surface, game_over_rect)
  pyg.display.flip()
  
  time.sleep(2)
  
  pyg.quit()
  
  quit()

while True:
  
  for event in pyg.event.get():
    if event.type == pyg.KEYDOWN:
      if event.key == pyg.K_UP:
        change_to = 'UP'
      if event.key == pyg.K_DOWN:
        change_to = 'DOWN'
      if event.key == pyg.K_LEFT:
        change_to = 'LEFT'
      if event.key == pyg.K_RIGHT:
        change_to = 'RIGHT'
    
  if change_to == 'UP' and direction != 'DOWN':
    direction = 'UP'
  if change_to == 'DOWN' and direction != 'UP':
    direction = 'DOWN'
  if change_to == 'LEFT' and direction != 'RIGHT':
    direction = 'LEFT'
  if change_to == 'RIGHT' and direction != 'LEFT':
    direction = 'RIGHT'
  
  if direction == 'UP':
    snake_position[1] -= 10
  if direction == 'DOWN':
    snake_position[1] += 10
  if direction == 'LEFT':
    snake_position[0] -= 10
  if direction == 'RIGHT':
    snake_position[0] += 10
  
  snake_body.insert(0, list(snake_position))
  if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
    score += 10
    fruit_spawn = False
  else:
    snake_body.pop()
  
  if not fruit_spawn:
    fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                      random.randrange(1, (window_y//10)) * 10]  
  fruit_spawn = True
  game_window.fill(black)
  
  for pos in snake_body:
    pyg.draw.rect(game_window, green, pyg.Rect(pos[0], pos[1], 9, 9))
  
  pyg.draw.rect(game_window, white, pyg.Rect(fruit_position[0], fruit_position[1], 10, 10))
  
  if snake_position[0] < 0 or snake_position[0] > window_x-10:
    game_over()
  if snake_position[1] < 0 or snake_position[1] > window_y-10:
    game_over()
  
  for block in snake_body[1:]:
    if snake_position[0] == block[0] and snake_position[1] == block[1]:
      game_over()
  
  show_score(1, white, 'helvetica', 20)
  
  pyg.display.update()
  
  fps.tick(snake_speed)