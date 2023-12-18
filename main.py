import time
import turtle
import random
import math
import keyboard

colors = {"char":(179,224,255),"charM":(156,158,159),"food3":(73, 118, 205),"food2":(113, 158, 235),"food1":(153, 198, 255),"heart":(198, 67, 90),"bot":(229, 116, 121), "green":(158, 202, 137)}
turtle.colormode(255)
score = 1
autoAim = False
turtle.title("Diep.io")
########################################################################################################################
########################################################################################################################
# Set up window
window = turtle.Screen()
window.screensize(400,400)
#window.bgpic("diepbg.png")
window.bgcolor("black")
window.tracer(0)
window.bounce_on = False
#Invis Turtle
invis = turtle.Turtle()
invis.shape("square")
invis.turtlesize(29.5)
#Border
border = turtle.Turtle()
border.color("grey")
border.hideturtle()
border.penup()
border.goto(-300, -300)
border.pendown()
border.pensize(4)
for i in range(4):
  border.fd(600)
  border.left(90)
#ammo innit
ammo = []
spawn_interval = 0.5
ball_speed = 2
#set up charactor
charM = turtle.Turtle()
charM.penup()
charM.color(colors["charM"])
charM.shape("square")
charM.turtlesize(0.75)
charM.setx(charM.xcor()+20)
char = turtle.Turtle()
char.penup()
char.color(colors["char"])
char.shape("circle")
char.turtlesize(1.75)
########################################################################################################################
########################################################################################################################
#Food creation

def makefood(num):
  for i in range(num):
    food.append(turtle.Turtle())
    food[-1].shape("triangle")
    food[-1].turtlesize(1)
    food[-1].penup()
    food[-1].color(colors["food3"])
    toggle = True
    while toggle:
      food[-1].goto(random.randint(-290, 290), random.randint(-290, 290))
      if (math.pow(abs(char.xcor() - food[-1].xcor()),2) + math.pow(abs(char.ycor() - food[-1].ycor()),2))>=10000:
        toggle = False
      for i in range(len(food)):
        if (math.pow(abs(food[i].xcor() - food[-1].xcor()),2) + math.pow(abs(food[i].ycor() - food[-1].ycor()),2))>=1000:
          toggle = False
    foodHealth.append(3)

food = []
foodHealth = []
makefood(5)

#Bot Creation
def spawnbot(num):
  for i in range(num):
    while True:
      loc = [random.randint(-281, 281), random.randint(-281, 281)]
      if (math.pow(abs(char.xcor() - loc[0]),2) + math.pow(abs(char.ycor() - loc[1]),2))<=10000:
        pass
      else:
        break
    botsM.append(turtle.Turtle())
    botsM[-1].penup()
    botsM[-1].goto(loc)
    botsM[-1].color(colors["charM"])
    botsM[-1].shape("triangle")
    botsM[-1].turtlesize(1)
    botsM[-1].setheading(botsM[-1].towards(char.pos()))
    botsM[-1].fd(20)
    bots.append(turtle.Turtle())
    bots[-1].shape("circle")
    bots[-1].turtlesize(1.75)
    bots[-1].penup()
    bots[-1].color(colors["bot"])
    bots[-1].goto(loc)
    bots[-1].setheading(bots[-1].towards(char.pos()))
    botsHealth.append(5)
    botsRest.append(0)

bots = []
botsM = []
botsHealth = []
botsRest = []
makefood(5)
########################################################################################################################
########################################################################################################################

def spawn_ball(reference):
  ammo.append(turtle.Turtle())
  ammo[-1].shape("circle")
  ammo[-1].turtlesize(0.75)
  ammo[-1].penup()
  ammo[-1].setposition(reference.position())
  ammo[-1].setheading(reference.heading())
  ammo[-1].fd(30)
  ammo[-1].color(colors["char"])

