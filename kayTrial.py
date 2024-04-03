import pygame
from pygame.locals import*

pygame.init()


screen_width = 700
screen_height = 700


screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Platformer')


sun_img = pygame.image.load('assets\Background\Blue.png')
bg_img = pygame.image.load('assets\Background\Blue.png')

run = True
while run == True:
    
    screen.blit(bg_img,(0,0))
    screen.blit(sun_img,(100,100))    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()
