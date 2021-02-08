#Code used to generate the other scenes in the video
#author: Samuel Khongthaw
#date: 08/02/2021
#**************************************************

import math
class Particle:
    def __init__(self,G,mass,momentum_x = 0,momentum_y = 0,x = 0,y = 0):
        self.mass = mass
        self.momentum_x = momentum_x
        self.momentum_y = momentum_y
        self.x = x
        self.y = y
        self.G = G
        self.dt = 0.001
        self.collided = False
    def move(self,x_y_central_mass,M):
        if(self.collided!=True):
            x2 = x_y_central_mass[0]
            y2 = x_y_central_mass[1]
            hyp = (self.x-x2)**2 + (self.y-y2)**2
            theta = math.atan2(y2-self.y,x2-self.x)
            force = (self.G*self.mass*M)/hyp
            force_x = force*math.cos(theta)
            force_y = force*math.sin(theta)
            self.momentum_x += force_x*self.dt
            self.momentum_y += force_y*self.dt
            self.x += self.momentum_x/self.mass*self.dt
            self.y += self.momentum_y/self.mass*self.dt
        return [self.x,self.y]
    

        
