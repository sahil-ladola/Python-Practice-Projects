import random
import turtle as t

t.colormode(255)
timmy = t.Turtle()

timmy.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# timmy.left(180)

# dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()

# different shapes
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# for i in range(3, 11):
#     timmy.color(random.choice(colors))
#     ang = 360 / i
#     j = 0
#     while j < i:
#         timmy.forward(50)
#         timmy.left(ang)
#         j += 1

# random walk
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# direction = [0, 90, 180, 270]
# timmy.pensize(7)
# for _ in range(160):
#     timmy.forward(16)
#     timmy.color(random_color())
#     timmy.setheading(random.choice(direction))

# spirograph
def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(4)

# from turtle import Screen


screen = t.Screen()
screen.exitonclick()
