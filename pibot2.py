#!/usr/bin/env python
#
 
import pygame
import sys
from pygame.locals import *
import nxt
import nxt.locator
from nxt.sensor import *
from nxt.motor import *
from time import sleep
 
 
def input(events, state):
    for event in events:
        if event.type == QUIT:
            state = 0
        if event.type == KEYDOWN:
            if event.key == K_q:
                print "q"
                state = 0
            elif event.key == K_w:
                print "Forwards"
                both.turn(100, 360, False)
            elif event.key == K_s:
                print "Backwards"
                both.turn(-100, 360, False)
            elif event.key == K_a:
                print "Left"
                leftboth.turn(100, 90, False)
            elif event.key == K_d:
                print "Right"
                rightboth.turn(100, 90, False)
            elif event.key == K_f:
                print "Head"
                head.turn(30, 45, False)
            elif event.key == K_r:
                state = explore(state)
 
    return state
 
def explore(state):
    if state == 1:
        state = 2
        print "Explore"
    elif state == 2:
        state = 1
        print "Command"
    return state
 
def autoroll():
    if Ultrasonic(brick, PORT_2).get_sample() < 20:
        both.brake()
        both.turn(-100, 360, False)
        sleep(1)
        leftboth.turn(100, 360, False)
        sleep(1)
    else:
        both.run(100)
 
def update(state):
    if state == 2:
        autoroll()
     
    return state
 
pygame.init()
window = pygame.display.set_mode((800, 400))
fpsClock = pygame.time.Clock()
 
brick = nxt.locator.find_one_brick()
left = Motor(brick, PORT_B)
right = Motor(brick, PORT_C)
both = nxt.SynchronizedMotors(left, right, 0)
leftboth = nxt.SynchronizedMotors(left, right, 100)
rightboth = nxt.SynchronizedMotors(right, left, 100)
head = Motor(brick, PORT_A)
 
state = 1
print "Running"
while (state > 0):
    state = input(pygame.event.get(), state)
    #pygame.display.flip()
    state = update(state)
 
print "Quit"