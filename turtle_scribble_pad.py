import turtle
import turtle as Turtle_Module

def move_forward():
    bob.forward(10)
def move_backward():
    bob.backward(10)
def turn_clockwise():
    current_heading = bob.heading()
    bob.setheading(current_heading+5)
def turn_counterclockwise():
    current_heading = bob.heading()
    bob.setheading(current_heading-5)
def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()

screen=Turtle_Module.Screen()

bob=Turtle_Module.Turtle()
bob.shape("turtle")
bob.color("red")

screen.onkey(move_forward,"d")
screen.onkey(move_backward,"a")
screen.onkey(turn_clockwise,"s")
screen.onkey(turn_counterclockwise,"w")
screen.onkey(clear,"c")
screen.listen()

screen.exitonclick()
