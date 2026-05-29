import turtle as t
import random

t.colormode(255)

def turtle_colors():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    colors=(red, green, blue)
    return colors

def draw_n_circles(turtle, num_circles):
     steps = int(360 / num_circles)
     orientation = 0
     while orientation<360:
         turtle.color(turtle_colors())
         turtle.setheading(orientation)
         turtle.circle(100)
         orientation += steps

bob = t.Turtle()
bob.shape("turtle")
bob.turtlesize(1.5)
draw_n_circles(bob, 7)

screen.exitonclick()
