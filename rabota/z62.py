import turtle
    size=int(input("Введите радиус первого круга:"))
turtle.shape("turtle")
turtle.speed(5)
i = 0
while i < 9:
 turtle.circle(size)
 size = size+10
 i += 1