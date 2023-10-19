# 제목:  틱택토(Tic-Tac-Toe) 게임
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.12

import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)

large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
size = [600,600]
screen = pygame.display.set_mode(size)

turn = 0
grid = [" ", " ", " ", 
        " ", " ", " ",
        " ", " ", " "]

done = False
clock = pygame.time.Clock()

def runGame():
  global done
  while not done :
    clock.tick(10)
    screen.fill(WHITE)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      
      pygame.display.update()

runGame()
pygame.quit()