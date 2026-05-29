import turtle as t
import random

t.colormode(255)

def turtle_colors():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    colors=(red, green, blue)
    return colors

rakku = t.Turtle()
rakku.shape("turtle")
rakku.turtlesize(1.5)
rakku.hideturtle()
rakku.speed("fastest")
rakku.pensize(5)
direction = [-20, 20]
orientation = [0, 90, 180, 270]
distance = 0

screen = t.Screen()
screen.bgcolor("black")

while True:
    arbiter=random.randint(1, 500)
    direction_choice=random.choice(direction)
    orientation_choice=random.choice(orientation)
    rakku.color(turtle_colors())
    if arbiter%random.randint(1,arbiter) == 0:
        rakku.forward(direction_choice)
        rakku.setheading(orientation_choice)
    else:
        rakku.backward(direction_choice)
        rakku.setheading(orientation_choice)
    if abs(rakku.position()[0]) > screen.canvwidth or abs(rakku.position()[1]) > screen.canvheight:
        rakku.penup()
        rakku.home()
        rakku.pendown()

screen.exitonclick()
