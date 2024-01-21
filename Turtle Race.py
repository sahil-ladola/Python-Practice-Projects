from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False


screen.setup(width=500, height=500)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_pos = [200, 142, 84, 26, -32, -90, -148]
turtles = []

for index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_pos[index])
    turtles.append(new_turtle)

user_prediction = screen.textinput(title="Make your prediction", prompt="Which turtle will win the race? Enter color: ")

if user_prediction:
    is_race_on = True

while is_race_on:
    for tur in turtles:
        if tur.xcor() > 230:
            is_race_on = False
            won_tur = tur.pencolor()
            if won_tur == user_prediction:
                print(f"You've Won! The {won_tur} turtle is the winner")
            else:
                print(f"You've lost! The {won_tur} turtle is the winner")
            random_dis = random.randint(0, 7)
            tur.forward(random_dis)
screen.exitonclick()



# red = Turtle()
# red.shape("turtle")
# red.color("red")
# red.penup()
# red.goto(x=-230, y=200)
#
# orange = Turtle()
# orange.shape("turtle")
# orange.color("orange")
# orange.penup()
# orange.goto(x=-230, y=142)
#
# yellow = Turtle()
# yellow.shape("turtle")
# yellow.color("yellow")
# yellow.penup()
# yellow.goto(x=-230, y=84)
#
# green = Turtle()
# green.shape("turtle")
# green.color("green")
# green.penup()
# green.goto(x=-230, y=26)
#
# blue = Turtle()
# blue.shape("turtle")
# blue.color("blue")
# blue.penup()
# blue.goto(x=-230, y=-32)
#
# indigo = Turtle()
# indigo.shape("turtle")
# indigo.color("indigo")
# indigo.penup()
# indigo.goto(x=-230, y=-90)
#
# violet = Turtle()
# violet.shape("turtle")
# violet.color("violet")
# violet.penup()
# violet.goto(x=-230, y=-148)
