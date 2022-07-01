import pygame
import numpy as np
import time

Display = pygame.display.set_mode([601, 701])
Screen = 'game'

Board = np.zeros((6, 7))

pygame.init()
pygame.display.set_caption('Connect 4')

done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if(Screen == 'start'):
      Display.fill((0, 0, 0))
      StartButton = pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
      Display.blit(pygame.font.SysFont("Raleway", 70).render("Connect 4", 1, (255, 255, 255)), (130, 200))
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Start Game", 1, (255, 255, 255)), (174, 317))

      if(pygame.mouse.get_pressed()[0] == True and StartButton.collidepoint(pygame.mouse.get_pos())):
        Screen = 'game'

    if(Screen == 'game'):
      Display.fill((0, 0, 0))

      Row = []
      for i in range(5):
        Row.append(pygame.draw.rect(Display, (255, 255, 255), (int(i * 100), 0, 100, 700),  1))

      for i in range(6):
        pygame.draw.line(Display, (255, 255, 255), (0, i * 100 + 100), (700, i * 100 + 100))
        
      for i in range(6):
        for j in range(7):
          if Board[i, j] == 1:
            Display.blit(pygame.font.SysFont("Raleway", 150).render("X", 1, (255, 255, 255)), (i * 100 + 13, j * 100 + 5))
          if Board[i, j] == 2:
            Display.blit(pygame.font.SysFont("Raleway", 150).render("O", 1, (255, 255, 255)), (i * 100 + 10, j * 100 + 5))

      for i in range(6):
        if pygame.mouse.get_pressed()[0] == True and Row[i].collidepoint(pygame.mouse.get_pos()):
          print(i)

    if(Screen == 'end'):
      Display.fill((0, 0, 0))

      EndButton = pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Play Again", 1, (255, 255, 255)), (180, 317))

      if(pygame.mouse.get_pressed()[0] == True and EndButton.collidepoint(pygame.mouse.get_pos())):
        Screen = 'game'

    pygame.display.flip()

pygame.quit()