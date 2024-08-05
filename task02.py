import turtle
import math

def draw_tree(branch_length, angle, level):
    if level > 0:
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        turtle.left(2 * angle)
        draw_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

        turtle.right(angle)
        turtle.backward(branch_length)


level = int(input("Введіть рівень рекурсії: "))

screen = turtle.Screen()
screen.bgcolor("white")

turtle.left(90)
turtle.penup()
turtle.goto(0, -screen.window_height() // 2)
turtle.pendown()
turtle.speed(0)

draw_tree(100, 30, level)

turtle.done()
