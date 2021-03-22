'''
Name: Minh Vu Anh Phan
Class: C SCI 131
Project Name: finalproject.py
This program draws a square pattern with different angles and size with the same center point
and clouds with different colors and a spiral pattern.
This program also allows user to rotate any jpg images by 180 degrees
'''
import turtle
import random
from PIL import Image #import the Image package
from random import randint #import the randint package


class FinalProject: #class for all actions in the project
    def __init__(self):
        pass
    def pattern(self):
        turtle.getscreen().bgcolor("cyan") #change the background color to cyan
        turtle.color("purple")
        length = 10
        turtle.penup()
        turtle.goto((-200,0)) #move the turtle to the point (-200,0)
        colors = ["red","blue","black","white","purple"] #make a list of color to be used in the pattern
        for i in range(19):
            turtle.penup() #don't let the turtle draw
            turtle.forward(length) #move the turtle to the direction it is facing by length
            turtle.left(90) #turn left 90 degrees
            turtle.forward(length)
            turtle.pendown() #put the pen down to start drawing
            turtle.color(colors[i%len(colors)]) #choose the color in the range of the list
            for i in range(4):
                turtle.left(90)
                turtle.forward(length*2)
            turtle.penup()
            turtle.backward(length) #move backwards in the direction it is facing
            turtle.left(90)
            turtle.forward(length)
            turtle.right(170)
            length += 5

    def cloud(self):
        turtle.setheading(0) #set the turtle heading to the right
        for i in range(10):
            x = random.randint(0,300) #choose the x coordinate of the turtle
            y = random.randint(-200,200) #choose the y coordinate of the turtle
            turtle.goto(x,y)
            red = random.randint(1,250) #choose a random number for red value
            green = random.randint(1,255) #choose a random number for green value
            blue = random.randint(1,255) #choose a random number for blue value
            turtle.fillcolor(red,green,blue) #choose the filling color with the color composed of the three values
            for i in range(10,31,10):
                turtle.begin_fill() #begin to fill
                turtle.circle(i) #make a circle
                turtle.end_fill() #stop filling
                turtle.backward(i)
            for i in range(30,9,-10):
                turtle.begin_fill()
                turtle.circle(i)
                turtle.end_fill()
                turtle.backward(i)

    def spiral(self,length):
        turtle.pendown()
        turtle.color("grey")
        turtle.forward(length)
        for i in range(4):
            if i % 2 == 0:
                turtle.color("white")
            else:
                turtle.color("black")
            turtle.circle(length/2)
            turtle.left(90)
        turtle.left(10)
        if length > 5:
            self.spiral(length-0.5) #recall the recursive function

    def snowflake(self, length):
        if length > 5:
            turtle.forward(length)
            turtle.right(30)
            self.snowflake(length-3)
            turtle.left(60)
            self.snowflake(length-3)
            turtle.right(30)
            turtle.backward(length)

    def imageconfigure(self):
        pref = input("Do you want to rotate your image by 180 degrees? (y/n)") #input the answer of y or n for the pref
        if pref == "y":
            file = input("Copy and paste your file name and extension in current workspace: ") #input the name of the file on the same directory (folder)
            photo = Image.open(file) #open the file to edit
            newphoto = photo.rotate(180) #copy the file and edit on the new file
            newphoto.save('rotated180degree.jpg') #save the new photo on the same directory
            print("Your new photo has been saved under the name rotated180degree.jpg")
        else:
            print("You have chosen not to")
def main():
    turtle.speed(10) #turtle speed to the fastest speed
    turtle.colormode(255)  # change the color mode to 255 instead of 1.0
    final = FinalProject()
    turtle.penup()
    final.pattern()
    final.cloud()
    turtle.goto(0,-200)
    turtle.pendown()
    final.spiral(40)
    final.imageconfigure()
    turtle.setheading(90)
    for i in range(4):
        final.snowflake(15)
        turtle.right(90)
    turtle.done()
main()