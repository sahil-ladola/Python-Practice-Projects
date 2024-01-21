from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def anti_clock():
    tim.setheading(tim.heading() + 10)


def clock():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
# screen.onkey(move_forward, "w")
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=anti_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
