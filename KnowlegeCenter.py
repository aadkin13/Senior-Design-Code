# This code if or the Knowledge Center
import pygame

pygame.init()
x = 20
y = 30
white = [255, 255, 255]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
stop = pygame.image.load('stop.jpg')
screen.fill(white)
screen.blit(stop, (x, y))
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if stop.get_rect().collidepoint(x, y):
                run = False
            
pygame.display.quit()