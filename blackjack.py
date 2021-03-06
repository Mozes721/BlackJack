import pygame as pygame
import random
from cards import *
from game import *
from constants import *

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('BlackJack')
gameDisplay.fill(background_color)
pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 600))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_texts(text, x, y):

    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def game_card(card, x, y):

    TextSurf, TextRect = text_objects(card, textfont)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


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
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)


def deal():
    global in_play, dealer
    in_play = True
    if in_play == True:
        deck = Deck()
        deck.shuffle()
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        game_texts("Dealer's hand is:", 500, 150)
        print(dealer.display())
        # game_card(player_hand, 500, 170)
        game_texts("Your's hand is:", 500, 400)
        #game_card(dealer_hand, 500, 170)
        
    
    if in_play == False:
        pass


def hit():
    pass


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
