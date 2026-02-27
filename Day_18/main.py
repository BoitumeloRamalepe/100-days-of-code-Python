import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color =(r,g,b)
    return random_color

######## Challenge 1 - Draw a Square ############
# for line in range(4):
#     tim.forward(100)
#     tim.left(90)


########### Challenge 2 - Draw a Dashed Line ########
# for line in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


########### Challenge 3 - Draw Shapes ########
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
 
# for shape_side_n in range(3,10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


########### Challenge 4 - Random Walk ########
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))




