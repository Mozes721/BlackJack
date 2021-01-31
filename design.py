import pygame  as pygame 

background_color = (34,139,34)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('BlackJack')
screen.fill(background_color)

pygame.display.flip()

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

