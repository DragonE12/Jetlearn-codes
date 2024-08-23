import pgzrun
import random

width = 300
height = 300

def draw():
    r = 255
    g = 0
    b = random.randint(120,255)
    x1,y1 = 0,height//2
    x2,y2 = width,height//2
    for i in range(20):
        screen.draw.line((x1,y1), (x2,y2), (r,g,b))
        r -= 10
        g += 10
        y2 += 5
        y1 -= 5

pgzrun.go()
