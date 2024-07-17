import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Mario clone')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Basic-pygame-project/graphics/Sky.png').convert()
ground_surface=pygame.image.load('Basic-pygame-project/graphics/ground.png').convert()
test_font = pygame.font.Font('Basic-pygame-project/font/Pixeltype.ttf',50)
test_surface = test_font.render('My game',False,'Black')
snail_surface = pygame.image.load('Basic-pygame-project/graphics/snail/snail1.png').convert_alpha()
snail_rectange=snail_surface.get_rect(midbottom=(700,300))
# snail_position=700
player_surface = pygame.image.load('Basic-pygame-project/graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(50,300))

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
    screen.blit(snail_surface,snail_rectange)
    snail_rectange.left-=3
    if snail_rectange.left<0:
        snail_rectange.right=850
    '''
    snail_position-=3
    if snail_position<0:
        snail_position=800'''
    screen.blit(player_surface,player_rectangle)
    player_rectangle.left+=2
    
    pygame.display.update()
    clock.tick(60)