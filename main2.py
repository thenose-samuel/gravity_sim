#I'm really sorry if the code is messy, this is my first time using the OOP paradigm
#The Particle class is in the other file named particle.py
#author: Samuel Khongthaw
#date: 08/02/2021
#************************#
import pygame,sys
from particle import Particle
from pygame.locals import*
pygame.init()
#CONSTANTS
WINDOW_SIZE = [1280,730]
G = 0.2
M = 10e7
#/CONSTANTS
pygame.display.set_caption("Gravity Simulator")
screen = pygame.display.set_mode(WINDOW_SIZE)
bg = pygame.image.load("bg.png").convert()
central_mass = pygame.image.load("centralmass.png").convert_alpha()
central_mass.set_colorkey(-1, RLEACCEL)
pos_central_mass = [1280//2,700//2]
rec_central = pygame.Rect(pos_central_mass[0],pos_central_mass[1],central_mass.get_width(),central_mass.get_height())
p1 = Particle(G,mass = 2,x = 300, y = 200, momentum_y = 300,momentum_x = 0)
p1_image = pygame.image.load('grass.png')
p1_rect = pygame.Rect(0,0,p1_image.get_width(),p1_image.get_height())
p2 = Particle(G,mass = 3,x = 100, y = 300, momentum_y = 200,momentum_x = 0)
p2_image = pygame.image.load('grass2.png')
p2_rect = pygame.Rect(0,0,p2_image.get_width(),p2_image.get_height())
p3 = Particle(G,mass = 4,x = 600, y = 700, momentum_y = 200,momentum_x = -400)
p3_image = pygame.image.load('grass3.png')
p3_rect = pygame.Rect(0,0,p3_image.get_width(),p3_image.get_height())
p4 = Particle(G,mass = 3,x = 1280//2-100 , y = 700//2-100, momentum_y = 700,momentum_x = -400)
p4_image = pygame.image.load('grass4.png')
p4_rect = pygame.Rect(0,0,p4_image.get_width(),p4_image.get_height())
while True:
    for event in pygame.event.get():
        if(event.type in [QUIT, KEYDOWN]):
            pygame.quit()
            sys.exit()
    screen.blit(bg,[0,0])
    screen.blit(central_mass,pos_central_mass)
    p1_rect.x,p1_rect.y = p1.move(pos_central_mass,M)
    if(p1_rect.colliderect(rec_central)):
       p1.collided = True
    p2_rect.x,p2_rect.y = p2.move(pos_central_mass,M)
    if(p2_rect.colliderect(rec_central)):
       p2.collided = True
    p3_rect.x,p3_rect.y = p3.move(pos_central_mass,M)
    if(p3_rect.colliderect(rec_central)):
       p3.collided = True
    p4_rect.x,p4_rect.y = p4.move(pos_central_mass,M)
    if(p4_rect.colliderect(rec_central)):
       p4.collided = True
    screen.blit(p4_image,[p4_rect.x,p4_rect.y])
    screen.blit(p1_image,[p1_rect.x,p1_rect.y])
    screen.blit(p2_image,[p2_rect.x,p2_rect.y])
    screen.blit(p3_image,[p3_rect.x,p3_rect.y])
    pygame.display.update()
    
    
