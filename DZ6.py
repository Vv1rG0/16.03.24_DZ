import turtle
def draw_star(n):
    turtle.penup()
    turtle.goto(0, 0) 
    turtle.pendown()

    for i in range(n):
        turtle.forward(200)
        turtle.left(180 - 180 / n)
draw_star(9)
turtle.done()