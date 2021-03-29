import pygame as pygame
import random
from blackjack_logic import *
from game import *
from constants import *
import sys

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('BlackJack')
gameDisplay.fill(background_color)
pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))


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


class Play(pygame.sprite.Sprite):
    in_play = True
    if in_play:
        def __init__(self):
            self.deck = Deck()
            self.dealer = Hand()
            self.player = Hand()

        def deal(self):
            self.deck.shuffle()
            self.dealer.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

            self.dealer.dealer_display()

            self.player.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())

            self.player.player_display()
            
            deal_1 = pygame.image.load('img/' + self.dealer.card_val[0] + '.png').convert()
            deal_2 = pygame.image.load('img/' + self.dealer.card_val[1] + '.png').convert()
            
            player_1 = pygame.image.load('img/' + self.player.card_val[0] + '.png').convert()
            player_2 = pygame.image.load('img/' + self.player.card_val[1] + '.png').convert()
            
            # self.player.player_display()
            # card = pygame.image.load('img/2H.png').convert()
            # card2 = pygame.image.load('img/AC.png').convert()

            # card3 = pygame.image.load('img/QC.png').convert()
            # card4 = pygame.image.load('img/JD.png').convert()
            # card5 = pygame.image.load('img/10S.png').convert()
            # card6 = pygame.image.load('img/6C.png').convert()

<<<<<<< HEAD
            self.dealer.dealer_display()
=======
>>>>>>> d9d228b7fd48e2a53b662197bff89f35dde16dcf
            game_texts("Dealer's hand is:", 500, 150)

    
            #self.dealer.card_img()
            gameDisplay.blit(deal_1, (400, 200))
            gameDisplay.blit(deal_2, (550, 200))
            #gameDisplay.blit(self.dealer.dealer_display(), (550, 200))
            # game_card(player_hand, 500, 170)
            game_texts("Your's hand is:", 500, 400)
        
            gameDisplay.blit(player_1, (400, 450))
            gameDisplay.blit(player_2, (510, 450))
            # gameDisplay.blit(card5, (520, 450))
            # gameDisplay.blit(card6, (630, 450))
           
        def hit(self):
            self.player.add_card(self.deck.deal())
            self.player.display()

            if self.player_is_over():
                print("You have busted dealer won")
                in_play = False
            
            
        def stand(self):
            pass

        def exit(self):
            sys.exit()
        
play_blackjack = Play()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button("Deal", 30, 100, 150, 50, light_slat, dark_slat, play_blackjack.deal)
        button("Hit", 30, 200, 150, 50, light_slat, dark_slat, play_blackjack.hit)
        button("Stand", 30, 300, 150, 50, light_slat, dark_slat, play_blackjack.stand)
        button("EXIT", 30, 500, 150, 50, light_slat, dark_red, play_blackjack.exit)
    
    pygame.display.flip()
