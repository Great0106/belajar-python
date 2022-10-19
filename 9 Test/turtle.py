from turtle import*
turtle = Turtle()
screen = Screen()
turtle.bgcolour(100, 100, 255)
turtle.pencolor(0, 0, 255)
turtle.width(5)
turtle.speed(100)

loops = int(input("How many loops?"))
degree = int(input("How many degrees?"))
for i in range(int(loops)):
    turtle.forward(90)
    turtle.left(degree)