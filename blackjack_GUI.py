import pygame as pygame
import random
from blackjack_logic import *
from game import *
from constants import *

pygame.init()

clock = pygame.time.Clock()

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
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)


class Play:
    in_play = True
    if in_play:
        def __init__(self):
            self.deck = Deck()
            self.dealer = Hand()
            self.player = Hand()

        def deal(self):
           
            self.dealer.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

            self.player.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())

            game_texts("Dealer's hand is:", 500, 150)
            game_card(self.dealer.draw(gameDisplay, ([500, 300])))

            # game_card(player_hand, 500, 170)
            game_texts("Your's hand is:", 500, 400)
            game_card(self.player.draw(gameDisplay, (500, 500)))

            # game_card(dealer_hand, 500, 170)
           
        def hit(self):
            self.player.add_card(self.deck.deal())
            self.player.display()

            if self.player_is_over():
                print("You have busted dealer won")
                in_play = False
            
            
        def stand(self):
            pass
        
play_blackjack = Play()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button("Deal", 30, 70, 150, 50, light_slat, dark_slat, play_blackjack.deal)
        button("Hit", 30, 150, 150, 50, light_slat, dark_slat, play_blackjack.hit)
        button("Stand", 30, 230, 150, 50, light_slat, dark_slat, play_blackjack.stand)

    
    pygame.display.flip()