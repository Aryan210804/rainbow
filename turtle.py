import turtle
t = turtle.Turtle()
turtle.bgcolor('#91C8E4')
color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
t.speed(0)  
for i in range(55555):
    t.pencolor(color[i % len(color)])
    t.width(i / 1000 + 20)
    t.forward(i)
    t.right(51)
turtle.done()
