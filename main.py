import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Infinite runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Basic-pygame-project/graphics/Sky.png').convert()
ground_surface=pygame.image.load('Basic-pygame-project/graphics/ground.png').convert()
test_font = pygame.font.Font('Basic-pygame-project/font/Pixeltype.ttf',50)
score_surface = test_font.render('SCORE:',False,(64,64,64))
score_rectangle = score_surface.get_rect(topleft=(0,10))

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
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print('Collision')
        if event.type == pygame.KEYDOWN:
            # print('KEY DOWN')
            if event.key == pygame.K_SPACE:
                print('JUMP')
        # if event.type == pygame.KEYUP:
        #     print('KEY UP')
    screen.blit(sky_surface,(0,0))    
    screen.blit(ground_surface,(0,300)) 
    pygame.draw.rect(screen,'#c0e8ec',score_rectangle,border_radius=10)
    pygame.draw.rect(screen,'#c0e8ec',score_rectangle,6)
    screen.blit(score_surface,score_rectangle) 
    screen.blit(snail_surface,snail_rectange)
    snail_rectange.left-=4
    if snail_rectange.right<0:
        snail_rectange.right=850
    '''
    snail_position-=3
    if snail_position<0:
        snail_position=800'''
    screen.blit(player_surface,player_rectangle)
    player_rectangle.left+=2
    # pygame.draw.line(screen,'Red',(0,0),(0,400))

    # keys=pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('JUMP')
    
    # if player_rectangle.colliderect(snail_rectange):
    #     print('Collision')
    # mouse_position = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_position):
        # print(pygame.mouse.get_pressed())
        # pass
    pygame.display.update()
    clock.tick(60)