import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Mario clone')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Basic-pygame-project/graphics/Sky.png')
ground_surface=pygame.image.load('Basic-pygame-project/graphics/ground.png')
test_font = pygame.font.Font(None,50)
test_surface = test_font.render('My game',False,'Green')

while True:
    #we draw all our elements here
    #and then update everythin
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
    screen.blit(sky_surface,(0,0))    
    screen.blit(ground_surface,(0,300)) 
    screen.blit(test_surface,(300,50)) 
      
    pygame.display.update()
    clock.tick(60)