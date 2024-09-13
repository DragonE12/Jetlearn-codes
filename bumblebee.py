import pgzrun
import random

width = 600
height = 500

game_over = False
score = 0

bumblebee = Actor("bee")
flower = Actor("flower")

bumblebee.pos = 100,100
flower.pos = 200,200
def draw():
    screen.blit("background", (0,0))
    bumblebee.draw()
    flower.draw()
    screen.draw.text("Score = " + str(score), color = "black", topleft = (10,10))
    if game_over:
        screen.fill("sky blue")
        screen.draw.text("Times Up! Your final score is " + str(score), color = "black", fontsize = 40, midtop = (width/2 , 10))



def place_flower():
    flower.x = random.randint(70,(width - 70))
    flower.y = random.randint(70, (height - 70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        bumblebee.x -= 2
    elif keyboard.right:
        bumblebee.x += 2
    elif keyboard.up:
        bumblebee.y -= 2
    elif keyboard.down:
        bumblebee.y += 2
    flower_collected = bumblebee.colliderect(flower)
    if flower_collected:
        score += 10
        place_flower()

clock.schedule(time_up, 60)

pgzrun.go()