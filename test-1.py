    #space invaders
import math
import os
import turtle
import random
#screen setup
sc = turtle.Screen()
sc.bgcolor("black")
sc.title("v@d3rZ")
#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player
pl = turtle.Turtle()
pl.color("yellow")
pl.shape("triangle")
pl.penup()
pl.speed(0)
pl.setposition(0, -250)
pl.setheading(90)

playerspeed = 15

#create the  enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 5
#choose number of enemies
number_of_enemies = 5
#create a empty list of enemies 
enemies = []
#add enemies to list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setpos(-250, 200)
    
#create the players bullet 
bullet  = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,  0.5)
bullet.hideturtle()

bulletspeed = 15

# define bullet state
##ready - ready to fire
###fire - bullet is firing

bulletstate = "ready"


#move the player left and right
def move_left():
    x = pl.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    pl.setx(x)

def move_right():
    x = pl.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    pl.setx(x)

def fire_bullet():
    #define bullet state if it needs changed'
    global bulletstate
    if bulletstate == "ready":
         bulletstate == "fire"
         #move bullet to just above player
    x = pl.xcor()
    y = pl.ycor() +10
    bullet.setposition(x, y)
    bullet.showturtle()
    
def iscollision(t1, t2):
    distance = t1.distance(t2)
    if distance < 15:
        return True
    else:
        return False
   


#create keyboard binding
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,'Up')



#main game loop



while True:
   for enemy in enemies:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)



    #Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -=20
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -=20
        enemyspeed *= -1
        enemy.sety(y)
    
    if iscollision(bullet , enemy):
        #reset the bullet 
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
       #reset enemy
        enemy.setposition(-200,250)
        
    if iscollision(pl, enemy):
        pl.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
    
    # move the bullet
    #if bulletstate == "fire":
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
#check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"   
# #check to see if there was a collision with the enemy and the bullet
    
   #delay = input("Press enter to quit")
    















