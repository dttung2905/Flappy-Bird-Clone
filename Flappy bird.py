import math
import os
from random import randint

import pygame
from pygame.locals import *


w = 640
h = 480

fps = 60
s= pygame.display.set_mode((w, h))
c= pygame.time.Clock()

class Bird():
    def __init__(self):
        self.x = 100
        self.y = 200
        self.i = pygame.image.load("FlappyBird.png")
        self.w = 72
        self.h = 63
        self.dx = 0
        self.dy = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    def paint(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dy +=1
        self.x += self.dx
        self.y += self.dy


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dy =-10
        s.blit(self.i,(self.x,self.y))

class lowerBlock():
    def __init__(self,x):
        self.x= x
        self.h = randint(0,300)+200 #Block appearing in random  height
        self.w = 80
        self.dx= -5 # Block moving from right to left
        self.dy = 0
        self.y = w - self.h
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def paint(self):
        #paint the exact same rectangle we just drew
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(s,(0,190,10),self.rect)
        self.x += self.dx
        self.y += self.dy

class upperBlock():
    def __init__(self,x):
        self.x= x
        self.h = randint(100,200)+200 #Block appearing in random  height
        self.w = 80
        self.dx= -5 # Block moving from right to left
        self.dy = 0
        self.y = w - self.h
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def paint(self):
        #paint the exact same rectangle we just drew
        self.rect = pygame.Rect(self.x, self.y, self.w, -self.h)
        pygame.draw.rect(s,(0,190,10),self.rect)
        self.x += self.dx
        self.y += self.dy
class Main():
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            s.fill((0,100,200))
            self.update()
            c.tick(fps)
            pygame.display.update()

    def update(self):
        self.b.paint()
        for i in self.p:
            i.paint()
            if i.rect.colliderect(self.b.rect):
                pygame.quit()
                quit()
        self.time += 1

        if self.time % self.interval == 0 and self.interval > 0 :
            self.p.append(upperBlock(w+100))
            self.p.append(lowerBlock(w + 100))
            self.interval -=1
    def init(self):
        self.time =0
        self.p = list()
        self.interval = 100
        self.b = Bird()
    def __init__(self):
        self.init()
        self.loop()

def main():
    a= Main()

if __name__ == "__main__":
    main()