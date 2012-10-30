#!/usr/bin/env python
#
 
import[object DOMWindow]pygame
import[object DOMWindow]sys
from[object DOMWindow]pygame.locals[object DOMWindow]import[object DOMWindow]*
import[object DOMWindow]nxt
import[object DOMWindow]nxt.locator
from[object DOMWindow]nxt.sensor import[object DOMWindow]*
from[object DOMWindow]nxt.motor import[object DOMWindow]*
from[object DOMWindow]time import[object DOMWindow]sleep
 
 
def[object DOMWindow]input(events, state):
[object DOMWindow]for[object DOMWindow]event in[object DOMWindow]events:
[object DOMWindow]if[object DOMWindow]event.type[object DOMWindow]==[object DOMWindow]QUIT:
[object DOMWindow]state =[object DOMWindow]0
[object DOMWindow]if[object DOMWindow]event.type[object DOMWindow]==[object DOMWindow]KEYDOWN:
[object DOMWindow]if[object DOMWindow]event.key ==[object DOMWindow]K_q:
[object DOMWindow]print[object DOMWindow]"q"
[object DOMWindow]state =[object DOMWindow]0
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_w:
[object DOMWindow]print[object DOMWindow]"Forwards"
[object DOMWindow]both.turn(100, 360, False)
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_s:
[object DOMWindow]print[object DOMWindow]"Backwards"
[object DOMWindow]both.turn(-100, 360, False)
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_a:
[object DOMWindow]print[object DOMWindow]"Left"
[object DOMWindow]leftboth.turn(100, 90, False)
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_d:
[object DOMWindow]print[object DOMWindow]"Right"
[object DOMWindow]rightboth.turn(100, 90, False)
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_f:
[object DOMWindow]print[object DOMWindow]"Head"
[object DOMWindow]head.turn(30, 45, False)
[object DOMWindow]elif[object DOMWindow]event.key ==[object DOMWindow]K_r:
[object DOMWindow]state =[object DOMWindow]explore(state)
 
[object DOMWindow]return[object DOMWindow]state
 
def[object DOMWindow]explore(state):
[object DOMWindow]if[object DOMWindow]state ==[object DOMWindow]1:
[object DOMWindow]state =[object DOMWindow]2
[object DOMWindow]print[object DOMWindow]"Explore"
[object DOMWindow]elif[object DOMWindow]state ==[object DOMWindow]2:
[object DOMWindow]state =[object DOMWindow]1
[object DOMWindow]print[object DOMWindow]"Command"
[object DOMWindow]return[object DOMWindow]state
 
def[object DOMWindow]autoroll():
[object DOMWindow]if[object DOMWindow]Ultrasonic(brick, PORT_2).get_sample() < 20:
[object DOMWindow]both.brake()
[object DOMWindow]both.turn(-100, 360, False)
[object DOMWindow]sleep(1)
[object DOMWindow]leftboth.turn(100, 360, False)
[object DOMWindow]sleep(1)
[object DOMWindow]else:
[object DOMWindow]both.run(100)
 
def[object DOMWindow]update(state):
[object DOMWindow]if[object DOMWindow]state ==[object DOMWindow]2:
[object DOMWindow]autoroll()
[object DOMWindow]
[object DOMWindow]return[object DOMWindow]state
 
pygame.init()
window =[object DOMWindow]pygame.display.set_mode((400, 400))
fpsClock =[object DOMWindow]pygame.time.Clock()
 
brick =[object DOMWindow]nxt.locator.find_one_brick()
left =[object DOMWindow]Motor(brick, PORT_B)
right =[object DOMWindow]Motor(brick, PORT_C)
both =[object DOMWindow]nxt.SynchronizedMotors(left, right, 0)
leftboth =[object DOMWindow]nxt.SynchronizedMotors(left, right, 100)
rightboth =[object DOMWindow]nxt.SynchronizedMotors(right, left, 100)
head =[object DOMWindow]Motor(brick, PORT_A)
 
state =[object DOMWindow]1
print[object DOMWindow]"Running"
while[object DOMWindow](state > 0):
[object DOMWindow]state =[object DOMWindow]input(pygame.event.get(), state)
[object DOMWindow]#pygame.display.flip()
[object DOMWindow]state =[object DOMWindow]update(state)
 
print[object DOMWindow]"Quit"