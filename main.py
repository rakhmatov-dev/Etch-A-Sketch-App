import random
import turtle
from turtle import Turtle, Screen

color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]
turtle.colormode(255)

mo = Turtle()
mo.pensize(15)
screen = Screen()
screen.title("Etch-A-Sketch")


def move_forwards():
    mo.forward(10)


def move_backwards():
    mo.backward(10)


def turn_left():
    mo.lt(10)


def turn_right():
    mo.rt(10)


def reset():
    mo.clear()
    mo.penup()
    mo.home()
    mo.pendown()


def change_color():
    mo.color(random.choice(color_list))


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.onkey(key="space", fun=change_color)

screen.exitonclick()