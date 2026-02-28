import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [ (203, 165, 109), (150, 72, 48), (239, 245, 240), (232, 235, 241), (222, 202, 137), (171, 152, 41), (52, 93, 124), (135, 32, 23), (133, 162, 184), (198, 92, 72), (49, 123, 90), (14, 98, 74), (146, 178, 147), (69, 49, 41), (234, 176, 166), (162, 142, 157), (55, 45, 50), (150, 19, 23), (113, 75, 77), (185, 205, 174), (22, 82, 86), (48, 65, 81), (45, 61, 73), (90, 144, 126), (219, 177, 181), (108, 127, 154), (194, 83, 86), (178, 190, 208)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    

screen = turtle_module.Screen()
screen.exitonclick()