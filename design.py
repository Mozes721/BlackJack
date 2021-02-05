import pygame  as pygame 
import random
from logic import *
pygame.init()

display_width = 800
display_height = 600

background_color = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
font = pygame.font.SysFont("Arial", 20)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('BlackJack')
gameDisplay.fill(background_color)
pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 600))



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# def message_display(text):
#     font = pygame.font.SysFont("Arial", 20)
#     TextSurf, TextRect = text_objects(text, font)
#     TextRect.center = ((display_width/2), (display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)

def button(msg, x, y, w, h, ic, ac, action=None):
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "deal":
                deal()
            elif action == "hit":
                hit()
            else:
                stand()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ( (x + (w/2)), (y + (h/2)) )
    gameDisplay.blit(TextSurf, TextRect)

def deal():
    game = Game()
    game.play()
    

def hit():
    
    print("hit") 

def stand():
    print("stand") 

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    

    button("Deal", 30, 70, 150, 50, light_slat, dark_slat, "deal")
    button("Hit", 30, 150, 150, 50, light_slat, dark_slat, "hit")
    button("Stand", 30, 230, 150, 50, light_slat, dark_slat, "stand")
    
    pygame.display.flip()

