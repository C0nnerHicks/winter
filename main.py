import turtle

import turtle

screen =  turtle.Screen()
screen. bgcolor("sky blue")
T_ground = turtle.Turtle()
T_ground.penup()
T_ground.pencolor("white")
T_ground.fillcolor("white")
T_ground.speed(0)
T_ground.goto(1000,-10000)
T_ground.pendown()
T_ground.begin_fill()
T_ground.goto(1000, 100)
T_ground.goto(1000,-100)
T_ground.goto(-1000,100)
T_ground.end_fill()
screen = turtle.Screen()
screen.bgcolor("sky blue")
tree = turtle.Turtle()
tree.speed(0)

def draw_triangle(color, size, y_pos):
   tree.penup()
   tree.goto(-size / 2, y_pos)
   tree.pendown()
   tree.begin_fill()
   tree.fillcolor(color)
   for _ in range(3):
       tree.forward(size)
       tree.left(120)
   tree.end_fill()
def draw_trunk():
   tree.penup()
   tree.goto(-20, -50)
   tree.pendown()
   tree.begin_fill()
   tree.fillcolor("brown")
   for _ in range(2):
       tree.forward(40)
       tree.left(90)
       tree.forward(60)
       tree.left(90)
   tree.end_fill()
def draw_message():
   tree.penup()
   tree.goto(-150, -120)
   tree.pendown()
   tree.color("red")
   tree.write("Merry Christmas!", font=("Arial", 24, "bold"))
draw_triangle("green", 200, 0)  # Top layer
draw_triangle("green", 180, 50)  # Middle layer
draw_triangle("green", 160, 100)  # Bottom layer
draw_trunk()
draw_message()
tree.hideturtle()
import turtle
dot_turtle = turtle.Turtle()
dot_turtle.shape("turtle")
dot_turtle.speed(0)
dot_turtle.color("white")
def draw_white_dots(number_of_dots):
   for _ in range(number_of_dots):
       dot_turtle.penup()
       dot_turtle.goto(random_position())
       dot_turtle.dot(5)
import random
def random_position():
   x = random.randint(-300, 300)
   y = random.randint(-300, 300)
   return x, y
draw_white_dots(100)
dot_turtle.hideturtle()
import turtle

def draw_branch(t, length, level):
    if level == 0:
        t.forward(length)
        return
    length /= 3.0
    draw_branch(t, length, level - 1)
    t.left(60)
    draw_branch(t, length, level - 1)
    t.right(120)
    draw_branch(t, length, level - 1)
    t.left(60)
    draw_branch(t, length, level - 1)

def draw_small_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")

    snowflake.penup()
    snowflake.goto(-50, 30)
    snowflake.pendown()

    for _ in range(3):
        draw_branch(snowflake, 100, 3)
        snowflake.right(120)

    snowflake.hideturtle()
    screen.mainloop()

draw_small_snowflake()