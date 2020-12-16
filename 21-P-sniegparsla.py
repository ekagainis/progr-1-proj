import turtle
import random
prieks = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["yellow", "green", "white", "pink"]
##for i in range(10):
##    for i in range(2):
##        prieks.forward(100)
##        prieks.right(60)
##        prieks.forward(100)
##        prieks.right(120)
##    prieks.right(36)
##    prieks.colour(random.choice(colours))

prieks.penup()
prieks.forward(90)
prieks.left(45)
prieks.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            prieks.forward(30)
            prieks.backward(30)
            prieks.right(45)
        prieks.left(90)
        prieks.backward(30)
        prieks.left(45)
    prieks.right(90)
    prieks.forward(90)

for i in range(8):
    branch()
    prieks.left(45)

#prieks.color(random.choice(colours))
        
   
   
    
    


