###
# Draw a square
#

import turtle


def draw_square(pen, length):
    # Draw the square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    # Hide the turtle
    pen.hideturtle()


def draw_trangle(pen, length):
        # Draw the trangle
    for i in range(3):
        pen.forward(length)
        pen.left(120)

    # hide the turtle
    pen.hideturtle()


def draw_rectangle(pen, length_a, length_b):
    # Draw the rectangle
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

    pen.hideturtle()

"""
if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(5)

    draw_square(90)
    draw_trangle(100)
    draw_rectangle(100, 50)
"""