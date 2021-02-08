#Code used to generate the other scenes in the video
#author: Samuel Khongthaw
#date: 08/02/2021
#**************************************************
import pygame,sys
from particle import Particle
from pygame.locals import*
pygame.init()
#CONSTANTS
WINDOW_SIZE = [1280,730]
G = 10
#/CONSTANTS
pygame.display.set_caption("Gravity Simulator")
screen = pygame.display.set_mode(WINDOW_SIZE)
bg = pygame.image.load("bg.png").convert()
star1 = pygame.image.load("binary1.png").convert()
star2 = pygame.image.load("binary2.png").convert()
star1.set_colorkey(-1, RLEACCEL)
star2.set_colorkey(-1, RLEACCEL)
s1 = Particle(G,mass = 10e5+10e5,x = 650, y = 300, momentum_y = 10e7,momentum_x = 10e7)
s2 = Particle(G,mass = 10e5+10e4,x = 500, y = 550, momentum_y = -10e7,momentum_x = -10e7)
while True:
    for event in pygame.event.get():
        if(event.type in [QUIT,KEYDOWN]):
            pygame.quit()
            sys.exit()
    screen.blit(bg,[0,0])
    past_s1 = [s1.x,s1.y]
    screen.blit(star1,s1.move([s2.x,s2.y],s2.mass))
    screen.blit(star2,s2.move(past_s1,s1.mass))
    pygame.display.update()
