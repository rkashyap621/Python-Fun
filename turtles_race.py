import turtle
import random

colors = ["violet", "turquoise", "SkyBlue", "chartreuse", "gold", "tomato", "firebrick"]
race_start = True
winner_turtle_color= 0
colors_str=""
for color in colors:
    colors_str += color
    if color == colors[-2]:
        colors_str += " and "
    if color!= colors[-2] and color!= colors[-1]:
        colors_str += ", "


jon = turtle.Turtle()
jon.color(colors[0])
jill = turtle.Turtle()
jill.color(colors[1])
jake = turtle.Turtle()
jake.color(colors[2])
bill = turtle.Turtle()
bill.color(colors[3])
may = turtle.Turtle()
may.color(colors[4])
gin = turtle.Turtle()
gin.color(colors[5])
ken = turtle.Turtle()
ken.color(colors[6])

race_helper= turtle.Turtle()
race_helper.color("white")
race_helper.shape("turtle")
race_helper.hideturtle()

turtles = (jon, jill, jake, bill, may, gin, ken)

screen = turtle.Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.setup(width = 800, height = 800)
height=screen.window_height()/2-100
width=screen.window_width()/2-100
race_helper.setheading(270)
race_helper.penup()
race_helper.setpos(width, height+100)
race_helper.pendown()
race_helper.forward((height*2)+205)

num_turtles = int(input("How many turtles do you want in race?(min: 2 and max:7):\n"))

race_turtles = []
turtle_colors= []
while len(race_turtles) < num_turtles:
    for i in range(num_turtles):
        turtle_selected = random.choice(turtles)
        if turtle_selected not in race_turtles and len(race_turtles) < num_turtles:
            race_turtles.append(turtle_selected)
            turtle_colors.append(turtle_selected.color()[0])

height *= -1

print(f"The colors of the race turtles are ({turtle_colors}):).")
user_bet = input("Welcome to Turtle Race!\nWhich turtle color would you bet will win the race?:\n")

for i in range(num_turtles):
    race_turtles[i].shape("turtle")
    race_turtles[i].penup()
    race_turtles[i].setpos((-1*width), height)
    race_turtles[i].pos()
    height+=100

while race_start:
    for turtle in race_turtles:
        distance = random.randint(1,10)
        if turtle.pos()[0] > width:
            winner_turtle_color= turtle.pencolor()
            race_start = False
        else:
            turtle.forward(distance)


if user_bet == str(winner_turtle_color):
    print("You win!")
else:
    print("You lose!")
print(f"The winner turtle color is {winner_turtle_color}!")

screen.exitonclick()
