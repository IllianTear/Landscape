import turtle
kvothe = turtle.Turtle()
snc = turtle.Screen()
Kylar = turtle.Turtle()
snc = turtle.Screen()
lee = turtle.Turtle()
snc = turtle.Screen()
bob = turtle.Turtle()
kvothe.color("yellow")
kvothe.penup()
kvothe.goto(-225,150)
kvothe.pendown()
kvothe.begin_fill()
kvothe.circle(75)
kvothe.end_fill()

Kylar.color("green")
Kylar.penup()
Kylar.goto(-400, 25)
Kylar.pendown()
Kylar.begin_fill()
Kylar.forward(800)
Kylar.right(90)
Kylar.forward(600)
Kylar.right(90)
Kylar.forward(800)
Kylar.right(90)
Kylar.forward(600)
Kylar.end_fill()

lee.color("gray")
lee.penup()
lee.goto(50, 0)
lee.pendown()
lee.begin_fill()
lee.forward(125)
lee.left(90)
lee.forward(150)
lee.left(90)
lee.forward(125)
lee.left(90)
lee.forward(150)
lee.end_fill()
lee.backward(150)
lee.color("brown")
lee.begin_fill()
lee.right(225)
lee.forward(72)
lee.right(45)
lee.forward(40)
lee.right(57)
lee.forward(60)
lee.end_fill()

bob.penup()
bob.goto(75, 30)
bob.pendown()
def square():
    for i in range(4):
        bob.forward(25)
        bob.left(90)
square()
bob.penup()
bob.goto(100, 30)
bob.pendown()
square()
bob.penup()
bob.goto(25, 15)
bob.pendown()
bob.begin_fill()
bob.forward(25)
bob.right(90)
bob.forward(25)
bob.right(90)
bob.forward(25)
bob.right(90)
bob.forward(25)
bob.backward(15)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(15)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(15)
bob.right(90)
bob.forward(50)
bob.end_fill()
bob.color("gray")
bob.penup()
bob.goto(-15, -20)
bob.pendown()
bob.circle(6)
bob.penup()
bob.goto(30, -20)
bob.pendown()
bob.circle(6)

turtle.exitonclick()