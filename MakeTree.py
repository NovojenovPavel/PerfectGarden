import turtle as t
import random


def draw(command):
    t.tracer(0)
    stack = []
    t.left(90)

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
                t.pencolor('green')
                t.forward(length+mutation(length, mutation_len_scale))
                t.pencolor('black')
            case "[":
                stack.append(t.xcor())
                stack.append(t.ycor())
                stack.append(t.heading())
                t.left(angle+mutation(angle, mutation_angle_scale))
            case "]":
                t.penup()
                t.setheading(stack.pop())
                t.sety(stack.pop())
                t.setx(stack.pop())
                t.pendown()
                t.right(angle+mutation(angle, mutation_angle_scale))
    t.hideturtle()
    t.update()
    t.mainloop()


def create(i, axiom):
    for i in range(i):
        axiomtp = ""
        for el in axiom:
            if el in translate:
                axiomtp += translate[el]
            else: axiomtp += el
        axiom = axiomtp
    return axiom

def makepicture():
    seed = create(depth, "0")
    print(seed)
    draw(seed)

def mutation(value, scale):
    return random.randint(int(-value*scale), int(value*scale))

def randintvalue(a, b):
    return random.randint(a,b)

# axiom = "0"
translate = {
    "0": "1[0]0",
    "1": "12",
}

length = 10
angle = 15
depth = 10
mutation_len_scale = 0.5
mutation_angle_scale = 0.5
reducing_chance_percent = 30


makepicture()
