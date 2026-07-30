import turtle

screen = turtle.Screen()
screen.title("Square Drawer")

pen = turtle.Turtle()
pen.speed(3)

for _ in range(4):
    pen.forward(100)
    pen.left(90)

screen.mainloop()
