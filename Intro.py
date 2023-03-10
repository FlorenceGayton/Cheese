import pygame
import math
import time
import sys

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cheese Game")

#load image
bg = pygame.image.load("Images\pixil-frame-0.png").convert()
bg = pygame.transform.scale(bg, (1000, 600))
bg_width = bg.get_width()
bg_rect = bg.get_rect()

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1
count = 0
font = pygame.font.SysFont('Berlin Sans FB', 40)
menuobjects = []
gameobjects = []


#Play button defs
class Button():
  def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.onclickFunction = onclickFunction
      self.onePress = onePress

      self.fillColors = {
          'normal': '#161616',
          'hover': '#424242',
          'pressed': '#333333',
      }

      self.buttonSurface = pygame.Surface((self.width, self.height))
      self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

      self.buttonSurf = font.render(buttonText, True, (255, 183, 0))

      self.alreadyPressed = False

  def process(self):

      mousePos = pygame.mouse.get_pos()
      self.buttonSurface.fill(self.fillColors['normal'])
      if self.buttonRect.collidepoint(mousePos):
          self.buttonSurface.fill(self.fillColors['hover'])

          if pygame.mouse.get_pressed(num_buttons=3)[0]:
              self.buttonSurface.fill(self.fillColors['pressed'])

              if self.onePress:
                  self.onclickFunction()

              elif not self.alreadyPressed:
                  self.onclickFunction()
                  self.alreadyPressed = True

          else:
              self.alreadyPressed = False

      self.buttonSurface.blit(self.buttonSurf, [
          self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
          self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
      ])
      screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
  global stage
  stage = "game"

#game loop
stage = "menu"
run = True
while run:
  clock.tick(FPS)
  if stage == "menu":
    #scroll background
    scroll -= 5

    #draw scrolling background
    if count == 702:
      title = pygame.image.load("Images\CheeseGameTitle.png").convert()
      screen.blit(title, (0, 0))
      PlayButton = Button(650, 450, 200, 50, 'PLAY', myFunction)
      menuobjects.append(PlayButton)
    else:
      for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        count += 1

    #reset scroll
    if abs(scroll) > bg_width:
      scroll = 0
    for object in menuobjects:
      object.process()
  elif stage == "game":
    #new background
    screen = pygame.display.set_mode((1000, 600))
    screen_x = 1000
    screen_y = 600
    bg2 = pygame.image.load("Images\\bg2.png").convert()
    screen.blit(bg2, (0, 0))

    #set character move variables
    CheeseChar_x = 100
    CheeseChar_y = 220
    step = 2
    
    #add character
    CheeseCharacter = pygame.image.load("Images\CheeseCharacter.png")
    screen.blit(CheeseCharacter, (CheeseChar_x, CheeseChar_y))
    
    # Character move
    pygame.display.flip() 
    pygame.display.update()    
    
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT] and CheeseChar_x > step:
      CheeseChar_x -= step
    if key_input[pygame.K_RIGHT] and CheeseChar_x < screen_x - 144 - step:
        CheeseChar_x += step
    if key_input[pygame.K_UP] and CheeseChar_y > step:
        CheeseChar_y -= step
    if key_input[pygame.K_DOWN] and CheeseChar_y < screen_y - 162 - step:
        CheeseChar_y += step


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()