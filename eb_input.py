#! /usr/bin/env python
# Clase Input
# Copyright (C) 2012  EGGBREAKER <eggbreaker@live.com.ar>

import pygame
from pygame.locals import *

UP, RIGHT, DOWN, LEFT = (1,1), (1,-1), (-1,-1), (-1,1)
NE, SE, NO, SO = (0,-1), (1,0), (-1,0), (0,1)
dKey2Dir = {275: RIGHT, 273:DOWN, 276:LEFT, 274:UP}

class Input():
    def __init__(self):
        self.facing = RIGHT
        self.Commands = []
        self.Order = (0,0)
        self.Quit = False
        self.ChangeSignal = False
        self.Click = False
        self.Rotate = False

    def update(self):
        self.ChangeSignal = False
        self.WalkRun = False
        self.Wait = False
        self.Rotate = False
        self.Click = False
        self.nSkill = 0
        for anEvent in pygame.event.get():
            if anEvent.type == pygame.KEYDOWN:
                if anEvent.key in dKey2Dir.keys():
                    self.append(dKey2Dir[anEvent.key])
                if anEvent.key == K_ESCAPE:
                    self.Quit = True
                if anEvent.key == K_TAB:
                    self.ChangeSignal = True
                if anEvent.key == K_LSHIFT:
                    self.WalkRun = True
                if anEvent.key == K_SPACE:
                    self.Wait = True
                if anEvent.key == K_LCTRL:
                    self.Rotate = True
                if pygame.mouse.get_pressed()[0]:
                    self.Click = True
                if anEvent.key == 'K_1':
                    self.nSkill = 0
                if anEvent.key == 'K_2':
                    self.nSkill = 1
            if anEvent.type == pygame.KEYUP:
                if anEvent.key in dKey2Dir.keys():
                    self.remove(dKey2Dir[anEvent.key])


    def updateOrder(self):
        xAcum, yAcum = 0, 0
        for Command in self.Commands:
            xAcum += Command[0]
            yAcum += Command[1]

        if xAcum == 2:
            xAcum = 1
        elif xAcum == -2:
            xAcum = -1

        if yAcum == 2:
            yAcum = 1
        elif yAcum == -2:
            yAcum = -1

        self.Order = xAcum, yAcum

    def append(self, aCommand):
        self.Commands.append(aCommand)
        self.updateOrder()

    def remove(self, aCommand):
        assert len(self.Commands) > 0
        self.Commands.remove(aCommand)
        self.updateOrder()

    def empty(self):
        return len(self.Commands) == 0

    def mouse(self):
        x, y = pygame.mouse.get_pos()
        pos = (int(x/(TILEW-(GAPSIZE*BOARDWIDTH))),int(y/(TILEH-(GAPSIZE*BOARDWIDTH))))
        return pos

    def mouseDirection(self, char):
        cX, cY = char.posicion
        mX, mY = self.mouse()
        if mX > cX:
            if abs(mX+cX) > abs(cY+mY):
                self.facing = RIGHT
        else:
            if abs(mX+cX) > abs(cY+mY):
                self.facing = LEFT
        if mY > cY:
            if abs(mY+cY) > abs(cX+mX):
                self.facing = DOWN
        else:
            if abs(mY+cY) > abs(cX+mX):
                self.facing = UP



