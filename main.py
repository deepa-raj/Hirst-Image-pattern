## import colorgram
##
## # Extract 6 colors from an image.
## rgb_colors = []
## colors = colorgram.extract('hirst_image.jpg', 30)
##
## for color in colors:
##     r = color.rgb.r
##     g = color.rgb.g
##     b = color.rgb.b
##     new_color = (r, g, b)
##     rgb_colors.append(new_color)
## print(rgb_colors)

"""The ABOVE CODE IS FOR DETECTING COLORS FROM THE HIRST IMAGE----------, which is that below 'color_list' variable"""

import turtle as turtle_module
import random

tim = turtle_module.Turtle()

turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
"""hide the lines drawn from dots"""
tim.hideturtle()
"""hide the cursor or turtle"""

color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
              (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
              (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31),
              (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182),
              (19, 71, 63), (175, 192, 212)]


tim.setheading(225)
"""225 because Middle angle between 270 and 180 which is (270-180 = 90) then (90/2 = 45) then (45+180 = 225)"""
tim.forward(300)
"""300 because to set a point in that direction for correct flow while seeing in the screen"""
tim.setheading(0)
"""0 because to continue from that point"""
num_of_dots = 100
"""Total number of dots we want to print"""

for dots_count in range(1, num_of_dots + 1):
    # If we put instead (0, num_of_dots) it goes wrong direction

    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    tim.dot(20, random.choice(color_list))

    if dots_count % 10 == 0:
        """ % - to get 10 dots in the line and break or goes in next line after the 10 dots """
        tim.setheading(90)
        """We have to turn tim left to 90 degrees"""
        tim.forward(50)
        """Get into move forward by 50 paces"""
        tim.setheading(180)
        """Again turning tim to left so we'll set the heading to 180 degrees"""
        tim.forward(500)
        """ in 1st line total number of dots are 10 and each paces counts 50 so (50*10 = 500) """
        tim.setheading(0)
        """0 to change its direction to right"""


screen = turtle_module.Screen()
screen.exitonclick()