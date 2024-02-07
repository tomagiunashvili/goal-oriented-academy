from turtle import *


#we want to paint a house

#stet 1: draw a square
speed(100)
width(7)
color('orange')
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color ("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()






penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

penup()
goto(65, 110)
pendown()

color("black")
left(30)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)





#drawing a window

penup()
goto(135, 50)
pendown()

color("black")
begin_fill
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
end_fill()

#drawing a window


penup()
goto(6, 110)
pendown()

color("black")
forward(58)
right(90)
forward(30)
right(90)
forward(57)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

exitonclick()