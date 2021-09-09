#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
turtle.clear()
turtle.color("black")
turtle.up()
turtle.goto(33, 190)
turtle.down()
turtle.goto(56,240)
turtle.goto(76,100)
turtle.goto(60,120)
turtle.up()
turtle.goto(-85,190)
turtle.down()
turtle.goto(-120,240)
turtle.goto(-140,100)
turtle.goto(-92,120)
turtle.up()
turtle.goto(24,74)
turtle.pencolor("Red")
turtle.color("Red")
turtle.down()
turtle.begin_fill()
turtle.circle(radius=15)
turtle.end_fill()
turtle.up()
turtle.goto(25,10)
turtle.pencolor("burlywood3")
turtle.color("burlywood3")
turtle.down()
turtle.fillcolor("burlywood3")
turtle.fillcolor("burlywood3")
turtle.begin_fill()
for i in range(1):
    turtle.forward(-300)
    turtle.left(-90)
    turtle.forward(260)
    turtle.right(-90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(260)
    turtle.left(-90)
    turtle.forward(-235)
turtle.end_fill()
turtle.pencolor("black")
turtle.color("black")
turtle.write("I got a prime package", 17)


