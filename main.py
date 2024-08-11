import pygame
from sys import exit
import math

def display_score():
    current_time=pygame.time.get_ticks() - start_time
    score = current_time/1000
    score_value = test_font.render(f"{math.trunc(score)}",False,(64,64,64))
    score_value_rectangle = score_value.get_rect(topleft=(120,10))
    screen.blit(score_value,score_value_rectangle)
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Infinite runner')
clock = pygame.time.Clock()
game_active = True
start_time = 0

sky_surface = pygame.image.load('Basic-pygame-project/graphics/Sky.png').convert()
ground_surface=pygame.image.load('Basic-pygame-project/graphics/ground.png').convert()
test_font = pygame.font.Font('Basic-pygame-project/font/Pixeltype.ttf',50)
score_surface = test_font.render('SCORE:',False,(64,64,64))
score_rectangle = score_surface.get_rect(topleft=(0,10))
game_over = test_font.render("GAME OVER",False,(0,0,0))
game_over_rect = game_over.get_rect(topleft = (300,50))
to_restart = test_font.render("To restart Press 'BACKSPACE'",False,(0,0,0))
to_quit = test_font.render("To quit press 'q'",False,(0,0,0))

snail_surface = pygame.image.load('Basic-pygame-project/graphics/snail/snail1.png').convert_alpha()
snail_rectange=snail_surface.get_rect(midbottom=(700,300))
player_surface = pygame.image.load('Basic-pygame-project/graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(70,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
        if game_active:
            if player_rectangle.bottom ==300:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rectangle.collidepoint(event.pos):
                        player_gravity = -25
            if player_rectangle.bottom == 300:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    game_active=True
                    snail_rectange.right =800
                    start_time = pygame.time.get_ticks()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
    if game_active:
        screen.blit(sky_surface,(0,0))    
        screen.blit(ground_surface,(0,300)) 
        pygame.draw.rect(screen,'#c0e8ec',score_rectangle,border_radius=10)
        pygame.draw.rect(screen,'#c0e8ec',score_rectangle,6)
        screen.blit(score_surface,score_rectangle) 
        screen.blit(snail_surface,snail_rectange)
        snail_rectange.left-=5
        display_score()
        if snail_rectange.right<0:
            snail_rectange.right=850
        if player_rectangle.left>800:
            player_rectangle.left = -30
        '''
        snail_position-=3
        if snail_position<0:
            snail_position=800'''
        player_gravity+=1
        player_rectangle.y += player_gravity 
        if player_rectangle.bottom>=300:
            player_rectangle.bottom =300
        screen.blit(player_surface,player_rectangle)
        
        if snail_rectange.colliderect(player_rectangle):
            game_active = False
    else:
        screen.blit(sky_surface,(0,0))
        pygame.draw.rect(screen,'#FF0000',game_over_rect,border_radius=10)
        pygame.draw.rect(screen,'#FF0000',game_over_rect,width=6)
        
        screen.blit(game_over,game_over_rect)
        screen.blit(to_restart,(150,100))
        screen.blit(to_quit,(270,150))


    pygame.display.update()
    clock.tick(60)