hearts = turtle.Turtle()
hearts.hideturtle()
hearts.penup()
hearts.goto(260, -317)
hearts.pendown()
hearts.color(colors["heart"])
hearts.write("Health", False, align="center", font=('Impact', 10, 'normal'))
def healthBar(num):
  hearts.penup()
  hearts.goto(290, -340)
  hearts.color('black')
  hearts.pendown()
  for i in range(round(num[0])):
    hearts.begin_fill()
    if i < num[1]:
      hearts.fillcolor(colors["heart"])
    else:
      hearts.fillcolor("grey")
    hearts.left(50)
    hearts.forward(16)
    hearts.circle(6, 200)
    hearts.right(140)
    hearts.circle(6, 200)
    hearts.forward(16)
    hearts.end_fill()
    hearts.penup()
    hearts.goto(hearts.xcor()-30, hearts.ycor())
    hearts.pendown()
    hearts.setheading(0)
health = [3,3]
healthBar(health)

#Title & Level Bar
levelVal = 0
level = turtle.Turtle()
level.hideturtle()
def levelBar(num):
  level.clear()
  level.penup()
  level.goto(-260, -317)
  level.pendown()
  level.color(colors["green"])
  level.write("Level " + str(score), False, align="center", font=('Impact', 10, 'normal'))
  level.penup()
  level.goto(-310, -330)
  level.color('black')
  level.pendown()
  for i in range(10):
    level.begin_fill()
    if i < num:
      level.fillcolor(colors["green"])
    else:
      level.fillcolor("grey")
    for i in range(4):
      level.left(90)
      level.forward(10)
    level.end_fill()
    level.penup()
    level.goto(level.xcor()+12, level.ycor())
    level.pendown()
    level.setheading(0)
levelBar(levelVal)
########################################################################################################################
########################################################################################################################
# Functions on Press
charSpeed = 0
def left():
  charMove(-1,0)
def down():
  charMove(0,-1)
def right():
  charMove(1,0)
def up():
  charMove(0,1)
def autoToggle():
  global autoAim
  if autoAim == False:
    autoAim = True
  elif autoAim == True:
    autoAim = False
def charMove(x,y):
  global charSpeed
  if charSpeed < 1.5:
    charSpeed += 0.04
  if -281 <= char.xcor()+charSpeed*x <= 281 and -281 <= char.ycor()+charSpeed*y <= 281:
    char.goto(char.xcor()+charSpeed*x, char.ycor()+charSpeed*y)
    charM.goto(charM.xcor() + charSpeed * x, charM.ycor() + charSpeed * y)
    #eating with char
    for i in range(len(food)):
      if abs(char.xcor() - food[i].xcor()) < 20 and abs(char.ycor() - food[i].ycor()) < 20:
        #remove food
        global health, levelVal, score, spawn_interval, ball_speed, botsHealth, bots
        health[1] -= foodHealth[i] /5
        foodHealth.pop(i)
        food[i].hideturtle()
        food.pop(i)
        #level
        if levelVal < 10:
          levelVal += 1
        else:
          if score < 40:
            score += 1
            if score % 2 == 0:
              spawnbot(int(round(score / 2)))
            if score in [3, 6, 10]:
              health = [health[0] + 1, health[1]]
              healthBar(health)
            spawn_interval = 0.5 - score / 40
            ball_speed = 2 + score / 5
            levelVal = 0
        levelBar(levelVal)
        if len(food) < 30:
          makefood(random.randint(1, 2))
        else:
          makefood(1)
        healthBar(health)
    #hitting bot
    for i in range(len(bots)):
      if (math.pow(abs(char.xcor() - bots[i].xcor()),2) + math.pow(abs(char.ycor() - bots[i].ycor()),2))<=700:
        botsHealth.pop(i)
        bots[i].hideturtle()
        bots.pop(i)
        botsM[i].hideturtle()
        botsM.pop(i)
        health[1] -= 5
        healthBar(health)
        break
def shoot(x,y):
  angle = char.towards(x, y)
  char.setheading(angle)
  charM.goto(char.pos())
  charM.setheading(angle)
  charM.fd(20)

frame_rate = 100
time_per_frame = 1 / frame_rate


#window.bgpic("diepbg.jpeg")
window.onkeypress(autoToggle, " ")
invis.ondrag(shoot)
invis.onclick(shoot)
window.listen()

