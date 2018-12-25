import turtle
#creating gui with turtle
turtoise = turtle.Turtle()
turtoise.ht()
turtoise.setpos(200,200)
turtoise.color("#000000")
window = turtle.Screen()
window.screensize(400,400,"red")
turtoise.setpos(200,250)
turtoise.setpos(300,250)
turtoise.setpos(300,200)
turtoise.setpos(200,200)
if turtle.onclick(200,200):
    turtle.forward(100)
def click(x,y,x1,y1,x2,y2):
    if turtle.onclick():        
        if turtoise.xcor() >= x1 and turtoise.xcor() <= x2:
            turtoise.color("#ff0000")
            turtoise.setpos(200,250)
            turtoise.setpos(300,250)
            turtoise.setpos(300,200)
            turtoise.setpos(200,200)
click(200,200,300,250)
#window.exitonclick()
