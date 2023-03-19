import random
import colorgram
import turtle as turtleModule

turtleModule.colormode(255)
myTurtle = turtleModule.Turtle()
myTurtle.hideturtle()   
myTurtle.shape("turtle")


# Extract 6 colors from an image.
colors = colorgram.extract('noche-estrellada.jpg', 6)
hexadecimalColors = []
for color in colors:
    colorsTuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    hexadecimalColors.append(colorsTuple)

# print(hexadecimalColors)
myTurtle.penup()
myTurtle.setx(-200)
myTurtle.sety(-200)
myTurtle.pendown()

def create_dot():
        myTurtle.color(random.choice(hexadecimalColors))
        myTurtle.dot(20)
        myTurtle.penup()
        myTurtle.forward(50)
        myTurtle.pendown()

def move_to_next_line():
    myTurtle.penup()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(450)
    myTurtle.right(90)
    myTurtle.right(90)
    myTurtle.pendown()


for i in range(9):
    for j in range(9):
        create_dot()
    move_to_next_line()
    
 
screen = turtleModule.Screen()
screen.exitonclick()