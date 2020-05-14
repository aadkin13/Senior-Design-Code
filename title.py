# This code if or the Knowledge Center
import pygame
import time

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((500, 500))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen.fill(black)
pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 64)

text = font.render('Hello, Welcome to the Discovery Place', True, green, black)
text2 = font.render('This is the Knowledge Center', True, green, black)

textRect = text.get_rect()
text2Rect = text2.get_rect()

textRect.center = (width / 2, height / 2)
text2Rect.center = (width/2 + 90, height/2 + 90)

run = True
while run:
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                
    pygame.display.update()
                
pygame.display.quit()
