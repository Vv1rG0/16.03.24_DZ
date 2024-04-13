import turtle
start_radius=int(input("Введите радиус первого круга: "))
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Circle Art")
t = turtle.Turtle()
t.speed(0)

def draw_circle(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.color(color)
    t.circle(r)

num_circles = 4
circle_spacing = 0
colors = ["blue", "orange", "green", "red"]

start_x = -(num_circles - 1) * circle_spacing / 2

for i in range(num_circles):
    draw_circle(start_x + i * circle_spacing, 0, start_radius + 10*i, colors[i % len(colors)])

screen.exitonclick()