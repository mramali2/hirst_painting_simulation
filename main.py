import turtle

import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle.colormode(255)


###Use colorgram to extract colour palette from image.

# colors = colorgram.extract("spots.jpg", 40)
#
# rbg_colors=[]
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b= color.rgb.b
#     new_color = (r,g,b)
#
#     rbg_colors.append(new_color)
#print(rbg_colors)

#List of colours generated from colorgram to use as random colours for painting.

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
              (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
              (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
              (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
              (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231),
              (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]


#Set turtles starting position for painting

timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.forward(500)


for i in range(10):
#At the end of each row move turtle back to starting positoin for new row
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


    for i in range(10):
        #Randomly coloured dots for each row
        color = random.choice(color_list)

        timmy.dot(20, color)
        timmy.forward(50)

screen.exitonclick()






