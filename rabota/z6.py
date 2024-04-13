import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Circle Art")
t = turtle.Turtle()
t.speed(0) 

def draw_circle(r, color):
    t.color(color)
    t.circle(r)

radius=int(input("Введите радус первого круга:"))
num_circles = 4
color = ["blue", "orange", "green", "red"]

for i in range(num_circles):
    draw_circle(radius, color[i % len(color)])
    radius += 10
    t.penup()
    t.right(45) 
    t.forward(3)
    t.left(45)
    t.pendown()

screen.exitonclick()