# Main animation loop
spawn_timer = time.time()

########################################################################################################################
########################################################################################################################

while health[1]>0:
  # in general, use condition with while loop but turtle can have exceptions
  frame_start_time = time.time()
  # Spawn new ball`
  if time.time() - spawn_timer > spawn_interval:
    spawn_ball(char)
    spawn_timer = time.time()
  ran = False
  if keyboard.is_pressed('Up'):
    up()
    ran = True
  if keyboard.is_pressed('Left'):
    left()
    ran = True
  if keyboard.is_pressed('Right'):
    right()
    ran = True
  if keyboard.is_pressed('Down'):
    down()
    ran = True
  if ran != True:
    charSpeed = 0

  for i in range(len(bots)):
    #flip on edge
    if bots[i].xcor() >= 281 or bots[i].ycor() >= 281 or bots[i].ycor() <= -281 or bots[i].xcor() <= -281:
      botsM[i].setheading(botsM[i].towards(char.pos()))
      bots[i].setheading(botsM[i].towards(char.pos()))
      botsM[i].goto(bots[i].pos())
      botsM[i].fd(20)
    bots[i].forward(ball_speed*2/3)
    botsM[i].forward(ball_speed*2/3)
    #If bot hits char
    if (math.pow(abs(char.xcor() - bots[i].xcor()),2) + math.pow(abs(char.ycor() - bots[i].ycor()),2))<=700:
      botsHealth.pop(i)
      bots[i].hideturtle()
      bots.pop(i)
      botsM[i].hideturtle()
      botsM.pop(i)
      health[1] -= 5
      healthBar(health)
      break
  # Move all ammo and clear ammo that leave the screen
  for ball in ammo.copy():
    ball.forward(ball_speed)
    #
    # Check if ball has hit a screen edge and remove
    if (abs(ball.xcor()) > 295 or abs(ball.ycor()) > 295):
      ball.hideturtle()
      ammo.remove(ball)
      break
    # Check if ball has hit bot
    for i in range(len(bots)):
      if (math.pow(abs(ball.xcor() - bots[i].xcor()),2) + math.pow(abs(ball.ycor() - bots[i].ycor()),2))<=800:
        #if not dead
        if botsHealth[i] !=1:
          botsHealth[i] -= 1
        else:
          #if destroyed
          botsHealth.pop(i)
          bots[i].hideturtle()
          bots.pop(i)
          botsM[i].hideturtle()
          botsM.pop(i)
        #remove ammo
        ball.hideturtle()
        ammo.remove(ball)
        break
    # Check if ball has hit a food
    for i in range(len(food)):
      if (math.pow(abs(ball.xcor() - food[i].xcor()),2) + math.pow(abs(ball.ycor() - food[i].ycor()),2))<=45:
        #if not dead yet
        if foodHealth[i] !=1:
          foodHealth[i] -=1
          food[i].color(colors["food"+str(foodHealth[i])])
        else:
        #if eaten
          foodHealth.pop(i)
          food[i].hideturtle()
          food.pop(i)
          if len(food) < 30:
            makefood(random.randint(1, 2))
          #regen
          if health[0] > health[1]:
            health[1] += 1
            healthBar(health)
          else:
            makefood(1)
          #level
          if levelVal <10:
            levelVal += 1
          else:
            if score < 40:
              score += 1
              if score%2 == 0:
                spawnbot(int(round(score/2)))
              if score in [3,6,10]:
                health=[health[0]+1,health[1]]
                healthBar(health)
              spawn_interval = 0.5 - score / 40
              ball_speed = 2 + score / 5
              levelVal = 0
          levelBar(levelVal)
        #remove ammo
        ball.hideturtle()
        ammo.remove(ball)
        break
  window.update()
  frame_time = time.time() - frame_start_time
  if frame_time < time_per_frame:
    time.sleep(time_per_frame - frame_time)
message = turtle.Turtle()
message.color(colors["heart"])
message.write("You Died!", False, align="center", font=('Impact', 50, 'normal'))
turtle.done()