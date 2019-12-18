#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Miles_Wieczorek
#Date
# 12-18-2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
miles = trtl.Turtle()
miles.turtlesize(2)
miles.pensize(5)


#movement functions
def up():
    miles.setheading(90)
    miles.forward(5)


def down():
    miles.setheading(270)
    miles.forward(5)


def left():
    miles.setheading(180)
    miles.forward(5)


def right():
    miles.setheading(0)
    miles.forward(5)


def space():
    miles.clear()

# making pensize bigger or smaller
def o():
    miles.pensize(15)


def p():
    miles.pensize(1)

# putting pen up and down
def u():
    if miles.pendown():
        miles.pendown()
    elif miles.penup():
        miles.pendown()


#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(space)
wn.onkeypress(o, "o")
wn.onkeypress(p, "p")
wn.onkeypress(u, "u")


#listen
wn.listen()

#mainloop
wn.mainloop()