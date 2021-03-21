import simpleguitk
import pygame as pygame

display_width = 800
display_height = 600

background_color = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)


SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)

# load card sprites
card_images = simpleguitk.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simpleguitk.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")  
