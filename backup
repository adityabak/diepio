import time
import turtle
import random
import math

colors = {"char":(179,224,255),"charM":(156,158,159),"food3":(73, 118, 205),"food2":(113, 158, 235),"food1":(153, 198, 255),"heart":(229, 116, 121)}
turtle.colormode(255)
score = 1
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
    food[-1].goto(random.randint(-300, 300), random.randint(-300, 300))
    foodHealth.append(3)

food = []
foodHealth = []
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

def healthBar(num):
  hearts = turtle.Turtle()
  hearts.hideturtle()
  hearts.penup()
  hearts.goto(290, -330)
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
########################################################################################################################
########################################################################################################################
# Functions on Press
charSpeed = 10
def left():
  charMove(-1,0)
def down():
  charMove(0,-1)
def right():
  charMove(1,0)
def up():
  charMove(0,1)
def charMove(x,y):
  if -281 <= char.xcor()+charSpeed*x <= 281 and -281 <= char.ycor()+charSpeed*y <= 281:
    char.goto(char.xcor()+charSpeed*x, char.ycor()+charSpeed*y)
    charM.goto(charM.xcor() + charSpeed * x, charM.ycor() + charSpeed * y)
    for i in range(len(food)):
      if abs(char.xcor() - food[i].xcor()) < 20 and abs(char.ycor() - food[i].ycor()) < 20:
        health[1] -= foodHealth[i] /5
        foodHealth.pop(i)
        food[i].hideturtle()
        food.pop(i)
        if len(food) < 30:
          makefood(random.randint(1, 2))
        else:
          makefood(1)
        healthBar(health)
def shoot(x,y):
  angle = char.towards(x, y)
  char.setheading(angle)
  charM.goto(char.pos())
  charM.setheading(angle)
  charM.fd(20)

frame_rate = 100
time_per_frame = 1 / frame_rate


#window.bgpic("diepbg.jpeg")
window.onkeypress(left, "a")
window.onkeypress(down, "s")
window.onkeypress(up, "w")
window.onkeypress(right, "d")
invis.ondrag(shoot)
invis.onclick(shoot)
window.listen()

# Main animation loop
spawn_timer = time.time()

########################################################################################################################
########################################################################################################################

while True:
  # in general, use condition with while loop but turtle can have exceptions
  frame_start_time = time.time()
  if health[1] <= 0:
    exit()
  # Spawn new ball
  if time.time() - spawn_timer > spawn_interval:
    spawn_ball(char)
    spawn_timer = time.time()
  # Move all ammo and clear ammo that leave the screen
  for ball in ammo.copy():
    ball.forward(ball_speed)
    #Bot
    #
    #char.setheading(char.towards(int(food[0].xcor()),int(food[0]. cor())))
    #
    # Check if ball has hit a screen edge and remove
    if (abs(ball.xcor()) > 295 or abs(ball.ycor()) > 295):
      ball.hideturtle()
      ammo.remove(ball)
    # Check if ball has hit a food
    for i in range(len(food)):
      if (math.pow(abs(ball.xcor() - food[i].xcor()),2) + math.pow(abs(ball.ycor() - food[i].ycor()),2))<=40:
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
        #Score increase
          if score < 70:
            score += 1
            spawn_interval = 0.5 - score /80
            ball_speed = 2 + score/10
        #remove ammo
        ball.hideturtle()
        ammo.remove(ball)
        break

  window.update()
  frame_time = time.time() - frame_start_time
  if frame_time < time_per_frame:
    time.sleep(time_per_frame - frame_time)