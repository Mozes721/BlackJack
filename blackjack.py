import pygame as pygame
import random
from cards import *
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

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def redrawWindow():
    

def deal():
    global in_play, dealer
    in_play = True
    if in_play == True:
        deck = Deck()
        deck.shuffle()
        dealer = Hand()
        game_texts("Dealer's hand is:", 500, 150)
        print(dealer.display())
        # game_card(player_hand, 500, 170)
        game_texts("Your's hand is:", 500, 400)
        #game_card(dealer_hand, 500, 170)
        
    
    if in_play == False:
        pass


def hit():
    print("hit")


def stand():
    print("stand")


running = True
deal_btn = button((0, 257, 0), 30, 70, 150, 50, "deal")
hit_btn = button((0, 255, 0), 30, 150, 150, 50, "hit")
stand_btn = button((0, 255, 0), 30, 230, 150, 50, "stand")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    
    pygame.display.flip()