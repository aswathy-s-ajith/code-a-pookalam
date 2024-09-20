import turtle

s = turtle.Turtle()
s.speed(200)


s.penup()  
s.sety(s.ycor() - 200)
s.color('#b31b1b')
s.begin_fill()
s.circle(180)
s.end_fill()


s.penup() 
s.sety(s.ycor() + 180)  
s.setx(0)  
s.pendown()

s.color('#FF0000')
s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
s.end_fill()


s.left(30)
s.color('#FF4500')
s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
s.end_fill()

s.left(30)
s.color('#FFdb49')
s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
s.end_fill()

s.left(30)
s.color('white')
s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
s.end_fill()


s.color('white')
s.begin_fill()
s.forward(110)
s.left(90)
s.circle(110)
s.end_fill()

s.sety(s.ycor() -110)

s.color('#b31b1b')
s.begin_fill()
s.pencolor('#b31b1b')


def draw_petal(radius):
    for _ in range(2):
        s.circle(radius, 90)  
        s.left(90)


def draw_flower_with_circle(num_petals, petal_radius, radius):
    
    for _ in range(num_petals):
        draw_petal(radius)  
        s.left(360 / num_petals)


draw_flower_with_circle(10, 10, 80)
s.end_fill()


s.color('#c74e4e')
s.pencolor('#b31b1b')
s.begin_fill()
draw_flower_with_circle(20, 5, 70)
s.end_fill()


s.color('#4ec74e')
s.pencolor('white')
s.begin_fill()
draw_flower_with_circle(20, 5, 60)
s.end_fill()


s.color('red')
s.pencolor('red')
s.begin_fill()
s.forward(65)
s.left(90)
s.circle(65)
s.end_fill()





s.penup()
s.left(90)  
s.forward(65) 
s.right(90) 
s.forward(65) 
s.pendown()
s.sety(s.ycor() +65)


s.color('#fcf03d')
s.begin_fill()
s.forward(50)
s.left(90)
s.circle(50)
s.end_fill()



s.penup()
s.left(90)  
s.forward(50)
s.right(90)  
s.forward(50) 
s.pendown()
s.setx(s.xcor() -50)

s.pencolor('maroon')
draw_flower_with_circle(30, 5, 20)


s.hideturtle()
turtle.done()
