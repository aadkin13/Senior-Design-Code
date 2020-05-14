# This code if or the Knowledge Center title screen
import pygame

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# screen = pygame.display.set_mode((500, 500))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen.fill(black)
pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 58)

text = font.render('Hello, Welcome to the Discovery Place', True, green, black)
text2 = font.render('This is the Knowledge Center', True, green, black)
text3 = font.render('Please place your artifact here', True, green, black)

textRect = text.get_rect()
text2Rect = text2.get_rect()
text3Rect = text3.get_rect()

textRect.center = (width / 2, height / 2 - 300)
text2Rect.center = (width / 2, height / 2 - 150)
text3Rect.center = (width / 2 + 90, height / 2)

arrow = pygame.image.load('arrow.jpg')

run = True
while run:
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    screen.blit(arrow, (width / 2 - 600, height / 2 - 90))
    screen.blit(text3, text3Rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.display.quit()
quit()
