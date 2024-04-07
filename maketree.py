import turtle
import turtle as t
import random
from tkinter import *


length = 10
angle = 15
depth = 10

# Mutation
mutation_len_scale = 0.5
mutation_angle_scale = 0.5
reducing_chance_percent = 30

# Colours
leaf_colours = [
    "#175c00",
    "#30731a",
    "#006108"
]

wood_colours = [
    "#261400",
    "#381d00",
    "#613200"
]

# Thick
start_thick = 16
mutation_wood_thick = 0.3
leaf_thick = 10
mutation_leaf_thick = 0.5


def draw(command):
    t.tracer(0)
    stack = []
    t.left(90)
    thick = start_thick
    t.pensize(thick)

    t.penup()
    t.goto(0, -300)
    t.pendown()

    for el in command:
        match el:
            case "1":
                t.forward(length+mutation(length, mutation_len_scale))
            case "2":
                if randintvalue(0, 100) > 50:
                    t.forward(length)
            case "0":
                t.pensize(leaf_thick+mutation(leaf_thick, mutation_leaf_thick))
                t.pencolor(leaf_colours[randintvalue(0, len(leaf_colours)-1)])
                t.forward(length+mutation(length, mutation_len_scale))
                t.pencolor(wood_colours[randintvalue(0, len(wood_colours)-1)])
                t.pensize(thick)
            case "[":
                thick = (thick * 0.75) + mutation(thick, mutation_wood_thick)
                t.pensize(thick)
                stack.append(thick)
                stack.append(t.xcor())
                stack.append(t.ycor())
                stack.append(t.heading())
                t.left(angle+mutation(angle, mutation_angle_scale))
            case "]":
                t.penup()
                t.setheading(stack.pop())
                t.sety(stack.pop())
                t.setx(stack.pop())
                thick = stack.pop()
                t.pensize(thick)
                t.pendown()
                t.right(angle+mutation(angle, mutation_angle_scale))
    t.hideturtle()
    t.update()



def create(i, axiom):
    for i in range(i):
        axiomtp = ""
        for el in axiom:
            if el in translate:
                axiomtp += translate[el]
            else:
                axiomtp += el
        axiom = axiomtp
    return axiom


def savepicture(lable):
    ts = turtle.getscreen()
    seed = create(depth, "0")
    print(seed)
    draw(seed)
    ts.getcanvas().postscript(file=lable+".eps")


def makepicture():
    seed = create(depth, "0")
    print(seed)
    draw(seed)
    t.mainloop()


def mutation(value, scale):
    return random.randint(int(-value*scale), int(value*scale))


def randintvalue(a, b):
    return random.randint(a, b)


# axiom = "0"
translate = {
    "0": "1[0]0",
    "1": "12",
}

makepicture()
